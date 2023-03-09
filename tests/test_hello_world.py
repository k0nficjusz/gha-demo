"""Test for main class."""
import unittest

from src.main import Main # pylint: disable=import-error


class MessageTestCase(unittest.TestCase):
    """Message test class."""
    def test_hello_world(self):
        """Test for Main with hello world message."""
        main = Main()
        main.run()
        self.assertEqual(main.message, "Hello World")

if __name__ == '__main__':
    unittest.main()
