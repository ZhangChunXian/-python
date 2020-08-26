# A Passing test
import unittest
from Testing_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    # Test for 'name_function.py'.

    # The method name must start with test_ so the method runs automatically when we run test_name_function.py
    def test_first_last_name(self):
        # Do names like 'Janis Joplin' work?
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        # Do names like "Wolfgang Amadeus Mozart" work?
        formatted_name = get_formatted_name('wolfgang', 'Mozart','amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':
    unittest.main()