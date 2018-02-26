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

    def shift(self, direction, neighbours=None):
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

    def expand(self, direction, neighbours=None):
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

    def shrink(self, direction, neighbours=None):
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

        def undo_move(self):
            pass


    def is_valid(self):
        """Return boolean of whether this slice has enough toppings and
        is small enough.
        """
        return (
            (self.get_mush_count() >= self.slices.min_mush) and
            (self.get_tom_count() >= self.slices.min_tom) and
            (self.get_size() <= self.slices.max_size)
        )


    def score_size(self, size_factor=1):
        """Score based on the size of this slice.
        """
        ideal = self.slices.min_mush + self.slices.min_tom
        return size_factor * abs(self.get_size() - ideal)


    def score_perim(self, perim_factor=1.0):
        """Score based on number of neighbouring sites owner by another slice.
        """
        n = 0.0

        # below
        if self.ri > 0:
            n += np.sum(self.slices.pizza[self.ri - 1, self.ci:self.cf + 1] > 0)
        # above
        if self.rf < self.slices.nrows - 1:
            n += np.sum(self.slices.pizza[self.rf + 1, self.ci:self.cf + 1] > 0)
        # left
        if self.ci > 0:
            n += np.sum(self.slices.pizza[self.ri:self.rf + 1, self.ci - 1] > 0)
        # right
        if self.cf < self.slices.ncols - 1:
            n += np.sum(self.slices.pizza[self.ri:self.rf + 1, self.cf + 1] > 0)

        return perim_factor * n


    def score_toppings(self, topping_factor=1):
        """Score based on which toppings this slice contains.
        """
        return topping_factor * (
            abs(self.get_mush_count() - self.slices.min_mush) +
            abs(self.get_tom_count() - self.slices.min_tom) +
        )


    def score(self):
        """Return the current score of this Slice.
        """
        SCORE_FNS = ['score_size', 'score_perim', 'score_toppings']
        return sum(getattr(self, fn)() for fn in SCORE_FNS)


    def cost_move(self, direction, move):
        """Compute the score differential of shifting in ``direction``.

        Parameters
        ----------
        direction : {'left', 'right', 'up', 'down'}
            Direction to perform move in.
        move : {'shift', 'expand', 'shrink'}
            What type of move to perform.

        Return
        ------
        difference in score before and after
        """
        move_fn = getattr(self, move)

        neighbours = self.get_neighbours(direction)
        score_before = sum(n.score() for n in neighbours)

        if not move_fn(direction, neighbours):
            return None

        score_after = sum(n.score() for n in neighbours)

        self.undo(direction, neighbours)
        return score_after - score_before
