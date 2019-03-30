import datetime as dt
class Event:
    def __init__(self,date,time,description,priority,repetition):
        self.date = dt.datetime.strptime(date, "%m %d %Y").date()
        self.time = time
        self.description = description
        self.priority = priority
        self.repetition = repetition


    def getDate(self):
        self.date = dt.datetime.strftime(self.date, "%m %d %Y")
        return self.date

    def getTime(self):
        return self.time

    def getDescription(self):
        return self.description

    def getPriority(self):
        return self.priority

    def getRepetition(self):
        return self.repetition

    def setDate(self,month,day,year):
        self.date = dt.datetime(year,month,day)

    def setTime(self,hour,minute):
        self.time = dt.time(hour,minute)

    def setDescription(self,desc):
        self.description = desc

    def setPriority(self,priority):
        self.priority = priority

    def setRepetition(self,rep):
        self.repetition = rep



