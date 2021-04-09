import unittest
from city_functions import get_city_function

class CityTestCase(unittest.TestCase):
    """Test for the city_function"""
    def test_city_country_place(self):
        """Do names like Tokiyo, Japan work?"""
        formatted_place = get_city_function('tokiyo','japan')
        self.assertEqual(formatted_place,'Tokiyo, Japan - Population ')

    def test_city_country_population_place(self):
        """Do name like San Fransisco, United States - Population 874,961"""
        formatted_place = get_city_function('san fransisco', 'united states','874,961')
        self.assertEqual(formatted_place,'San Fransisco, United States - Population 874,961')

if __name__ == '__main__':
    unittest.main()