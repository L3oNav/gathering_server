

class RefiningGeneral:

    def __init__(self, response, return_rate):
        self.resources = response[::-1]
        self.return_rate = return_rate

    def calculator(self):
        refined = {}
        for tier in self.resources:
            refined.append(self._refiner(tier))
        return refined

    def _refiner(self, material):
        for values in material['value']:
            count = (values['value']+(values['value']*self.return_rate))// 5
            values['previous_tier'] = count
            values['can_refinig'] = values['previous_tier']
            values.pop('value')
        return material
