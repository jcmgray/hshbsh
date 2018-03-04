from .input import load_data
from .output import write_journeys
from .taxi_lib import Taxi


def main_function(fname, outname=None, wide=True):
    settings, journeys = load_data(fname)

    taxis = [Taxi() for _ in range(settings.ntaxi)]

    if wide:
        any_valid = True
        while any_valid:
            any_valid = False

            # sort taxis by time
            taxis.sort(key=lambda taxi: taxi.time)

            for taxi in taxis:
                any_valid |= taxi.do_closest(journeys, settings)

    else:
        for taxi in taxis:
            has_valid_journey = True
            while has_valid_journey:
                has_valid_journey = taxi.do_closest(journeys, settings)

    if outname:
        write_journeys(taxis, outfilename=outname)

    return settings.score
