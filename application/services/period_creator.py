from period_minute    import PeriodMinute
from period_hour      import PeriodHour
from period_day       import PeriodDay
from period_week      import PeriodWeek
from domain.schedule  import Schedule

class PeriodCreator:

    @staticmethod
    def create_period_from( scheduleParser ):
        SECONDS = '0'
        MINUTES = '1'
        HOURS   = '2'
        DAYS    = '3'
        WEEKS   = '4' 

        period_type  = scheduleParser.getPeriodType()

        frequency    = scheduleParser.getFrequency()
        runHours     = scheduleParser.getHours()
        runDays      = scheduleParser.getRunDays()
        runMonths    = scheduleParser.getMonths()
        start_minute = scheduleParser.getMinute()
        start_hour   = scheduleParser.getHour()

        if   period_type == SECONDS:
            return None

        elif period_type == MINUTES:
            schedule = Schedule.createMinuteSchedule( frequency, runHours, runDays, start_minute )
            return PeriodMinute( schedule )

        elif period_type == HOURS:
            schedule = Schedule.createHourSchedule  ( frequency, runHours, runDays, start_minute )
            return PeriodHour  ( schedule )

        elif period_type == DAYS:
            schedule = Schedule.createDaySchedule   ( runDays, start_hour, start_minute )
            return PeriodDay   ( schedule )

        elif period_type == WEEKS:
            schedule = Schedule.createWeekSchedule   ( runDays, start_hour, start_minute )
            return PeriodWeek  ( schedule )

        else:
            return None