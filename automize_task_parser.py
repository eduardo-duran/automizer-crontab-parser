
class AutomizeTaskParser:
    def __init__(self, task):
        self.task = task

    def parseName(self):
        name = self.task.split('>>')
        name = name[0].split('>')
        return name[-1]

    def parseFullPath(self):
        fullpath = self.task.split('>>')
        fullpath = fullpath[1].split('>')
        return fullpath[0]

    def parsePath(self):
        path = self.task.split('>>')
        path = path[1].split('>')
        return path[1]

    def parseFilename(self):
        filename = self.task.split('>>')
        filename = filename[1].split('>')
        filename = filename[0].split('\\')
        return filename[-1]