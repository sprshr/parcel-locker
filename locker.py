import sqlite3 as sq
import datetime
import telegram
from os import getenv
from random import randint
from dotenv import load_dotenv

load_dotenv()

class Locker:
    couriers = {"FedEx": 11111, "UPS": 22222, "USPS": 33333}
    databasePath = 'locker_log.db'
    columnHeaders = ("firstName", "lastName", "streetAddress", "zipCode",
                        "courier", "dateDroppedOff", "timeDroppedOff",
                        "pickUpCode", "item", "pickedUp", "datePickedUp", "timePickedUp")
    # botApiToken must be stored in a separate .env file
    botApiToken = getenv('botApiToken')
    channelID = "@parcelLocker"
    bot = telegram.Bot(botApiToken)
    
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
        # Initiates databases if does not exist
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

    #checks if the package is to be dropped off or picked up
    def is_drop_off(self, courierCode):
        for key in self.couriers:
            if self.couriers[key] == courierCode:
                self.courier = key
                return True
        else:
            return False

    #Inserts drop off info into the database & sends a notification to the telegram channel
    def drop_off(self, first, last, address, zipCode, item):
        zipCode = str(zipCode)
        digit = 0
        pickUpCode = ""
        while digit < 5:
            pickUpCode += str(randint(1, 9))
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
        self.conn.close()
        ### only takes HTML for formatting
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
        #if there is a package pending for the code entered
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
        #if there is no package for the code entered
        else:
            return False
        self.conn.close()
