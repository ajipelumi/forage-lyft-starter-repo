#!/usr/bin/python3
import unittest
from models.car import Car, CarFactory
from datetime import datetime


class TestCar(unittest.TestCase):
    """ Test cases for Car. """
    @classmethod
    def setUpClass(cls):
        """ Set up the test class. """
        # Create a CarFactory.
        cls.car_factory = CarFactory()

    def test_create_calliope(self):
        """ Test if a Calliope car can be created. """
        current_date = datetime(2023, 1, 1)
        last_service_date = datetime(2021, 1, 1)
        current_mileage = 10000
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]
        # Create a Calliope car.
        calliope = self.car_factory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)
        # Check if the Calliope car is an instance of Car.
        self.assertIsInstance(calliope, Car)

    def test_create_glissade(self):
        """ Test if a Glissade car can be created. """
        current_date = datetime(2023, 1, 1)
        last_service_date = datetime(2021, 1, 1)
        current_mileage = 10000
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]
        # Create a Glissade car.
        glissade = self.car_factory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)
        # Check if the Glissade car is an instance of Car.
        self.assertIsInstance(glissade, Car)

    def test_create_palindrome(self):
        """ Test if a Palindrome car can be created. """
        current_date = datetime(2023, 1, 1)
        last_service_date = datetime(2021, 1, 1)
        warning_light_on = True
        tire_wear = [0, 0, 0, 0]
        # Create a Palindrome car.
        palindrome = self.car_factory.create_palindrome(current_date, last_service_date, warning_light_on, tire_wear)
        # Check if the Palindrome car is an instance of Car.
        self.assertIsInstance(palindrome, Car)

    def test_create_rorschach(self):
        """ Test if a Rorschach car can be created. """
        current_date = datetime(2023, 1, 1)
        last_service_date = datetime(2021, 1, 1)
        current_mileage = 10000
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]
        # Create a Rorschach car.
        rorschach = self.car_factory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)
        # Check if the Rorschach car is an instance of Car.
        self.assertIsInstance(rorschach, Car)

    def test_create_thovex(self):
        """ Test if a Thovex car can be created. """
        current_date = datetime(2023, 1, 1)
        last_service_date = datetime(2021, 1, 1)
        current_mileage = 10000
        last_service_mileage = 0
        tire_wear = [0, 0, 0, 0]
        # Create a Thovex car.
        thovex = self.car_factory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)
        # Check if the Thovex car is an instance of Car.
        self.assertIsInstance(thovex, Car)


if __name__ == '__main__':
    unittest.main()
