import unittest
from automize_schedule_export_parser import AutomizeScheduleExportParser

export = 'data\schedules\EventScan_15@%%@true@%%@TaskTypes.WINCOMMAND@%%@EventScan_15_task_name@%%@@%%@15@%%@1@%%@18@%%@2@%%@5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,@%%@1,2,3,4,5,6,7,@%%@0,1,2,3,4,5,6,7,8,9,10,11,@%%@@%%@1,2,3,4,5@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@'

parser = AutomizeScheduleExportParser(export)

class TestExportParser(unittest.TestCase):

    def test_getTaskName_parses_correctly(self):    
        self.assertEqual('EventScan_15_task_name', parser.getTaskName())

    def test_isEnabled_returns_true(self):
        self.assertEqual('true', parser.isEnabled())

    def test_getTaskType_parses_correctly(self):
        self.assertEqual('WINCOMMAND', parser.getType())

    def test_getFrequency(self):
        self.assertEqual('15', parser.getFrequency())

    def test_getPeriodType(self):
        self.assertEqual('1', parser.getPeriodType())

    def test_getHour(self):
        self.assertEqual('18', parser.getHour())

    def test_getMinute(self):
        self.assertEqual('2', parser.getMinute())

    def test_getHours(self):
        self.assertEqual('5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,', parser.getHours())

    def test_getRunDays(self):
        self.assertEqual('1,2,3,4,5,6,7,', parser.getRunDays())

    def test_getMonths(self):
        self.assertEqual('0,1,2,3,4,5,6,7,8,9,10,11,', parser.getMonths())

    def test_getWeekDays(self):
        self.assertEqual('1,2,3,4,5', parser.getWeekDays())

if __name__ == '__main__':
    unittest.main() 