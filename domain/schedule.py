class Schedule:
    frequency     = ""
    runHours      = ""
    runDaysOfWeek = ""
    runWeeks      = ""
    runMonths     = ""
    startMinute   = ""
    startHour     = ""

    def __init__( self, frequency, runHours, runDaysOfWeek, runWeeks, runMonths, startMinute, startHour ):
        self.frequency     =  frequency
        self.runHours      =  runHours
        self.runDaysOfWeek =  runDaysOfWeek
        self.runWeeks      =  runWeeks
        self.runMonths     =  runMonths
        self.startMinute   =  startMinute
        self.startHour     =  startHour

    @staticmethod
    def createSchedule      ( frequency, runHours, runDaysOfWeek, runWeeks, runMonths, startMinute, startHour ):
        schedule = Schedule ( frequency, runHours, runDaysOfWeek, runWeeks, runMonths, startMinute, startHour )
        return schedule

    @staticmethod
    def createMinuteSchedule( frequency, runHours, runDaysOfWeek, startMinute ):
        schedule = Schedule ( frequency, runHours, runDaysOfWeek, "", "", startMinute, "")
        return schedule

    @staticmethod
    def createHourSchedule  ( frequency, runHours, runDaysOfWeek, startMinute ):
        schedule = Schedule ( frequency, runHours, runDaysOfWeek, "", "", startMinute, "")
        return schedule

    @staticmethod
    def createDaySchedule   ( runDaysOfWeek, startHour, startMinute ):
        schedule = Schedule ( '', '', runDaysOfWeek, '', '', startMinute, startHour )
        return schedule

    @staticmethod
    def createWeekSchedule   ( runDaysOfWeek, startHour, startMinute ):
        schedule = Schedule ( '', '', runDaysOfWeek, '', '', startMinute, startHour )
        return schedule