from typing import Union

import yaml
from . import Path
from . import Logger
from . import datetime


class Param(dict):
    """
    a dictionary that supports dot notation
    as well as dictionary access notation
    usage: d = Param() or d = Param({'val1':'first'})
    set attributes: d.val2 = 'second' or d['val2'] = 'second'
    get attributes: d.val2 or d['val2']
    """
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __init__(self, dct):
        super().__init__()
        for key, value in dct.items():
            if hasattr(value, 'keys'):
                value = Param(value)
            self[key] = value


class Config:
    _last_read_access: datetime
    _last_write_access: datetime

    @classmethod
    def load(cls, path: Path) -> Union[Param, None]:
        if not path.exists():
            raise ConfigFileNotExist(path)
        with open(path, 'r') as fd:
            try:
                param = Param(yaml.safe_load(fd))
                Logger.info(f"{cls}: configuration loaded correctly")
                return param
            except yaml.YAMLError:
                Logger.error(f"{cls}: Error in loading the configuration {path}")
                return None
            finally:
                cls._log_read_access()

    @classmethod
    def save(cls, path: Path, config: Union[dict, Param]) -> bool:
        try:
            yaml.safe_dump(config)
            Logger.info(f"{cls}: configuration saved correctly")
            return True
        except yaml.YAMLError:
            Logger.error(f"{cls}: Error saving the configuration {path}")
            return False
        finally:
            cls._log_write_access()

    @classmethod
    def _log_read_access(cls):
        cls._last_read_access = datetime.now()
        Logger.debug(f"{cls}: New read access at {cls._last_read_access}")

    @classmethod
    def _log_write_access(cls):
        cls._last_write_access = datetime.now()
        Logger.debug(f"{cls}: New write access at {cls._last_write_access}")


class ConfigFileNotExist(Exception):
    def __init__(self, path):
        Logger.error(f"{self.__class__}: Error config path does not exist -> {path}")
