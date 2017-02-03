class StringService:

    def __init__(self):
        StringService.__init__(self)
        pass

    @staticmethod
    def isEmpty(mystring):
        return (not mystring or mystring.isspace())

    @staticmethod
    def removeCommaFromLastChar(mystring):
        while mystring[-1] == ',':
            mystring = mystring[:-1]
        return mystring

    @staticmethod
    def replace_values_from_task(task, target, replacement):
        if task == target:
            return replacement

        result     = ''
        delimiter  = ','
        task_array = task.split(delimiter)
        
        for element in task_array:
            if element == target:
                result += replacement + delimiter
            else:
                result += element     + delimiter

        return result