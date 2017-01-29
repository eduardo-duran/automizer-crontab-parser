from string_service import StringService as _string

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
        hours = self.runHours
        if _string.isEmpty(hours):
            return '*'

        hours = _string.removeCommaFromLastChar(hours)
        return hours

    def getDaysOfMonth(self):
        return '*'

    def getMonths(self):
        return '*'

    def getDaysOfWeek(self):
        days = self.runDaysOfWeek
        if _string.isEmpty(days):
            return '*'

        days = _string.removeCommaFromLastChar(days)
        return days

# def isDayDivisibleBy(period):
#     return 24 % period == 0