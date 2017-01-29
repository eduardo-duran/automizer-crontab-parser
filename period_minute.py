from string_service import StringService as _string

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