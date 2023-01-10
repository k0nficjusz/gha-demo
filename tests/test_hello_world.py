
from src.main import Main

import unittest


class my_hello_world_test_case(unittest.TestCase):
    def test_hello_world(self):
        main = Main()
        main.run()
        self.assertEqual(main.message, "Hello World")

if __name__ == '__main__':
    unittest.main()