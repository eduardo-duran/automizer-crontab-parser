class DateService:

    def __init__(self):
        DateService.__init__(self)
        pass

    @staticmethod
    def decrease_1_day_to_match_crontab(days):
        result     = ''
        delimiter  = ','

        if len( days ) == 1:
            result = int( days ) - 1
            return   str( result )

        days = days.split( delimiter )
        for day in days:
            if not day:
                continue

            day     = int( day )
            day    -= 1
            result += str( day ) + delimiter
        
        return result