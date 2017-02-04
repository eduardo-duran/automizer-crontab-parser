import unittest
from application.automize_task_parser import AutomizeTaskParser

task='data\tasks\EventScan_15@%%@TaskTypes.WINCOMMAND@%%@EventScan_15_task_name@%%@@%%@D:\CORE\bin\EventNotifierCombo.bat@%%@D:\CORE\bin@%%@15@%%@15@%%@@%%@^@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@'

taskParser = AutomizeTaskParser(task)

class TestTaskParser(unittest.TestCase):

    def test_name_is_correctly_parsed(self):
        self.assertEqual('EventScan_15_task_name', taskParser.getName())

    def test_fullPath_is_correctly_parsed(self):
        self.assertEqual('D:\CORE\bin\EventNotifierCombo.bat', taskParser.getFullPath())

    def test_path_is_correctly_parsed(self):
        self.assertEqual('D:\CORE\bin', taskParser.getPath())

    def test_filename_is_correctly_parsed(self):
        self.assertEqual('EventNotifierCombo.bat', taskParser.getFilename())

if __name__ == '__main__':
    unittest.main()