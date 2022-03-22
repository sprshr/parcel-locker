import sqlite3 as sq

databasePath = 'locker_log.db'


class Locker:
    couriers = {"FedEx": 11111, "UPS": 22222, "USPS": 33333}
    exists = False
    #create database table
    @classmethod
    def create(self):
        try:
            self.conn = sq.connect(databasePath)
            self.cursor = self.conn.cursor()
            self.cursor.execute("""CREATE TABLE locker_log(
                               firstName text,
                               lastName text,
                               address text,
                               zipCode int,
                               pickUpCode int,
                               item text
            )""")
        except sq.Error:
            #exists is for testing purposes
            Locker.exists = True
        finally:
            Locker.exists = True

    def is_drop_off(self, courierCode):
        for key in self.couriers:
            if self.couriers[key] == courierCode:
                self.courier = key
                return True
        else:
            return False

    def drop_off(self, first, last, address, zipCode):
        pass