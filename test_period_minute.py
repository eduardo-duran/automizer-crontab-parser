import unittest
from period_minute import PeriodMinute
from schedule      import Schedule

class TestPeriodMinute(unittest.TestCase):

    def test_minutes_are_divisors_of_an_hour(self):
        self.assertTrue( PeriodMinute.divisible_by_minutes_in_hour(1)  )
        self.assertTrue( PeriodMinute.divisible_by_minutes_in_hour(2)  )
        self.assertTrue( PeriodMinute.divisible_by_minutes_in_hour(3)  )
        self.assertTrue( PeriodMinute.divisible_by_minutes_in_hour(4)  )
        self.assertTrue( PeriodMinute.divisible_by_minutes_in_hour(5)  )
        self.assertTrue( PeriodMinute.divisible_by_minutes_in_hour(6)  )
        self.assertTrue( PeriodMinute.divisible_by_minutes_in_hour(10) )
        self.assertTrue( PeriodMinute.divisible_by_minutes_in_hour(12) )
        self.assertTrue( PeriodMinute.divisible_by_minutes_in_hour(15) )
        self.assertTrue( PeriodMinute.divisible_by_minutes_in_hour(20) )
        self.assertTrue( PeriodMinute.divisible_by_minutes_in_hour(30) )

    def test_minutes_are_not_divisors_of_an_hour(self):
        self.assertFalse( PeriodMinute.divisible_by_minutes_in_hour(7)  )
        self.assertFalse( PeriodMinute.divisible_by_minutes_in_hour(8)  )
        self.assertFalse( PeriodMinute.divisible_by_minutes_in_hour(9)  )
        self.assertFalse( PeriodMinute.divisible_by_minutes_in_hour(11) )
        self.assertFalse( PeriodMinute.divisible_by_minutes_in_hour(13) )
        self.assertFalse( PeriodMinute.divisible_by_minutes_in_hour(16) )
        self.assertFalse( PeriodMinute.divisible_by_minutes_in_hour(18) )
        self.assertFalse( PeriodMinute.divisible_by_minutes_in_hour(21) )
        self.assertFalse( PeriodMinute.divisible_by_minutes_in_hour(23) )
        self.assertFalse( PeriodMinute.divisible_by_minutes_in_hour(25) )
        self.assertFalse( PeriodMinute.divisible_by_minutes_in_hour(27) )
    
    def test_calculate_minutes_with_start_minute_set_to_5(self):
        frequency   = 15
        startMinute = 5

        minutes = PeriodMinute.calculate_minutes( frequency, startMinute )

        self.assertEqual( minutes, "5,20,35,50")

    def test_getMinutes_with_minute_set_to_zero_by_default(self):
        frequency   = '15'
        startMinute = '0'
        dummy       = ''
        period      = createPeriod(frequency, dummy, dummy, startMinute)

        self.assertEqual('0,15,30,45', period.getMinutes())

    def test_getMinutes_with_minute_set_to_6(self):
        frequency   = '15'
        startMinute = '6'
        dummy       = '0'
        period      = createPeriod(frequency, dummy, dummy, startMinute)

        self.assertEqual('6,21,36,51', period.getMinutes())

    def test_getMinutes_with_minute_set_to_21(self):
        frequency = '21'
        dummy     = '0'
        period    = createPeriod(frequency, dummy, dummy, dummy)

        self.assertEqual('*/21', period.getMinutes())

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
        startMinute = '0'
        period      = createPeriod(frequency, runHours, runDays, startMinute)

        self.assertEqual('0,20,40 5,6,9 * * 1,2', period.getFormula())

def createPeriod(frequency, runHours, runDays, startMinute):
    schedule = Schedule.createMinuteSchedule ( frequency, runHours, runDays, startMinute )
    return PeriodMinute( schedule )

if __name__ == '__main__':
    unittest.main() 