import unittest
from automize_schedule_export_parser import AutomizeScheduleExportParser

export = 'data\schedules\EventScan_15@%%@true@%%@TaskTypes.WINCOMMAND@%%@EventScan_15_task_name@%%@@%%@15@%%@1@%%@18@%%@2@%%@5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,@%%@1,2,3,4,5,6,7,@%%@0,1,2,3,4,5,6,7,8,9,10,11,@%%@@%%@1,2,3,4,5@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@'

parser = AutomizeScheduleExportParser(export)

class TestExportParser(unittest.TestCase):

    def test_parseTaskName_parses_correctly(self):    
        self.assertEqual('EventScan_15_task_name', parser.parseTaskName())

    def test_isEnabled_returns_true(self):
        self.assertEqual('true', parser.isEnabled())

    def test_parseTaskType_parses_correctly(self):
        self.assertEqual('WINCOMMAND', parser.parseType())

    def test_parseFrequency(self):
        self.assertEqual('15', parser.parseFrequency())

    def test_parsePeriodType(self):
        self.assertEqual('1', parser.parsePeriodType())

    def test_parseHour(self):
        self.assertEqual('18', parser.parseHour())

    def test_parseMinute(self):
        self.assertEqual('2', parser.parseMinute())

    def test_parseHours(self):
        self.assertEqual('5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,', parser.parseHours())

    def test_parseRunDays(self):
        self.assertEqual('1,2,3,4,5,6,7,', parser.parseRunDays())

    def test_parseMonths(self):
        self.assertEqual('0,1,2,3,4,5,6,7,8,9,10,11,', parser.parseMonths())

    def test_parseWeekDays(self):
        self.assertEqual('1,2,3,4,5', parser.parseWeekDays())

if __name__ == '__main__':
    unittest.main() 