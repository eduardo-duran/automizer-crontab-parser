import sys
from automize_schedule_export_parser      import AutomizeScheduleExportParser
from automize_task_parser                 import AutomizeTaskParser
from application.services.period_creator  import PeriodCreator
from infrastructure.range_service         import RangeService as _range

class Program:
    def __init__(self, task, export):
        self.taskParser = AutomizeTaskParser(task)
        self.scheduleParser = AutomizeScheduleExportParser(export)

    @staticmethod
    def main():
        if len( sys.argv ) != 3:
            raise SystemExit( show_usage() )

        tasks_path     = sys.argv[1]
        schedules_path = sys.argv[2]
        
        tasks_unparsed     = get_list_from_file( tasks_path )
        schedules_unparsed = get_list_from_file( schedules_path )

        tasks = []
        for task in tasks_unparsed:
            tasks.append( AutomizeTaskParser(task) )

        schedules = []
        for schedule in schedules_unparsed:
            schedules.append( AutomizeScheduleExportParser(schedule) )

        for schedule in schedules:
            if not schedule.isEnabled:
                continue
            
            task = find_task_named( schedule.getTaskName(), tasks )

            if task is None:
                print ( schedule.getTaskName() + ' does not have matching task.' )
                continue

            period  = PeriodCreator.create_period_from( schedule )
            crontab = period.getFormula()
            crontab = _range.convert_list_to_range( crontab.split(' ') )

            print( task.getFullPath() + ' ' + crontab )


def show_usage():
    print( 'Usage:')
    print( 'python-script <path with tasks> <path with schedules>')

def get_list_from_file(filepath):
    lines = []
    with open(filepath) as f:
        for line in f:
            lines.append(line)
    return lines

def find_task_named(name, tasks):
    for task in tasks:
        if task.getName() == name:
            return task
    return None

if __name__ == '__main__':
    Program.main()