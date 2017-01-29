class StringService:

    def __init__(self):
        StringService.__init__(self)
        pass

    @staticmethod
    def isEmpty(mystring):
        return (not mystring or mystring.isspace())
    @staticmethod
    def removeCommaFromLastChar(mystring):
        if mystring[-1] == ',':
            return mystring[:-1]
        return mystring