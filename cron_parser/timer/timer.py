from cron_parser.timer.field import Field

class Timer:

    statement = None
    
    minute = Field(0,59)
    hour = Field(0,23)
    day = Field(1,31)
    month = Field(1,12)
    day_of_week = Field(0,6)

    def __init__(self, cron_statement):
        self.statement = cron_statement
        
        statement = cron_statement.split(" ")

        if len(statement) != 5:
            raise Exception("Invalid Cron statement")

        self.minute.set_value(statement[0])
        self.hour.set_value(statement[1])
        self.day.set_value(statement[2])
        self.month.set_value(statement[3])
        self.day_of_week.set_value(statement[4])
    
    def describe(self):
        print("Minute", self.minute.value )
        print("Hour", self.hour.value )
        print("Day", self.day.value )
        print("Month", self.month.value )
        print("Day of Week", self.day_of_week.value )

