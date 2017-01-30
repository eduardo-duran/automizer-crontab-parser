from string_service import StringService as _string

class PeriodMinute:
    def __init__(self, schedule):
        self.schedule = schedule

    def getFormula(self):
        return (self.getMinutes() + ' ' + 
               self.getHours() + ' ' +
               self.getDaysOfMonth() + ' ' +
               self.getMonths() + ' ' +
               self.getDaysOfWeek() )

    def getMinutes(self):
        minutes = '*/' + self.schedule.frequency
        return minutes

    def getHours(self):
        hours = self.schedule.runHours
        if _string.isEmpty(hours):
            return '*'

        hours = _string.removeCommaFromLastChar(hours)
        return hours

    def getDaysOfMonth(self):
        return '*'

    def getMonths(self):
        return '*'

    def getDaysOfWeek(self):
        days = self.schedule.runDaysOfWeek
        if _string.isEmpty(days):
            return '*'

        days = _string.removeCommaFromLastChar(days)
        return days