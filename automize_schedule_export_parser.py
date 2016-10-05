
class AutomizeScheduleExportParser:
    def __init__(self, export):
        self.export = export
        self.schedule = export.split('@%%@')

    def parseTaskName(self):
        return self.schedule[3]

    def isEnabled(self):
        return self.schedule[1]

    def parseType(self):
        scheduleType = self.schedule[2]
        return scheduleType.replace('TaskTypes.', '')

    def parseFrequency(self):
        return self.schedule[5]

    def parsePeriodType(self):
        return self.schedule[6]

    def parseHour(self):
        return self.schedule[7]

    def parseMinute(self):
        return self.schedule[8]

    def parseHours(self):
        return self.schedule[9]

    def parseRunDays(self):
        return self.schedule[10]

    def parseMonths(self):
        return self.schedule[11]

    def parseWeekDays(self):
        return self.schedule[13]