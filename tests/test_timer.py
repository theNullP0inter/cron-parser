import pytest
from cron_parser.timer import Timer

def test_timer():

    with pytest.raises(Exception):
        t = Timer("* *")
    
    with pytest.raises(Exception):
        t = Timer("* * * * * *")
    
    t = Timer("* * * * *")

    assert t.statement == "* * * * *"

    t = Timer("1 2 3 4 5")
    assert t.statement == "1 2 3 4 5"

    assert t.minute.value == 1
    assert t.hour.value == 2
    assert t.day.value == 3
    assert t.month.value == 4
    assert t.day_of_week.value == 5