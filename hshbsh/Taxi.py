import functools

class Taxi:
    def __init__(self):
        self.time = 0
        self.r = 0
        self.c = 0
        self.jids = []


    def do_closest(self, all_journeys):
        # filter journeys above - tls > self.time
        journeys_above = filter(lambda x: x.tls > self.time, all_journeys)

        # filter cone
        journeys_in_cone = tuple(filter(lambda x: abs(x.ts-self.time) >= abs(x.rs-self.r) + abs(x.rc-self.c), journeys_above))
        journeys_in_cone_late = tuple(filter(lambda x: abs(x.tls-self.time) >= abs(x.rs-self.r) + abs(x.rc-self.c), journeys_above))

        if len(journeys_in_cone_late) == 0:
            return False

        # compute distance to each
        nearest_by_start = functools.reduce(lambda x, y: min(x[1], y[1]), map(lambda x: (x.jid, x.ts - self.time), journeys_in_cone), float("inf"))
        nearest_by_latest_start = functools.reduce(lambda x, y: min(x[1], y[1]), map(lambda x: (x.jid, x.tls - self.time), journeys_in_cone_late))
        nearest = min(nearest_by_start[1], nearest_by_latest_start[1])

        # save id of nearest
        self.jids.append(nearest[0])

        # remove nearest
        del all_journeys[nearest[0]]

        return True