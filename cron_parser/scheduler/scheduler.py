from cron_parser.timer import Timer


class Scheduler:
    
    def __init__(self, statement):
        self.timer = Timer(" ".join(statement.split(" ")[:-1]))
        self.command = statement.split(" ")[-1]
    
    def printTask(self):
        
        self.timer.describe()
        print("command", self.command)

