class StockProfile:
    def __init__(self, name, cost, total, interval):
        """Download yahoo tickers
        :Parameters:
            name: str
                Name of the Stock you have
            cost: str                
                Average cost of the stock you own
            total: str
                Total number of stock you own
            interval : str
                Valid interval: daily,monthly,quarterly,yearly,five
                daily-15m/1d, monthly-1d/1mo, quarterly-1wk/3mo, yearly-1mo/2y, five-3mo/5y
                Length of data for subplots
        """
        self.name = name
        self.cost = cost
        self.total = total
        self.current_value = round(self.cost * self.total,2)
        #Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        #Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        if interval == "daily":
            self.period = '1d'
            self.interval = '15m'
        elif interval == "quarterly":
            self.period = '3mo'
            self.interval = '1wk'
        elif interval == "monthly":
            self.period = '1mo'
            self.interval = '1d'
        elif interval == "yearly":
            self.period = '2y'
            self.interval = '1mo'
        elif interval == "five":
            self.period = '5y'
            self.interval = '3mo'
        else:
            self.period = '5d'
            self.interval = '15m'

    def set_current(self, current_price):
        self.current_price = round(current_price, 2)
        self.net_value = current_price * self.total - self.current_value
        self.result = round(self.net_value, 2)
        if self.net_value > 0:
            self.color_text = 'green'
            self.color_bg = '#caffbf'
        else:
            self.color_text = 'red'
            self.color_bg = '#ffadad'

    def to_string(self):
        return f"{self.name} | shares {round(self.total,2)} | avg {round(self.cost,2)} " \
               f"| cur {self.current_price} | net {self.result}"
    

