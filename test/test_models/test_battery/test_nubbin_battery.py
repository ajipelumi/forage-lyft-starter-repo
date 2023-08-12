import unittest
from models.battery import NubbinBattery
from datetime import datetime


class TestNubbinBattery(unittest.TestCase):
    """ Test cases for NubbinBattery. """
    def test_instatiation(self):
        """ Test instatiation of NubbinBattery. """
        last_service_date = datetime(2019, 1, 1)
        current_date = datetime(2023, 1, 1)
        # Create a NubbinBattery.
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        # Check if the NubbinBattery is an instance of NubbinBattery.
        self.assertIsInstance(nubbin_battery, NubbinBattery)

    def test_battery_should_be_serviced(self):
        """ Test if the battery should be serviced. """
        last_service_date = datetime(2018, 1, 1)
        current_date = datetime(2023, 1, 1)
        # Create a NubbinBattery.
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        # Check if the battery should be serviced.
        self.assertTrue(nubbin_battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        """ Test if the battery should not be serviced. """
        last_service_date = datetime(2022, 1, 1)
        current_date = datetime(2023, 1, 1)
        # Create a NubbinBattery.
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        # Check if the battery should not be serviced.
        self.assertFalse(nubbin_battery.needs_service())


if __name__ == '__main__':
    unittest.main()
