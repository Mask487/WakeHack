import datetime as dt
class Event:
    def __init__(self,date,time,description,priority,repetition,tag=0000):
        self.date = date
        self.tag = tag
        self.time = time
        self.description = description
        self.priority = priority
        self.repetition = repetition

    def getDate(self):
        return self.date

    def getTag(self):
        return str(self.tag)

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

    def getTag(self):
        return self.tag


