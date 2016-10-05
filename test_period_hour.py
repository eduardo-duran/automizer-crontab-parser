import unittest
from period_hour import PeriodHour

class TestPeriodMinute(unittest.TestCase):
    
    def test_hours_are_divisors_of_day(self):
        hoursInDay = 24
        self.assertTrue( hoursInDay % 12 == 0 )
        self.assertTrue( hoursInDay % 8 == 0 )
        self.assertTrue( hoursInDay % 4 == 0 )
        self.assertTrue( hoursInDay % 1 == 0 )

    def test_hours_are_not_divisors_of_day(self):
        hoursInDay = 24
        self.assertFalse( hoursInDay % 13 == 0 )
        self.assertFalse( hoursInDay % 7 == 0 )
        self.assertFalse( hoursInDay % 5 == 0 )
        self.assertFalse( hoursInDay % 9 == 0 )

    def test_get_minutes_returns_zero(self):
        dummy    = ''

        period = createPeriod('1', dummy)
        self.assertEqual('0', period.getMinutes())

    def test_getHours_with_two_different_runHours(self):
        runHours = '5,6,'
        dummy    = ''
        period = createPeriod(runHours, dummy)

        self.assertEqual('5,6', period.getHours())

    # def test_getDaysOfWeek(self):
    #     runDays = '2,3,4,5,6,'
    #     dummy   = ''
    #     period = createPeriod(dummy, dummy, runDays)

    #     self.assertEqual('2,3,4,5,6', period.getDaysOfWeek())

    # def test_getFormula(self):
    #     period = '20'
    #     runHours  = '5,6,9,'
    #     runDays   = '1,2,'
    #     period = createPeriod(period, runHours, runDays)

    #     self.assertEqual('*/20 5,6,9 * * 1,2', period.getFormula())

def createPeriod( runHours, runDays ):
    return PeriodHour( runHours, runDays )

if __name__ == '__main__':
    unittest.main() 