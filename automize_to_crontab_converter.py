from automize_schedule_export_parser import AutomizeScheduleExportParser
from automize_task_parser import AutomizeTaskParser

class AutomizeToCrontabConverter:
    def __init__(self, task, export):
        self.taskParser = AutomizeTaskParser(task)
        self.scheduleParser = AutomizeScheduleExportParser(export)

    
    