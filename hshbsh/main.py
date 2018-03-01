from .input import load_data
from .output import write_journeys
from .taxi_lib import Taxi


def main_function(fname, outname='answer.txt'):
    settings, journeys = load_data(fname)

    taxis = [Taxi() for _ in range(settings.ntaxi)]

    any_valid = True
    while any_valid:
        any_valid = all(taxi.do_closest(journeys) for taxi in taxis)

    write_journeys(taxis, outfilename=outname)
