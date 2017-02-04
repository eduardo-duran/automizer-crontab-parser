class RangeService:

    def __init__(self):
        RangeService.__init__(self)
        pass

    @staticmethod
    def convert_to_range( target ):
        if len( target ) == 1:
            return target

        numbers = target.split( ',' )
        numbers = [ int(x) for x in numbers ]

        for index, value in enumerate( numbers ):
            if index == 0:
                continue

            previous_number = numbers[index - 1]
            current_number  = numbers[index]
            if ( current_number - 1) == previous_number:
                if index == len( numbers ) - 1:
                    result = str( numbers[0] ) + '-' + str ( numbers[index] )
                    return result

        return target

    @staticmethod
    def convert_list_to_range( values ):
        result = ''

        converted = []
        for group in values:
            converted.append( RangeService.convert_to_range( group ) )

        for index,value in enumerate( converted ):
            if index == len( converted ) - 1:
                result += value
                return result
            result += value + ' '
        
        return result
