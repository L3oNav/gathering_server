

class RefiningRocks:

    def __init__(self, resources):
        self.resources = resources[::-1]

    def calculator(self):
        refined = []
        for tier in self.resources:
            refined.append(self._refiner(tier))
        return refined

    def _refiner(self, rock):
        for values in rock['value']:
            count = values['value'] // 5
            values['previous_tier'] = count
            if values['enchant'] == 1:
                values['previous_tier'] = count * 2
            if values['enchant'] == 2:
                values['previous_tier'] = count * 4
            if values['enchant'] == 3:
                values['previous_tier'] = count * 8
            values['can_refinig'] = values['previous_tier']
        return rock
