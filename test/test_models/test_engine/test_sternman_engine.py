import unittest
from models.engine import StermanEngine


class TestStermanEngine(unittest.TestCase):
    """ Test cases for StermanEngine. """
    def test_instatiation(self):
        """ Test instatiation of StermanEngine. """
        # Create a StermanEngine.
        sternman_engine = StermanEngine(False)
        # Check if the StermanEngine is an instance of StermanEngine.
        self.assertIsInstance(sternman_engine, StermanEngine)

    def test_engine_should_be_serviced(self):
        """ Test if the engine should be serviced. """
        # Create a StermanEngine.
        sternman_engine = StermanEngine(True)
        # Check if the engine should be serviced.
        self.assertTrue(sternman_engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        """ Test if the engine should not be serviced. """
        # Create a StermanEngine.
        sternman_engine = StermanEngine(False)
        # Check if the engine should not be serviced.
        self.assertFalse(sternman_engine.needs_service())


if __name__ == '__main__':
    unittest.main()
