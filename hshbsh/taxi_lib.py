
class Taxi:
    def __init__(self):
        self.time = 0
        self.r = 0
        self.c = 0
        self.jids = []

    def do_closest(self, all_journeys, B=0):

        journeys_in_cone = []
        journeys_in_cone_late = []
        for j in all_journeys.values():
            # filter journeys above - tls > self.time
            if j.tls < self.time:
                continue

            if abs(j.ts - self.time) >= abs(j.rs - self.r) + abs(j.cs - self.c):
                journeys_in_cone.append(j)

            elif abs(j.tls - self.time) >= abs(j.rs - self.r) + abs(j.cs - self.c):
                journeys_in_cone_late.append(j)

        if len(journeys_in_cone_late) + len(journeys_in_cone) == 0:
            return False

        # compute distance to each
        def time_difference(journey):
            return journey.ts - self.time - B

        def time_difference_earliest(journey):
            return abs(journey.rs - self.r) + abs(journey.cs - self.c)

        js_ts = [(time_difference(j), j) for j in journeys_in_cone]
        js_ts_late = [(time_difference_earliest(j), j)
                      for j in journeys_in_cone_late]

        if not js_ts:
            return False

        time, journey = min(js_ts , key=lambda x: x[0])

        # save id of nearest
        self.jids.append(journey.jid)

        # remove nearest
        del all_journeys[journey.jid]

        dist = (time + journey.length)

        self.r = journey.rd
        self.c = journey.cd

        self.time += dist

        return True
