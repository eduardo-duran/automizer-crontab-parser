from infrastructure.string_service import StringService as _string
from period_day                    import PeriodDay

class PeriodWeek:
    def __init__(self, schedule):
        self.period = PeriodDay( schedule )

    def getFormula(self):
        return self.period.getFormula()

    def getMinutes(self):
        return self.period.getMinutes()

    def getHours(self):
        return self.period.getHours()

    def getDaysOfMonth(self):
        return self.period.getDaysOfMonth()

    def getMonths(self):
        return self.period.getMonths()

    def getDaysOfWeek(self):
        return self.period.getDaysOfWeek()