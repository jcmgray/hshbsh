from .input import load_data
from .output import write_journeys
from .taxi_lib import Taxi


def main_function(fname, outname='answer.txt', wide=True):
    settings, journeys = load_data(fname)

    taxis = [Taxi() for _ in range(settings.ntaxi)]

    if wide:
        any_valid = True
        while any_valid:
            any_valid = all(taxi.do_closest(journeys)
                            for taxi in taxis)

    else:
        for taxi in taxis:
            has_valid_journey = True
            while has_valid_journey:
                has_valid_journey = taxi.do_closest(journeys)

    write_journeys(taxis, outfilename=outname)
