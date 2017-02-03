import unittest
from period_hour import PeriodHour
from schedule    import Schedule

class TestPeriodMinute(unittest.TestCase):
    
    def test_hours_are_divisors_of_day(self):
        hoursInDay = 24
        self.assertTrue( PeriodHour.divisible_by_hours_in_day(12) )
        self.assertTrue( PeriodHour.divisible_by_hours_in_day(8) )
        self.assertTrue( PeriodHour.divisible_by_hours_in_day(4) )
        self.assertTrue( PeriodHour.divisible_by_hours_in_day(1) )

    def test_hours_are_not_divisors_of_day(self):
        hoursInDay = 24
        self.assertFalse( PeriodHour.divisible_by_hours_in_day(13) )
        self.assertFalse( PeriodHour.divisible_by_hours_in_day(7) )
        self.assertFalse( PeriodHour.divisible_by_hours_in_day(5) )
        self.assertFalse( PeriodHour.divisible_by_hours_in_day(9) )

    def test_get_minutes_returns_zero(self):
        frequency = '1'
        dummy     = ''

        period = createPeriod( frequency, dummy, dummy, dummy )
        self.assertEqual('0', period.getMinutes())

    def test_getHours_with_two_different_runHours(self):
        runHours = '5,6,'
        dummy    = ''
        period = createPeriod( dummy, runHours, dummy, dummy )

        self.assertEqual('5,6', period.getHours())

    # def test_getDaysOfWeek(self):
    #     runDaysOfWeek = '2,3,4,5,6,'
    #     dummy   = ''
    #     period = createPeriod(dummy, dummy, runDaysOfWeek)

    #     self.assertEqual('2,3,4,5,6', period.getDaysOfWeek())

    # def test_getFormula(self):
    #     period = '20'
    #     runHours  = '5,6,9,'
    #     runDaysOfWeek   = '1,2,'
    #     period = createPeriod(period, runHours, runDaysOfWeek)

    #     self.assertEqual('*/20 5,6,9 * * 1,2', period.getFormula())

def createPeriod( frequency, runHours, runDaysOfWeek, startMinute ):
    schedule = Schedule.createHourSchedule ( frequency, runHours, runDaysOfWeek, startMinute )
    return PeriodHour( schedule )

if __name__ == '__main__':
    unittest.main() 