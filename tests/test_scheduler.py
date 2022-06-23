import pytest
from cron_parser.scheduler.scheduler import Scheduler

def test_scheduler():

    
    s = Scheduler("* * * * * /something.sh")

    assert s.timer.statement == "* * * * *"
    assert s.command == "/something.sh"