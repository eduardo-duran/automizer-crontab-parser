
class PeriodHour:
    def __init__(self, runHours, runDaysOfWeek):
        self.runHours = runHours
        self.runDaysOfWeek = runDaysOfWeek

    def getFormula(self):
        return (self.getMinutes() + ' ' + 
               self.getHours() + ' ' +
               self.getDaysOfMonth() + ' ' +
               self.getMonths() + ' ' +
               self.getDaysOfWeek() )

    def getMinutes(self):
        return '0'

    def getHours(self):

        return 'not divisible'

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

# def isDayDivisibleBy(period):
#     return 24 % period == 0