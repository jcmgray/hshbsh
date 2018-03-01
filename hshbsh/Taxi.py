import functools

class Taxi:
    def __init__(self):
        self.time = 0
        self.r = 0
        self.c = 0
        self.jids = []


    def do_closest(self, all_journeys):
        # filter journeys above - tls > self.time
        journeys_above = list(filter(lambda x: x.tls > self.time, all_journeys))

        # filter cone
        journeys_in_cone = list(filter(lambda x: abs(x.ts-self.time) >= abs(x.rs-self.r) + abs(x.cs-self.c), journeys_above))
        journeys_in_cone_late = list(filter(lambda x: abs(x.tls-self.time) >= abs(x.rs-self.r) + abs(x.cs-self.c), journeys_above))

        if len(journeys_in_cone_late) == 0:
            return False

        # compute distance to each
        nearest_by_start = functools.reduce(lambda x, y: min(x[1], y[1]), map(lambda x: (x.jid, x.ts - self.time), journeys_in_cone), (0, float("inf")))
        nearest_by_latest_start = functools.reduce(lambda x, y: min(x[1], y[1]), map(lambda x: (x.jid, x.tls - self.time), journeys_in_cone_late))
        nearest = nearest_by_start if nearest_by_start[1] >= nearest_by_latest_start[1] else nearest_by_latest_start

        # save id of nearest
        self.jids.append(nearest[0])

        # remove nearest
        journey_to_do = all_journeys[nearest[0]]
        del all_journeys[nearest[0]]

        dist = abs(journey_to_do.rs-self.r) + abs(journey_to_do.cs-self.c) + journey_to_do.length

        self.r = journey_to_do.rd
        self.c = journey_to_do.cd

        self.time += dist

        return True
