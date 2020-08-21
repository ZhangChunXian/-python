import unittest
from city_functions import City_Country

class City_Country_TestCase(unittest.TestCase):

    def test_city_country(self):
        City_Country_string = City_Country('santiage', 'chile')
        self.assertEqual(City_Country_string, 'santiage, chile')
    def test_city_country_population(self):
        City_Country_string = City_Country('santiage', 'chile', '5000000')
        self.assertEqual(City_Country_string, 'santiage, chile- population 5000000')

if __name__ == '__main__':
    unittest.main()
