import numpy as np


class Journey:
    def __init__(self, cs, rs, cd, rd, ts, td, jid):
        self.cs = cs
        self.rs = rs
        self.cd = cd
        self.rd = rd
        self.ts = ts
        self.td = td
        self.jid = jid

        self.calc_props()

    def calc_props(self):
        self.length = abs(self.cd - self.cs) + abs(self.rd - self.rs)
        self.tls = self.td - self.length - 1

    def __repr__(self):
        return (
            "Journey(cs={j.cs}, rs={j.rs}, cd={j.cd}, "
            "rd={j.rd}, ts={j.ts}, td={j.td}, jid={j.jid})".format(j=self))


class Settings:
    def __init__(self, nrow, ncol, ntaxi, nrides, bonus, tsteps):
        self.nrow = nrow
        self.ncol = ncol
        self.ntaxi = ntaxi
        self.nrides = nrides
        self.bonus = bonus
        self.tsteps = tsteps

    def __repr__(self):
        return (
            "Settings(nrow={s.nrow}, ncol={s.ncol}, ntaxi={s.ntaxi}, "
            "nrides={s.nrides}, bonus={s.bonus}, tsteps={s.tsteps})"
            "".format(s=self))


def gen_journeys(main_data):
    """Generate the Journeys from the main data.
    """
    for jid, line in enumerate(main_data):
        a, b, x, y, s, f = line
        yield jid, Journey(cs=b, rs=a, cd=y, rd=x, ts=s, td=f, jid=jid)


def load_data(fname):
    """Load data ``fname``

    Returns
    -------
    s, js : Settings, dict of Journeys
    """
    data = np.loadtxt(fname, dtype=int)

    R, C, F, N, B, T = data[0]
    s = Settings(nrow=R, ncol=C, ntaxi=F, nrides=N, bonus=B, tsteps=T)

    main_data = data[1:]
    js = {jid: j for jid, j in gen_journeys(main_data)}

    return s, js
