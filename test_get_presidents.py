from get_presidents import get_presidents
import pytest


def test_get_presidents():
    test_list = ["Washington", "Adams", "Jefferson", "Madison",
                 "Monroe", "Adams", "Jackson", "Buren", "Harrison",
                 "Tyler", "Polk", "Taylor", "Fillmore", "Pierce",
                 "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes",
                 "Garfield", "Arthur", "Cleveland", "Harrison",
                 "McKinley", "Roosevelt", "Taft", "Wilson",
                 "Harding", "Coolidge", "Hoover", "Roosevelt",
                 "Truman", "Eisenhower", "Kennedy", "Johnson",
                 "Nixon", "Ford", "Carter", "Reagan", "Bush",
                 "Clinton", "Bush", "Obama", "Trump"]
    president_list = get_presidents()

    for i in test_list:
        found = False
        for j in president_list:
            if (j.find(i) >= 0):
                found = True
                break
        assert found, i + " not found"



