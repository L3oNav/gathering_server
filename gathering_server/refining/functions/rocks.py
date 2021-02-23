

class RefiningRocks:

    def __init__(self, resources, return_rate=0.364, focus=30000):
        self.resources = resources[::-1]
        self.return_rate = return_rate

    def calculator(self):
        bridgewatch = []
        bridgewatch_focus = []
        for tier in self.resources:
            bridgewatch.append(self._bridgewatch(tier))
            #tier['bridgewatch_focus'] = bridgewatch_focus.append(self._bridgewatch_focus(tier))
        return { 'refined_bridgewatch': bridgewatch, 'refined_bridgewatch_focus': bridgewatch_focus }

    def _bridgewatch(self, rock):
        previous_tier = 0
        can_refinig = 0
        for values in rock['value']:
            count = (values['value'] + values['value'] * self.return_rate) // 5
            if values['enchant'] == 0:
                previous_tier += count
            if values['enchant'] == 1:
                previous_tier += count * 2
            if values['enchant'] == 2:
                previous_tier += count * 4
            if values['enchant'] == 3:
                previous_tier += count * 8
            values.pop('value')
        rock['value'] = {
            'can_refinig': int(previous_tier),
            'previous_tier': int(previous_tier)
        }
        return rock
