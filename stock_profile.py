class StockProfile:
    def __init__(self, name, cost, total):
        self.name = name
        self.cost = cost
        self.total = total

    def purchased_value(self):
        return round(self.cost * self.total,2)

    def set_current(self, current_price):
        self.current_price = current_price
        self.net_value = current_price * self.total - self.purchased_value()
        if self.net_value > 0:
            self.result = f"gain of {round(self.net_value,2)}"
        else:
            self.result = f"loss of {round(self.net_value,2)}"

    def to_string(self):
        return f"{round(self.total,2)} shares of {self.name}. At {round(self.cost,2)} is {self.result}"
    

