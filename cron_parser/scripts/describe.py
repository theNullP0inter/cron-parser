import argparse
from cron_parser.scheduler import Scheduler

def describe():

    parser = argparse.ArgumentParser(description='Describe a cronjob')
    parser.add_argument('statement', metavar='S', type=str,
                    help='Cron statement')

    args = parser.parse_args()
    scheduler = Scheduler(args.statement)
    scheduler.printTask()


    

