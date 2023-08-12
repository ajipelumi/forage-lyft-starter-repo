import unittest
from models.battery import SplinderBattery
from datetime import datetime


class TestSplinderBattery(unittest.TestCase):
    """ Test cases for SplinderBattery. """
    def test_instatiation(self):
        """ Test instatiation of SplinderBattery. """
        last_service_date = datetime(2021, 1, 1)
        current_date = datetime(2023, 1, 1)
        # Create a SplinderBattery.
        splinder_battery = SplinderBattery(last_service_date, current_date)
        # Check if the SplinderBattery is an instance of SplinderBattery.
        self.assertIsInstance(splinder_battery, SplinderBattery)

    def test_battery_should_be_serviced(self):
        """ Test if the battery should be serviced. """
        last_service_date = datetime(2020, 1, 1)
        current_date = datetime(2023, 1, 1)
        # Create a SplinderBattery.
        splinder_battery = SplinderBattery(last_service_date, current_date)
        # Check if the battery should be serviced.
        self.assertTrue(splinder_battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        """ Test if the battery should not be serviced. """
        last_service_date = datetime(2022, 1, 1)
        current_date = datetime(2023, 1, 1)
        # Create a SplinderBattery.
        splinder_battery = SplinderBattery(last_service_date, current_date)
        # Check if the battery should not be serviced.
        self.assertFalse(splinder_battery.needs_service())


if __name__ == '__main__':
    unittest.main()
