class Slice:
    def __init__(self, pizza, owner, slices, ri, rf, ci, cf):
        self.ri = ri
        self.rf = rf
        self.ci = ci
        self.cf = cf

    def starve_count(self):
        pass

    def get_mush_count(self):
        pass

    def get_tom_count(self):
        pass

    def get_neighbours(self, direction):
        pass

    def get_border_ration(self):
        pass

    def shift(self, direction):
        pass

    def expand(self, direction):
        pass

    def shrink(self, direction):
        pass