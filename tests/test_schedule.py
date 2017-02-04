import unittest
from schedule import Schedule
class TestSchedule(unittest.TestCase):

    def test_creation_of_minute_task(self):
        schedule = Schedule.createMinuteSchedule( "2", "3", "4", "5" )
        self.assertEqual( schedule.frequency,     "2" )
        self.assertEqual( schedule.runHours,      "3" )
        self.assertEqual( schedule.runDaysOfWeek, "4" )
        self.assertEqual( schedule.startMinute,   "5" )

    def test_creation_of_day_task(self):
        schedule = Schedule.createDaySchedule( "runDaysOfWeek", "startHour", "startMinute" )
        self.assertEqual( schedule.runDaysOfWeek, "runDaysOfWeek" )
        self.assertEqual( schedule.startHour,     "startHour"     )
        self.assertEqual( schedule.startMinute,   "startMinute"   )

if __name__ == '__main__':
    unittest.main() 