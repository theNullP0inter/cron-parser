import pytest
from cron_parser.timer.field import Field

def test_min_max(mocker):

    f = Field(1,2)
    assert f.min == 1
    assert f.max == 2


def test_set_value(mocker):


    mocker.patch( 'cron_parser.timer.field.Field._get_all_values' , return_value="all")
    mocker.patch( 'cron_parser.timer.field.Field._get_range_values' , return_value="range")
    mocker.patch( 'cron_parser.timer.field.Field._get_list_values' , return_value="list")
    mocker.patch( 'cron_parser.timer.field.Field._get_step_values' , return_value="step")
    mocker.patch( 'cron_parser.timer.field.Field._get_simple_values' , return_value="simple")

    f = Field(10,100)
    
    f.set_value("*")
    assert f.value == "all"

    f.set_value("15-25")
    assert f.value == "range"

    f.set_value("25,30")
    assert f.value == "list"

    f.set_value("*/10")
    assert f.value == "step"

    f.set_value("25")
    assert f.value == "simple"

def test_simple_values():

    f = Field(10,30)
    assert f._get_simple_values("11") == 11
    assert f._get_simple_values("10") == 10

    with pytest.raises(Exception):
        f._get_simple_values("9")

    assert f._get_simple_values("29") == 29
    assert f._get_simple_values("30") == 30
    with pytest.raises(Exception):
        f._get_simple_values("31")

def test_all_values():
    f = Field(10,30)
    assert f._get_all_values() == [x for x in range(10, 31)]

def test_list_values():
    f = Field(10,30)

    assert f._get_list_values("10,11,13") == [10,11,13]
    assert f._get_list_values("10,11,30") == [10,11,30]

    with pytest.raises(Exception):
        f._get_list_values("9,10,13") 

    with pytest.raises(Exception):
        f._get_list_values("10,11,31") 


def test_step_values():
    f = Field(10,30)
    assert f._get_step_values("*/15") == [x for x in range(10, 31, 15)]
    assert f._get_step_values("12/15") == [x for x in range(12, 31, 15)]
    
    with pytest.raises(Exception):
        f._get_step_values("9/15")

    
        


    