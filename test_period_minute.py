import unittest
from period_minute import PeriodMinute

class TestPeriodMinute(unittest.TestCase):
    
    def test_getMinutes_with_minute_set_to_zero_by_default(self):
        frequency = '15'
        dummy     = ''
        period = createPeriod(frequency, dummy, dummy)

        self.assertEqual('*/15', period.getMinutes())

    def test_getHours_with_two_different_runHours(self):
        runHours = '5,6,'
        dummy    = ''
        period = createPeriod(dummy, runHours, dummy)

        self.assertEqual('5,6', period.getHours())

    def test_getDaysOfWeek(self):
        runDays = '2,3,4,5,6,'
        dummy   = ''
        period = createPeriod(dummy, dummy, runDays)

        self.assertEqual('2,3,4,5,6', period.getDaysOfWeek())

    def test_getFormula(self):
        frequency = '20'
        runHours  = '5,6,9,'
        runDays   = '1,2,'
        period = createPeriod(frequency, runHours, runDays)

        self.assertEqual('*/20 5,6,9 * * 1,2', period.getFormula())

def createPeriod(frequency, runHours, runDays):
    return PeriodMinute(frequency, runHours, runDays)

if __name__ == '__main__':
    unittest.main() 