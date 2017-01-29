import unittest
from automize_to_crontab_converter import AutomizeToCrontabConverter

task='data\tasks\EventScan_15>TaskTypes.WINCOMMAND>task_name_EventScan_15>>D:\CORE\bin\EventNotifierCombo.bat>D:\CORE\bin>15>15>>^>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
export = 'data\schedules\EventScan_15@%%@true@%%@TaskTypes.WINCOMMAND@%%@EventScan_15_task_name@%%@@%%@15@%%@1@%%@18@%%@2@%%@5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,@%%@1,2,3,4,5,6,7,@%%@0,1,2,3,4,5,6,7,8,9,10,11,@%%@@%%@1,2,3,4,5@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@@%%@'

converter = AutomizeToCrontabConverter(task, export)

class TestAutomizeToCrontabConverter(unittest.TestCase):

    def test(self):
        self.assertEqual('1', '1')

if __name__ == '__main__':
    unittest.main() 