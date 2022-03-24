#Avoid running the test to keep the database file!!!!!
#This test deletes the database file at /locker_log.db!!!!!

import unittest
import os
from locker import Locker


class TestLocker(unittest.TestCase):
    def setUp(self):
        try:
            os.remove(Locker.databasePath)
        except FileNotFoundError:
            pass
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

    def test_drop_off(self):
        self.fedex.is_drop_off(11111)
        self.fedex.drop_off("Sepehr", "Sahraian", "62 Clver Dr.", 92612, "This is the package")
        self.ups.is_drop_off(22222)
        self.ups.drop_off("Sepehr", "Sahraian", "62 Clver Dr.", 92612, "This is the package")
        self.usps.is_drop_off(33333)
        self.usps.drop_off("Sepehr", "Sahraian", "62 Clver Dr.", 92612, "This is the package")
        self.assertTrue(os.path.isfile(Locker.databasePath))

    def tearDown(self):
        del self.fedex
        del self.ups
        del self.usps
        del self.wrongParcel
        os.remove(Locker.databasePath)


if __name__ == "__main__":
    unittest.main()
