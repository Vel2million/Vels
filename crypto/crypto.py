import json
from nomics import Nomics
nomics = Nomics("b5f50663ab9d737a4dc97572316678b6")

markets = nomics.Markets.get_markets(exchange = 'binance')

dataset = nomics.Markets.get_market_cap_history(
    start = "2020-12-15T00:00:00Z",
    end = "2020-12-31T00:00:00Z"
)

print(json.dumps(dataset))