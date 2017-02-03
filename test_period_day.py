import unittest
from period_day import PeriodDay
from schedule   import Schedule

class TestPeriodDay(unittest.TestCase):

    def test_getHours_with_startHour_8(self):
        startHour   = '8'
        dummy       = ''
        period      = createPeriod( dummy, startHour, dummy )

        hours       = period.getHours()

        expected    = "8"
        self.assertEqual( expected, hours )

    def test_getMinutes_with_startMinute_10(self):
        startMinute = '10'
        dummy       = ''
        period      = createPeriod( dummy, dummy, startMinute )

        minutes     = period.getMinutes()

        expected    = "10"
        self.assertEqual( expected, minutes )

    def test_getDaysOfWeek_with_one_value(self):
        days_of_week   = '2'
        dummy          = ''
        period         = createPeriod( days_of_week, dummy, dummy )

        days           = period.getDaysOfWeek()

        expected       = "2"
        self.assertEqual( expected, days )

    def test_getDaysOfWeek_with_two_values(self):
        days_of_week   = '2,3'
        dummy          = ''
        period         = createPeriod( days_of_week, dummy, dummy )

        days           = period.getDaysOfWeek()

        expected       = "2,3"
        self.assertEqual( expected, days )

    def test_getDaysOfWeek_with_zero_runDays_throw_exception(self):
        days_of_week   = '0'
        dummy          = ''
        period         = createPeriod( days_of_week, dummy, dummy )

        self.assertRaises( SystemExit, period.getDaysOfWeek )

    def test_getDaysOfWeek_with_empty_runDays_throw_exception(self):
        days_of_week   = ''
        dummy          = ''
        period         = createPeriod( days_of_week, dummy, dummy )

        self.assertRaises( SystemExit, period.getDaysOfWeek )

    def test_getDaysOfWeek_with_one_value_7_runDays_returns_0(self):
        days_of_week   = '7'
        dummy          = ''
        period         = createPeriod( days_of_week, dummy, dummy )

        days           = period.getDaysOfWeek()

        expected       = "0"
        self.assertEqual( expected, days )

    def test_getDaysOfWeek_with_two_values_with_7_runDays_converts_7_to_0(self):
        days_of_week   = '4,7'
        dummy          = ''
        period         = createPeriod( days_of_week, dummy, dummy )

        days           = period.getDaysOfWeek()

        expected       = "4,0"
        self.assertEqual( expected, days )

    def test_getDaysOfWeek_with_five_values_with_a_7_in_runDays_converts_7_to_0(self):
        days_of_week   = '2,3,4,5,7'
        dummy          = ''
        period         = createPeriod( days_of_week, dummy, dummy )

        days           = period.getDaysOfWeek()

        expected       = "2,3,4,5,0"
        self.assertEqual( expected, days )

    def test_getDaysOfMonth_is_ignored_and_returns_star(self):
        dummy          = 'any value'
        period         = createPeriod( dummy, dummy, dummy )

        days           = period.getDaysOfMonth()

        expected       = "*"
        self.assertEqual( expected, days )

    def test_getMonths_is_ignored_and_returns_star(self):
        dummy          = 'any value'
        period         = createPeriod( dummy, dummy, dummy )

        days           = period.getMonths()

        expected       = "*"
        self.assertEqual( expected, days )

    def test_getFormula_with_one_day(self):
        runDaysOfWeek   = '1'
        startHour       = '16'
        startMinute     = '4'
        period          = createPeriod( runDaysOfWeek, startHour, startMinute )

        formula         = period.getFormula()

        expected        = '4 16 * * 1'
        self.assertEqual( expected, formula )

    def test_getFormula_with_two_days(self):
        runDaysOfWeek   = '4,5'
        startHour       = '2'
        startMinute     = '52'
        period          = createPeriod( runDaysOfWeek, startHour, startMinute )

        formula         = period.getFormula()

        expected        = '52 2 * * 4,5'
        self.assertEqual( expected, formula )

    def test_getFormula_with_four_days_converting_7_to_0(self):
        runDaysOfWeek   = '2,4,5,7'
        startHour       = '5'
        startMinute     = '44'
        period          = createPeriod( runDaysOfWeek, startHour, startMinute )

        formula         = period.getFormula()

        expected        = '44 5 * * 2,4,5,0'
        self.assertEqual( expected, formula )

def createPeriod( runDaysOfWeek, startHour, startMinute ):
    schedule = Schedule.createDaySchedule ( runDaysOfWeek, startHour, startMinute )
    return PeriodDay( schedule )

if __name__ == '__main__':
    unittest.main() 