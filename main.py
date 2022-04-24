#Default courier codes
#Fedex : 11111
#UPS : 22222
#USPS : 33333
from locker import Locker
from input import Input

asciiArt = r"""
  _____                                 _     _                       _
 |  __ \                               | |   | |                     | |                 
 | |__) |   __ _   _ __    ___    ___  | |   | |        ___     ___  | | __   ___   _ __ 
 |  ___/   / _` | | '__|  / __|  / _ \ | |   | |       / _ \   / __| | |/ /  / _ \ | '__|
 | |      | (_| | | |    | (__  |  __/ | |   | |____  | (_) | | (__  |   <  |  __/ | |   
 |_|       \__,_| |_|     \___|  \___| |_|   |______|  \___/   \___| |_|\_\  \___| |_|   
                                                                                         
                                                                                         
"""
entryCodeError = "\nPlease try again!\nEnter your 5 digit specified code:\nCouriers! Enter your assigned code to drop off packages"
zipCodeError = "\nPlease enter a valid 5 digit zip Code:"
blankError = "{} cannot be blank.\nPlease enter a valid {}:"
packageTextError = "Please enter a text representing the package:"

while True:
    print(asciiArt)
    print("Parcel Locker")
    print("\nPlease enter your code:")
    print("\nCouriers! Enter your assigned code to drop off packages\n")
    entryCode = Input.numeric(entryCodeError, 5, 5)
    parcel = Locker()
    # returns true if the code entered in associated with a courier
    if parcel.is_drop_off(entryCode):
        print(f"Hello {parcel.courier}!\n")
        print("Please enter the recipient's first name:")
        firstName = Input.text(blankError.format("First name", "first name"))
        print("\nPlease enter the recipient's last name:")
        lastName = Input.text(blankError.format("Last name", "last name"))
        print("\nPlease enter the recipient's street address:")
        print("Enter apartment number if applicable")
        streetAddress = Input.text(blankError.format("Street Address", "street address"))
        print("\nPlease enter the recipient's 5-digit zip code:")
        zipCode = Input.numeric(zipCodeError, 5, 5)
        print("\nPlease place the package in the locker")
        print("Enter a piece of text as your package:\nIt's just a simulation!")
        package = Input.text(packageTextError)
        pickUpCode = parcel.drop_off(firstName, lastName, streetAddress, zipCode, package)
        print("\nThe recipient will need the code below to to pickup the package.\n")
        print(pickUpCode)
        print("\nThank you for using Parcel Locker!")
        print("\nPress enter to return to Parcel Locker")
        input()
    else: 
        package = parcel.pick_up(entryCode)
        # if the code entered if associated with a package that has not been picked up yet
        if package != False and package['pickedUp'] == 'False':
            print(f"\nPackage for {package['firstName']} {package['lastName']}")
            print(f"Package dropped off by {package['courier']} on {package['dateDroppedOff']} at {package['timeDroppedOff']}")
            print("Please pick Up your package from the locker")
            print(f"\n{package['item']}")
            print("\nThank you for using Parcel Locker!")
            print("\nPress enter to return to Parcel Locker")
            input()
        #if the code entered is associated with a package that has been picked up already.
        elif package != False and package['pickedUp'] == 'True':
            print(f"\nThe package has already been picked up on {package['datePickedUp']} at {package['timePickedUp']}.")
            print("Thank you!")
            print("\nPress enter to return to the Parcel Locker")
            input()
        #if there is no package associated with the code entered
        else:
            print(f"\nThere is no match for the code {entryCode}")
            print("Please try again.")
            print("\nPress enter to return to the Parcel Locker")
            input()
