"""The overall Slices object which manages iterating.
"""


class Slices:

    def __init__(self, pizza, owner, min_mush, min_tom, max_size):
        self.pizza = pizza
        self.nrow, self.ncol = pizza.shape
        self.owner = owner
        self.min_mush = min_mush
        self.min_tom = min_tom
        self.max_size = max_size
        self.slice_map = dict()

    def addSlice(self, s, s_id):
        self.slice_map[s_id] = s

    def getSlice(self, i):
        return self.slice_map[i]

    def totalCost(self):
        return sum(s.score() for s in self.slice_map.values())

    def rangeOverSlices(self, n):

        for slc in self.slice_map.values():
            slc.update()

        return self.totalCost()
