import unittest
from models.engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    """ Test cases for CapuletEngine. """
    def test_instatiation(self):
        """ Test instatiation of CapuletEngine. """
        # Create a CapuletEngine.
        capulet_engine = CapuletEngine(30000, 0)
        # Check if the CapuletEngine is an instance of CapuletEngine.
        self.assertIsInstance(capulet_engine, CapuletEngine)

    def test_engine_should_be_serviced(self):
        """ Test if the engine should be serviced. """
        # Create a CapuletEngine.
        capulet_engine = CapuletEngine(30001, 0)
        # Check if the engine should be serviced.
        self.assertTrue(capulet_engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        """ Test if the engine should not be serviced. """
        # Create a CapuletEngine.
        capulet_engine = CapuletEngine(30000, 0)
        # Check if the engine should not be serviced.
        self.assertFalse(capulet_engine.needs_service())


if __name__ == '__main__':
    unittest.main()
