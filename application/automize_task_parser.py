
class AutomizeTaskParser:
    def __init__(self, task):
        self.task = task.split('@%%@')

    def getName(self):
        return self.task[2]

    def getFullPath(self):
        return self.task[4]

    def getPath(self):
        return self.task[5]

    def getFilename(self):
        return self.task[4].split('\\')[-1]