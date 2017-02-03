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

        days = self.convert_seven_to_zeros( days )
        
        days = _string.removeCommaFromLastChar(days)
        return days

    @staticmethod
    def convert_seven_to_zeros(days):
        if days == '7':
            return '0'

        days_array = days.split(',')
        result = ''
        for day in days_array:
            if day == '7':
                result += '0,'
            else:
                result += day + ','

        return result