import unittest
from automize_task_parser import AutomizeTaskParser

task='data\tasks\EventScan_15>TaskTypes.WINCOMMAND>task_name_EventScan_15>>D:\CORE\bin\EventNotifierCombo.bat>D:\CORE\bin>15>15>>^>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'

taskParser = AutomizeTaskParser(task)

class TestTaskParser(unittest.TestCase):

    def test_name_is_correctly_parsed(self):    
        self.assertEqual('task_name_EventScan_15', taskParser.parseName())

    def test_fullPath_is_correctly_parsed(self):
        self.assertEqual('D:\CORE\bin\EventNotifierCombo.bat', taskParser.parseFullPath())

    def test_path_is_correctly_parsed(self):
        self.assertEqual('D:\CORE\bin', taskParser.parsePath())

    def test_filename_is_correctly_parsed(self):
        self.assertEqual('EventNotifierCombo.bat', taskParser.parseFilename())

if __name__ == '__main__':
    unittest.main()