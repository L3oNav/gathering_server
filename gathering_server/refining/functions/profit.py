import json


class RefiningProfit:
    def __init__(self,
                 resources,
                 prices,
                 prices_refined,
                 fee_percentage,
                 focus_from=6,
                 focus=30000):
        self.resources = resources
        self.prices = prices
        self.prices_refined = prices_refined
        self.fee_percentage = fee_percentage
        self.focus_from = focus_from
        self.focus = focus

    def _fee(self, product_value):
        return self.fee_percentage * product_value * 5 / 100

    def _profit_estimated(self, refined_price, resources_cost, product_value):
        return (refined_price - resources_cost +
                (resources_cost / 100 * self.return_rate) -
                self._fee(product_value))
