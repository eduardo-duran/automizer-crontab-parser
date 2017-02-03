from string_service import StringService as _string

class PeriodDay:
    def __init__(self, schedule):
        self.schedule = schedule

    def getFormula(self):
        return (self.getMinutes()      + ' ' + 
                self.getHours()        + ' ' +
                self.getDaysOfMonth()  + ' ' +
                self.getMonths()       + ' ' +
                self.getDaysOfWeek() )

    def getMinutes(self):
        return self.schedule.startMinute

    def getHours(self):
        return self.schedule.startHour

    def getDaysOfMonth(self):
        return '*'

    def getMonths(self):
        return '*'

    def getDaysOfWeek(self):
        days = self.schedule.runDaysOfWeek
        if _string.isEmpty(days) or days == '0':
            raise SystemExit('Run Days can not be null when using day period')

        days = _string.replace_values_from_task( days, '7', '0' )
        days = _string.removeCommaFromLastChar ( days )

        return days