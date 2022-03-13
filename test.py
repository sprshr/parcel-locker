import unittest
from locker import *
from input import Input
class TestLocker(unittest.TestCase):
    def setUp(self):
        self.fedex = Locker()
        self.ups = Locker()
        self.usps = Locker()
        self.wrongParcel = Locker()

    def test_is_drop_off(self):
        self.assertTrue(self.fedex.is_drop_off(11111))
        self.assertEqual(self.fedex.courier, "FedEx")
        self.assertTrue(self.ups.is_drop_off(22222))
        self.assertEqual(self.ups.courier, "UPS")
        self.assertTrue(self.usps.is_drop_off(33333))
        self.assertEqual(self.usps.courier, "USPS")
        self.assertFalse(self.wrongParcel.is_drop_off(343654))

    def tearDown(self):
        del self.fedex
        del self.ups
        del self.usps
        del self.wrongParcel

if __name__ == "__main__":
    unittest.main()