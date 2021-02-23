from .profit import *
from .rocks import *
from .general import *
from .searchPrices import *

class Refining:

    def __init__(self, response, return_rate=0.364):
        self.resources = response[::-1]
        self.return_rate = return_rate

    def calculator(self):
        refiner = []
        for tier in self.resources:
            refiner.append(self._refiner(tier))
        return refiner

    def _refiner(self, material):
        for values in material['value']:
            count = (values['value']+(values['value']*self.return_rate)) // 5
            values['previous_tier'] = count
            values['can_refinig'] = values['previous_tier']
            values.pop('value')
        return material
