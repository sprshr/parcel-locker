import unittest
from locker import *
class TestLocker(unittest.TestCase):
    def setUp(self):
        self.fedex = Locker()
        self.ups = Locker()
        self.usps = Locker()
        self.wrongParcel = Locker()

    def test_is_drop_off(self):
        self.assertTrue(self.fedex.is_drop_off(1))
        self.assertEqual(self.fedex.courier, "FedEx")
        self.assertTrue(self.ups.is_drop_off(2))
        self.assertEqual(self.ups.courier, "UPS")
        self.assertTrue(self.usps.is_drop_off(3))
        self.assertEqual(self.usps.courier, "USPS")
        self.assertFalse(self.wrongParcel.is_drop_off(444))

    def tearDown(self):
        del self.fedex
        del self.ups
        del self.usps
        del self.wrongParcel

if __name__ == "__main__":
    unittest.main()