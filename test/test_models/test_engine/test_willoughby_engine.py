import unittest
from models.engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    """ Test cases for WilloughbyEngine. """
    def test_instatiation(self):
        """ Test instatiation of WilloughbyEngine. """
        # Create a WilloughbyEngine.
        willoughby_engine = WilloughbyEngine(60000, 0)
        # Check if the WilloughbyEngine is an instance of WilloughbyEngine.
        self.assertIsInstance(willoughby_engine, WilloughbyEngine)

    def test_engine_should_be_serviced(self):
        """ Test if the engine should be serviced. """
        # Create a WilloughbyEngine.
        willoughby_engine = WilloughbyEngine(60001, 0)
        # Check if the engine should be serviced.
        self.assertTrue(willoughby_engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        """ Test if the engine should not be serviced. """
        # Create a WilloughbyEngine.
        willoughby_engine = WilloughbyEngine(60000, 0)
        # Check if the engine should not be serviced.
        self.assertFalse(willoughby_engine.needs_service())


if __name__ == '__main__':
    unittest.main()
