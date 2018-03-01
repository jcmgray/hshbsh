from hshbsh import main_function
import os


def test_main():
    main_function('data/a_example.in')
    os.remove('answer.txt')
