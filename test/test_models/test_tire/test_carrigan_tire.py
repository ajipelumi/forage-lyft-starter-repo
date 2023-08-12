import unittest
from models.tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    """ Test cases for CarriganTire. """
    def test_instatiation(self):
        """ Test instatiation of CarriganTire. """
        # Hold array of 4 tires.
        tires = [0, 0, 0, 0]
        # Create a CarriganTire.
        carrigan_tire = CarriganTire(tires)
        # Check if the CarriganTire is an instance of CarriganTire.
        self.assertIsInstance(carrigan_tire, CarriganTire)

    def test_tire_should_be_serviced(self):
        """ Test if the tire should be serviced. """
        # Hold array of 4 tires.
        # Tire will be serviced if one or more of the tires is >= 0.9
        tires = [0.9, 0, 0, 0]
        # Create a CarriganTire.
        carrigan_tire = CarriganTire(tires)
        # Check if the tire should be serviced.
        self.assertTrue(carrigan_tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        """ Test if the tire should not be serviced. """
        # Hold array of 4 tires.
        # Tire will not be serviced if all of the tires are < 0.9
        tires = [0.8, 0.8, 0.8, 0.8]
        # Create a CarriganTire.
        carrigan_tire = CarriganTire(tires)
        # Check if the tire should not be serviced.
        self.assertFalse(carrigan_tire.needs_service())


if __name__ == '__main__':
    unittest.main()
