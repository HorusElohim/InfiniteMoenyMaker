import cbpro
import base64
from . import Logger, Config, Path
from .urls import CBSandbox, CBMain


class CBWsReceiver(cbpro.WebsocketClient):
    def __init__(self, config_path: Path, url=CBMain.ws_api, products=None, message_type="subscribe", channels=None):
        api = Config.load(config_path).coinbase.api
        super().__init__(url, products, message_type, None, True, True, api.key, api.secret, api.passphrase, channels)
        self.message_count = 0
        Logger.info(f"{self.__class__}: initialized")

    def on_open(self):
        Logger.info(f"{self.__class__}: opening connection")

    def on_message(self, msg):
        self.message_count += 1
        print(f"Message {msg}")

    def on_close(self):
        Logger.info(f"{self.__class__}: Total msg received({self.message_count}). Closing connection")
