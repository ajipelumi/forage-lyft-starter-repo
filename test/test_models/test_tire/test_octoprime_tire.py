import unittest
from models.tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    """ Test cases for OctoprimeTire. """
    def test_instatiation(self):
        """ Test instatiation of OctoprimeTire. """
        # Hold array of 4 tires.
        tires = [0, 0, 0, 0]
        # Create a OctoprimeTire.
        octoprime_tire = OctoprimeTire(tires)
        # Check if the OctoprimeTire is an instance of OctoprimeTire.
        self.assertIsInstance(octoprime_tire, OctoprimeTire)

    def test_tire_should_be_serviced(self):
        """ Test if the tire should be serviced. """
        # Hold array of 4 tires.
        # Tire will be serviced if the sum of the tires is >= 3
        tires = [0.9, 0.9, 0.9, 0.9]
        # Create a OctoprimeTire.
        octoprime_tire = OctoprimeTire(tires)
        # Check if the tire should be serviced.
        self.assertTrue(octoprime_tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        """ Test if the tire should not be serviced. """
        # Hold array of 4 tires.
        # Tire will not be serviced if all of the sum of the tires is < 3
        tires = [0.7, 0.7, 0.7, 0.7]
        # Create a OctoprimeTire.
        octoprime_tire = OctoprimeTire(tires)
        # Check if the tire should not be serviced.
        self.assertFalse(octoprime_tire.needs_service())


if __name__ == '__main__':
    unittest.main()
