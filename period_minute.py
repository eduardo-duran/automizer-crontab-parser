
class PeriodMinute:
    def __init__(self, frequency, runHours, runDaysOfWeek):
        self.frequency = frequency
        self.runHours = runHours
        self.runDaysOfWeek = runDaysOfWeek

    def getFormula(self):
        return (self.getMinutes() + ' ' + 
               self.getHours() + ' ' +
               self.getDaysOfMonth() + ' ' +
               self.getMonths() + ' ' +
               self.getDaysOfWeek() )

    def getMinutes(self):
        minutes = '*/' + self.frequency
        return minutes

    def getHours(self):
        hours = self.runHours
        if isEmpty(hours):
            return '*'

        hours = removeCommaFromLastChar(hours)
        return hours

    def getDaysOfMonth(self):
        return '*'

    def getMonths(self):
        return '*'

    def getDaysOfWeek(self):
        days = self.runDaysOfWeek
        if isEmpty(days):
            return '*'

        days = removeCommaFromLastChar(days)
        return days

def isEmpty(mystring):
    return (not mystring or mystring.isspace())

def removeCommaFromLastChar(mystring):
    if mystring[-1] == ',':
        return mystring[:-1]
    return mystring