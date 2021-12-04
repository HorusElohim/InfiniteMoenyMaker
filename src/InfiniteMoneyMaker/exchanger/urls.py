from dataclasses import dataclass


@dataclass
class CBSandbox:
    website: str = "https://public.sandbox.exchange.coinbase.com"
    rest_api: str = "https://api-public.sandbox.exchange.coinbase.com"
    ws_api: str = "wss://ws-feed-public.sandbox.exchange.coinbase.com"
    fix_api: str = "tcp+ssl://fix-public.sandbox.exchange.coinbase.com:4198"


@dataclass
class CBMain:
    ws_api: str = "wss://ws-feed.pro.coinbase.com/"
