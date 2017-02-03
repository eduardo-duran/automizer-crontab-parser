from string_service import StringService as _string

class PeriodHour:
    def __init__(self, schedule):
        self.schedule = schedule

    def getFormula(self):
        return (self.getMinutes()      + ' ' + 
                self.getHours()        + ' ' +
                self.getDaysOfMonth()  + ' ' +
                self.getMonths()       + ' ' +
                self.getDaysOfWeek() )

    def getMinutes(self):
        return '0'

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

    @staticmethod
    def divisible_by_hours_in_day(hours):
        hours_in_day = 24
        return hours_in_day % int(hours) == 0

# def isDayDivisibleBy(period):
#     return 24 % period == 0