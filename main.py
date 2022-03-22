from locker import *
from input import Input
asciiArt = r"""
  _____                                 _     _                       _
 |  __ \                               | |   | |                     | |                 
 | |__) |   __ _   _ __    ___    ___  | |   | |        ___     ___  | | __   ___   _ __ 
 |  ___/   / _` | | '__|  / __|  / _ \ | |   | |       / _ \   / __| | |/ /  / _ \ | '__|
 | |      | (_| | | |    | (__  |  __/ | |   | |____  | (_) | | (__  |   <  |  __/ | |   
 |_|       \__,_| |_|     \___|  \___| |_|   |______|  \___/   \___| |_|\_\  \___| |_|   
                                                                                         
                                                                                         
"""
entryCodeError = "\nPlease enter your 5 digit specified code.\nCouriers! Enter your assigned code to drop off packages."
zipCodeError = "\nPlease enter a valid 5 digit zip Code"

print(asciiArt)
print("Parcel Locker\n")
print("Please enter your code\n")
print("Couriers! Enter your assigned code to drop off packages\n")
entryCode = Input.numeric(entryCodeError, 5, 5)

#returns if package is to be dropped off
parcel = Locker()
if parcel.is_drop_off(entryCode):
    print(f"Hello {parcel.courier}!\n")
    print("Please enter the recipient's first name:")
    firstName = input()
    print("\nPlease enter the recipient's last name:")
    lastName = input()
    print("\nPlease enter the recipient's street address")
    print("Enter apartment number if aplicable")
    streetAddress = input()
    print("\nPlease enter the recipient's 5-digit zip code")
    zipCode = Input.numeric()
    parcel.drop_off(firstName, lastName, streetAddress, zipCode)

else: 
    #pickup instructions go here
    pass