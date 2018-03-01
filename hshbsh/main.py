from .input import load_data
from .taxi_lib import Taxi
from .output import writeJourneys


def main_function(fname):
    settings, journeys = load_data(fname)

    taxis = [Taxi() for _ in range(settings.ntaxi)]

    for taxi in taxis:

        has_valid_journey = True
        while has_valid_journey:
            has_valid_journey = taxi.do_closest(journeys)

    writeJourneys(taxis)
