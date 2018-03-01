from .input import load_data
from .output import write_journeys
from .taxi_lib import Taxi


def main_function(fname, outname):
    settings, journeys = load_data(fname)

    taxis = [Taxi() for _ in range(settings.ntaxi)]

    for taxi in taxis:

        has_valid_journey = True
        while has_valid_journey:
            has_valid_journey = taxi.do_closest(journeys)

    write_journeys(taxis, outfilename=outname)
