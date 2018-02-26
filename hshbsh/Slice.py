class Slice:
    def __init__(self, pizza, owner, slices, id, ri, rf, ci, cf):
        self.owner = owner
        self.slices = slices
        self.id = id
        self.pizza = pizza
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

    def _clear_slice(self):
        for i in range(self.ci, self.cf + 1):
            for j in range(self.ri, self.rf + 1):
                if self.owner[i][j] == self.id:
                    self.owner[i][j] = 0

    def _lay_slice(self):
        for i in range(self.ci, self.cf + 1):
            for j in range(self.ri, self.rf + 1):
                self.owner[i][j] = self.id

    def shift(self, direction):
        self._clear_slice()

        if direction == "up":
            self.ci -= 1
            self.cf -= 1
        elif direction == "down":
            self.ci += 1
            self.cf += 1
        elif direction == "left":
            self.ri -= 1
            self.rf -= 1
        elif direction == "right":
            self.ri += 1
            self.rf += 1

        self._lay_slice()

    def expand(self, direction):
        self._clear_slice()

        if direction == "up":
            self.ci -= 1
        elif direction == "down":
            self.cf += 1
        elif direction == "left":
            self.ri -= 1
        elif direction == "right":
            self.rf += 1

        self._lay_slice()

    def shrink(self, direction):
        self._clear_slice()

        if direction == "up":
            self.cf -= 1
        elif direction == "down":
            self.ci += 1
        elif direction == "left":
            self.rf -= 1
        elif direction == "right":
            self.ri += 1

        self._lay_slice()
