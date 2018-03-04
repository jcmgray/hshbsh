
class Taxi:
    def __init__(self):
        self.time = 0
        self.r = 0
        self.c = 0
        self.jids = []
        self._finished = False

    def __repr__(self):
        return ("Taxi(time={t.time}, r={t.r}, c={t.c}, "
                "jids={t.jids})".format(t=self))

    def do_closest(self, all_journeys, settings):

        if self._finished:
            return False

        journeys_in_cone = []
        journeys_in_cone_late = []

        for j in all_journeys.values():
            # filter journeys starting in past
            if j.tls < self.time:
                continue

            distance_from_j = abs(j.rs - self.r) + abs(j.cs - self.c)

            # can reach before first valid time to take
            if j.ts - self.time >= distance_from_j:
                journeys_in_cone.append(j)

            # can reach before last valid time to take
            elif j.tls - self.time >= distance_from_j:
                journeys_in_cone_late.append(j)

        if len(journeys_in_cone_late) + len(journeys_in_cone) == 0:
            self._finished = True
            return False

        # compute distance to each
        def time_difference(journey):
            time = journey.ts - self.time
            sort = time - settings.bonus
            score = journey.length + settings.bonus
            return sort, score, time

        def time_difference_earliest(journey):
            time = abs(journey.rs - self.r) + abs(journey.cs - self.c)
            sort = time
            score = journey.length
            return sort, score, time

        js_ts = [(*time_difference(j), j) for j in journeys_in_cone]
        js_ts_late = [(*time_difference_earliest(j), j)
                      for j in journeys_in_cone_late]

        best = min(js_ts + js_ts_late, key=lambda x: x[0])
        score, time, journey = best[1:]

        # save id of nearest
        self.jids.append(journey.jid)

        # remove nearest
        del all_journeys[journey.jid]

        dist = time + journey.length

        self.r = journey.rd
        self.c = journey.cd

        self.time += dist

        # add score to settings
        settings.score += score

        return True
