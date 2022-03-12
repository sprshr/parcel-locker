import unittest
from locker import *


class TestLocker(unittest.TestCase):
    def setUp(self):
        self.fedex = Locker()
        self.ups = Locker()
        self.usps = Locker()
        self.wrong_package = Locker()

    def test_drop_off(self):
        self.assertEqual(self.fedex.drop_off(1), 'FedEx')
        self.assertEqual(self.ups.drop_off(2), "UPS")
        self.assertEqual(self.usps.drop_off(3), "USPS")
        self.assertFalse(self.wrong_package.drop_off(454))


if __name__ == "__main__":
    unittest.main()