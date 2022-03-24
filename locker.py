import sqlite3 as sq
import datetime

class Locker:
    couriers = {"FedEx": 11111, "UPS": 22222, "USPS": 33333}
    exists = False
    databasePath = 'locker_log.db'

    def __init__(self):
        self.conn = sq.connect(Locker.databasePath)
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('''CREATE TABLE locker_log(
                           firstName TEXT,
                           lastName TEXT,
                           streetAddress TEXT,
                           zipCode TEXT,
                           courier TEXT,
                           dateDroppedOff TEXT,
                           timeDroppedOff TEXT,
                           item TEXT
                           
            )''')
        except sq.Error:
            pass
        self.conn.commit()

    def is_drop_off(self, courierCode):
        for key in self.couriers:
            if self.couriers[key] == courierCode:
                self.courier = key
                return True
        else:
            return False

    def drop_off(self, first, last, address, zipCode, item):
        zipCode = str(zipCode)
        dt = datetime.datetime.now()
        dateDroppedOff = dt.strftime("%A, %B %d, %Y")
        timeDroppedOff = dt.strftime("%I:%M %p")
        with self.conn:
            self.cursor.execute(f"""INSERT INTO locker_log VALUES(
                    '{first}',
                    '{last}',
                    '{address}',
                    '{zipCode}',
                    '{self.courier}',
                    '{dateDroppedOff}',
                    '{timeDroppedOff}',
                    '{item}'
                    )""")
        # with self.conn:
        #     self.cursor.execute("SELECT * FROM locker_log")
        #     print(self.cursor.fetchall())
        # self.conn.close()