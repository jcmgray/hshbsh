class Slice:
    def __init__(self, pizza, owner, slices, id, ri, rf, ci, cf):
        self.last_neighbours = None
        self.last_dir = None
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
        return []

    def _clear_slice(self):
        for i in range(self.ci, self.cf + 1):
            for j in range(self.ri, self.rf + 1):
                if self.owner[i][j] == self.id:
                    self.owner[i][j] = 0

    def _lay_slice(self):
        for i in range(self.ci, self.cf + 1):
            for j in range(self.ri, self.rf + 1):
                self.owner[i][j] = self.id

    def _shrink_neighbours(self, direction, neighbours):
        self.last_dir = direction
        self.last_neighbours = []

        if direction == "up":
            for x in filter(lambda s: s.rf < self.ri, neighbours):
                x.shrink("up")
                self.last_neighbours.append(x)
        elif direction == "down":
            for x in filter(lambda s: s.ri > self.ri, neighbours):
                x.shrink("down")
                self.last_neighbours.append(x)
        elif direction == "left":
            for x in filter(lambda s: s.cf < self.ci, neighbours):
                x.shrink("left")
                self.last_neighbours.append(x)
        elif direction == "right":
            for x in filter(lambda s: s.ci > self.cf, neighbours):
                x.shrink("right")
                self.last_neighbours.append(x)

    def _can_move(self, direction):
        maxX, maxY = self.pizza.shape

        if direction == "up":
            if self.ri > 0:
                return True
        elif direction == "down":
            if self.rf < maxY:
                return True
        elif direction == "left":
            if self.ci > 0:
                return True
        elif direction == "right":
            if self.cf < maxX:
                return True
        return False

    def shift(self, direction, neighbours=None):
        if not self._can_move(direction):
            return False

        if neighbours is None:
            neighbours = self.get_neighbours()

        self._shrink_neighbours(direction, neighbours)

        self._clear_slice()

        if direction == "up":
            self.ri -= 1
            self.rf -= 1
        elif direction == "down":
            self.ri += 1
            self.rf += 1
        elif direction == "left":
            self.ci -= 1
            self.cf -= 1
        elif direction == "right":
            self.ci += 1
            self.cf += 1

        self._lay_slice()

        return True

    def expand(self, direction, neighbours=None):
        if not self._can_move(direction):
            return False

        if neighbours is None:
            neighbours = self.get_neighbours()

        self._shrink_neighbours(direction, neighbours)

        self._clear_slice()

        if direction == "up":
            self.ri -= 1
        elif direction == "down":
            self.rf += 1
        elif direction == "left":
            self.ci -= 1
        elif direction == "right":
            self.cf += 1

        self._lay_slice()

        return True

    def shrink(self, direction, neighbours=None):
        if direction == "right" or direction == "left":
            if not (self.ri < self.rf):
                return False

        if direction == "up" or direction == "down":
            if not (self.ci < self.cf):
                return False

        if neighbours is None:
            neighbours = self.get_neighbours()

        self._shrink_neighbours(direction, neighbours)

        self._clear_slice()

        if direction == "up":
            self.rf -= 1
        elif direction == "down":
            self.ri += 1
        elif direction == "left":
            self.cf -= 1
        elif direction == "right":
            self.ci += 1

        self._lay_slice()

        return True

    def undo_move(self):
        for s in self.last_neighbours:
            if self.last_dir == "up":
                s.expand("down")
            elif self.last_dir == "down":
                s.expand("up")
            elif self.last_dir == "left":
                s.expand("right")
            elif self.last_dir == "right":
                s.expand("left")
