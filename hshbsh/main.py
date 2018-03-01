from .input import load_data
from .Taxi import Taxi
from .output import writeJourneys


def main_function(fname):
    settings, journeys = load_data(fname)

    taxis = [Taxi() for _ in range(settings.ntaxi)]

    for taxi in taxis:
        while taxi.has_valid_journey:

            taxi.do_closest()

    writeJourneys(taxis)
