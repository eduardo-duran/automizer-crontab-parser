import unittest
from period_hour import PeriodHour
from schedule    import Schedule

class TestPeriodHour(unittest.TestCase):
    
    def test_hours_are_divisors_of_day(self):
        hoursInDay = 24
        self.assertTrue( PeriodHour.divisible_by_hours_in_day(12) )
        self.assertTrue( PeriodHour.divisible_by_hours_in_day(8)  )
        self.assertTrue( PeriodHour.divisible_by_hours_in_day(6)  )
        self.assertTrue( PeriodHour.divisible_by_hours_in_day(4)  )
        self.assertTrue( PeriodHour.divisible_by_hours_in_day(1)  )

    def test_hours_are_not_divisors_of_day(self):
        hoursInDay = 24
        self.assertFalse( PeriodHour.divisible_by_hours_in_day(13) )
        self.assertFalse( PeriodHour.divisible_by_hours_in_day(7)  )
        self.assertFalse( PeriodHour.divisible_by_hours_in_day(5)  )
        self.assertFalse( PeriodHour.divisible_by_hours_in_day(9)  )
        
    def test_calculate_hours_with_frequency_to_6(self):
        frequency   = 6

        hours       = PeriodHour.calculate_hours( frequency )

        expected    = "6,12,18,24,"
        self.assertEqual( expected, hours )

    def test_calculate_hours_with_frequency_to_8(self):
        frequency   = 8

        hours       = PeriodHour.calculate_hours( frequency )

        expected    = "8,16,24,"
        self.assertEqual( expected, hours )

    def test_getHours_with_frequency_to_8(self):
        frequency   = '8'
        dummy       = ''
        period      = createPeriod( frequency, dummy, dummy, dummy)

        hours       = period.getHours()

        expected    = "8,16,0"
        self.assertEqual( expected, hours )

    def test_getHours_with_frequency_to_7(self):
        frequency   = '7'
        dummy       = ''
        period      = createPeriod( frequency, dummy, dummy, dummy)

        hours       = period.getHours()

        expected    = "*/7"
        self.assertEqual( expected, hours )

    def test_getHours_with_frequency_to_13(self):
        frequency   = '13'
        dummy       = ''
        period      = createPeriod( frequency, dummy, dummy, dummy)

        hours       = period.getHours()

        expected    = "*/13"
        self.assertEqual( expected, hours )

    def test_getDaysOfWeek(self):
        runDaysOfWeek = '2,3,4,5,6,'
        dummy         = ''
        period        = createPeriod( dummy, dummy, runDaysOfWeek, dummy )

        days_of_week  = period.getDaysOfWeek()

        expected      = '2,3,4,5,6'
        self.assertEqual( expected, days_of_week )

    def test_getFormula_with_start_minute_0(self):
        frequency       = '6'
        runHours        = '5,6,9,'
        runDaysOfWeek   = '1,2,'
        startMinute     = '0'
        period          = createPeriod( frequency, runHours, runDaysOfWeek, startMinute )

        formula         = period.getFormula()

        expected        = '0 6,12,18,0 * * 1,2'
        self.assertEqual( expected, formula )

    def test_getFormula_with_start_minute_1(self):
        frequency       = '6'
        runHours        = '5,6,9,'
        runDaysOfWeek   = '1,2,'
        startMinute     = '1'
        period          = createPeriod( frequency, runHours, runDaysOfWeek, startMinute )

        formula         = period.getFormula()

        expected        = '1 6,12,18,0 * * 1,2'
        self.assertEqual( expected, formula )

    def test_getFormula_with_start_minute_56(self):
        frequency       = '6'
        runHours        = '5,6,9,'
        runDaysOfWeek   = '1,2,'
        startMinute     = '56'
        period          = createPeriod( frequency, runHours, runDaysOfWeek, startMinute )

        formula         = period.getFormula()

        expected        = '56 6,12,18,0 * * 1,2'
        self.assertEqual( expected, formula )

def createPeriod( frequency, runHours, runDaysOfWeek, startMinute ):
    schedule = Schedule.createHourSchedule ( frequency, runHours, runDaysOfWeek, startMinute )
    return PeriodHour( schedule )

if __name__ == '__main__':
    unittest.main() 