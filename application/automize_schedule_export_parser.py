
class AutomizeScheduleExportParser:
    def __init__(self, export):
        self.export = export
        self.schedule = export.split('@%%@')

    def getTaskName(self):
        return self.schedule[3]

    def isEnabled(self):
        return self.schedule[1]

    def getType(self):
        scheduleType = self.schedule[2]
        return scheduleType.replace('TaskTypes.', '')

    def getFrequency(self):
        return self.schedule[5]

    def getPeriodType(self):
        return self.schedule[6]

    def getHour(self):
        return self.schedule[7]

    def getMinute(self):
        return self.schedule[8]

    def getHours(self):
        return self.schedule[9]

    def getRunDays(self):
        return self.schedule[10]

    def getMonths(self):
        return self.schedule[11]

    def getWeekDays(self):
        return self.schedule[13]