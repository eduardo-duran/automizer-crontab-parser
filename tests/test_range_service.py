import unittest
from range_service import RangeService as _range

class TestRangeService(unittest.TestCase):

    def test_convert_to_range_correctly(self):
        pair      = '2,3'

        converted = _range.convert_to_range( pair )

        expected  = '2-3'
        self.assertEqual( expected, converted )

    def test_convert_to_range_with_3_values(self):
        pair      = '3,4,5'

        converted = _range.convert_to_range( pair )

        expected  = '3-5'
        self.assertEqual( expected, converted )

    def test_convert_to_range_returns_the_same_when_there_is_no_range(self):
        pair      = '5,6,8'

        converted = _range.convert_to_range( pair )

        expected  = '5,6,8'
        self.assertEqual( expected, converted )

    def test_convert_list_of_values_to_range(self):
        values    = []
        values.append( '0,1,2' )
        values.append( '4,5,6' )

        converted = _range.convert_list_to_range( values )

        expected  = '0-2 4-6'
        self.assertEqual( expected, converted )

    def test_convert_list_of_values_to_range_with_stars(self):
        values    = []
        values.append( '12,13,14' )
        values.append( '*' )
        values.append( '24,25,26' )
        values.append( '4,5,7' )

        converted = _range.convert_list_to_range( values )

        expected  = '12-14 * 24-26 4,5,7'
        self.assertEqual( expected, converted )

if __name__ == '__main__':
    unittest.main() 