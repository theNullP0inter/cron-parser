from cron_parser.timer import Timer


class Scheduler:
    '''
        Scheduler can execute the jobs using a crontab

    '''
    
    def __init__(self, statement):
        self.timer = Timer(" ".join(statement.split(" ")[:-1]))
        self.command = statement.split(" ")[-1]
    
    def printTask(self):
        
        self.timer.describe()
        print("command", self.command)

    def executeTask(self):
        print("executing", self.command)

