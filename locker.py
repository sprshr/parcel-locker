import sqlite3 as sq
import datetime
from random import randint
import telegram


class Locker:
    couriers = {"FedEx": 11111, "UPS": 22222, "USPS": 33333}
    exists = False
    databasePath = 'locker_log.db'
    columnHeaders = ("firstName", "lastName", "streetAddress", "zipCode",
                        "courier", "dateDroppedOff", "timeDroppedOff",
                        "pickUpCode", "item", "pickedUp", "datePickedUp", "timePickedUp")
    botAPItoken = "5282147545:AAGHHXwAgbfq7LY0v77PdVLrIZ-aso20BjA"
    channelID = "@parcelLocker"
    bot = telegram.Bot(botAPItoken)
    @classmethod
    def get_date(cls):
        dt = datetime.datetime.now()
        return dt.strftime("%A %B %d, %Y")

    @classmethod
    def get_time(cls):
        dt = datetime.datetime.now()
        return dt.strftime("%I:%M %p")

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
                            pickUpCode TEXT,
                            item TEXT,
                            pickedUp TEXT,
                            datePickedUp TEXT,
                            timePickedUp TEXT
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
        digit = 0
        pickUpCode = ""
        while digit < 5:
            pickUpCode += str(randint(0, 9))
            digit += 1
        with self.conn:
            self.cursor.execute(f"""INSERT INTO locker_log VALUES(
                    '{first}',
                    '{last}',
                    '{address}',
                    '{zipCode}',
                    '{self.courier}',
                    '{Locker.get_date()}',
                    '{Locker.get_time()}',
                    '{pickUpCode}',
                    '{item}',
                    'False',
                    Null,
                    Null
                    )""")
        # with self.conn:
        #     self.cursor.execute("SELECT * FROM locker_log")
        #     print(self.cursor.fetchall())
        self.conn.close()
        message =f"<b>Package Dropped off</b>\nfor {first} {last}\non {Locker.get_date()} at {Locker.get_time()}\nby {self.courier}\npickup code: <b>{pickUpCode}</b>\nPlease pickup your package from Parcel Locker.\nThank you"    
        Locker.bot.send_message(Locker.channelID, message)
        return pickUpCode

    def pick_up(self, pickUpCode):
        pickUpCode = str(pickUpCode)
        try:
            with self.conn:
                self.cursor.execute(f"SELECT * FROM locker_log WHERE pickUpCode = {pickUpCode}")
                results = self.cursor.fetchone()
        except sq.OperationalError:
            results = None
        if results != None:
            dictResults = {}
            index = 0
            for header in Locker.columnHeaders:
                dictResults[header] = results[index]
                index += 1
            if dictResults['pickedUp'] == 'False':
                with self.conn:
                    self.cursor.execute(f"UPDATE locker_log SET pickedUp = 'True' WHERE pickUpCode = {pickUpCode}")
                    self.cursor.execute(f"UPDATE locker_log SET datePickedUp = '{Locker.get_date()}' WHERE pickUpCode = {pickUpCode}")
                    self.cursor.execute(f"UPDATE locker_log SET timePickedUp = '{Locker.get_time()}' WHERE pickUpCode = {pickUpCode}")
                message = f"<b>Package Picked up</b>\non {Locker.get_date()} at {Locker.get_time()}\nPickup Code {dictResults['pickUpCode']}"
                Locker.bot.send_message(Locker.channelID, message)
            return dictResults
        else:
            return False
        self.conn.close()