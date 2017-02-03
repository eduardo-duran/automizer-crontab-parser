from string_service import StringService as _string

class PeriodMinute:
    
    def __init__(self, schedule):
        self.schedule = schedule

    def getFormula(self):
        return (self.getMinutes()     + ' ' + 
                self.getHours()       + ' ' +
                self.getDaysOfMonth() + ' ' +
                self.getMonths()      + ' ' +
                self.getDaysOfWeek() )

    def getMinutes(self):
        minutes = self.schedule.frequency


        if self.divisible_by_minutes_in_hour( int(minutes) ):
            minutes = self.calculate_minutes( int(minutes), int(self.schedule.startMinute) )
            return minutes

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

    @staticmethod
    def divisible_by_minutes_in_hour(minutes):
        minutes_in_hour = 60
        return minutes_in_hour % int(minutes) == 0

    @staticmethod
    def calculate_minutes(minutes, startMinute):
        minutes_in_hour = 60
        minutes_count = startMinute
        result = str(startMinute) + ','

        while 1 == 1:
            minutes_count += minutes
            if minutes_count >= minutes_in_hour:
                break
            result += str(minutes_count) + ','
        return _string.removeCommaFromLastChar( result )