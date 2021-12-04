import cbpro
from . import Logger, Config, Path, datetime
from .urls import CBSandbox, CBMain


class CBWsReceiver(cbpro.WebsocketClient):
    open_date: datetime
    close_date: datetime

    def __init__(self, config_path: Path, url=CBMain.ws_api, products=None, message_type="subscribe", channels=None):
        api = Config.load(config_path).coinbase.api
        super().__init__(url, products, message_type, None, True, True, api.key, api.secret, api.passphrase, channels)
        self.message_count = 0

        Logger.info(f"{self.__class__}: initialized")

    def on_open(self):
        self.open_date = datetime.now()
        Logger.info(f"{self.__class__}: opening connection at {self.open_date}")

    def on_message(self, msg):
        self.message_count += 1
        print(f"Message {msg}")

    def on_close(self):
        self.close_date = datetime.now()
        Logger.info(f"{self.__class__}: Closing connection at {self.close_date}")
        self.print_communication_stats()

    def print_communication_stats(self):
        active_time = self.close_date - self.open_date
        update_period = active_time / self.message_count
        update_frequency = 1 / update_period.total_seconds()
        Logger.info(f"{self.__class__}: Active time({active_time}),"
                    f" total msg received({self.message_count}),"
                    f" update frequency Hz ({update_frequency:6.4f})"
                    f" update period ({update_period})")

