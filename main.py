from locker import *
asciiArt = r"""
  _____                                 _     _                       _
 |  __ \                               | |   | |                     | |                 
 | |__) |   __ _   _ __    ___    ___  | |   | |        ___     ___  | | __   ___   _ __ 
 |  ___/   / _` | | '__|  / __|  / _ \ | |   | |       / _ \   / __| | |/ /  / _ \ | '__|
 | |      | (_| | | |    | (__  |  __/ | |   | |____  | (_) | | (__  |   <  |  __/ | |   
 |_|       \__,_| |_|     \___|  \___| |_|   |______|  \___/   \___| |_|\_\  \___| |_|   
                                                                                         
                                                                                         
"""

print(asciiArt)
print("Parcel Locker\n")
print("Please enter your code\n")
print("Couriers! Enter your assigned code to drop off packages\n")
entry_code = int(input())

#returns if package is to be dropped off
parcel = Locker()
if parcel.is_drop_off(entry_code):
    print(f"Hello {parcel.courier}!\n")
    print("Please enter the recepient name:\n")
    recepientName = input()