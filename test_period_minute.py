import unittest
from period_minute import PeriodMinute
from schedule      import Schedule

class TestPeriodMinute(unittest.TestCase):
    
    def test_getMinutes_with_minute_set_to_zero_by_default(self):
        frequency = '15'
        dummy     = ''
        period    = createPeriod(frequency, dummy, dummy, dummy)

        self.assertEqual('*/15', period.getMinutes())

    def test_getHours_with_two_different_runHours(self):
        runHours = '5,6,'
        dummy    = ''
        period   = createPeriod(dummy, runHours, dummy, dummy)

        self.assertEqual('5,6', period.getHours())

    def test_getDaysOfWeek(self):
        runDays = '2,3,4,5,6,'
        dummy   = ''
        period  = createPeriod(dummy, dummy, runDays, dummy)

        self.assertEqual('2,3,4,5,6', period.getDaysOfWeek())

    def test_getFormula(self):
        frequency   = '20'
        runHours    = '5,6,9,'
        runDays     = '1,2,'
        startMinute = ''
        period      = createPeriod(frequency, runHours, runDays, startMinute)

        self.assertEqual('*/20 5,6,9 * * 1,2', period.getFormula())

def createPeriod(frequency, runHours, runDays, startMinute):
    schedule = Schedule.createMinuteSchedule ( frequency, runHours, runDays, startMinute )
    return PeriodMinute( schedule )

if __name__ == '__main__':
    unittest.main() 