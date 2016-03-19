import json


class Stock:

    def __init__(self):
        self.name = ""
        self.symbol = ""
        self.sector = ""
        self.industry = ""

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)


class StockDailyPriceData:

    def __init__(self):
        self.symbol = ""
        self.date = None
        self.volume = 0
        self.open = 0.0
        self.close = 0.0
        self.adj_close = 0.0
        self.high = 0.0
        self.low = 0.0

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)