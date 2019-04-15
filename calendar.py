"""
Command Line Calendar: A program to manage user's calendar. According some commands
you can View, Add, Update or Delete any event on the calendar
V1
April 14, 2019
"""
from time import sleep, strftime
from datetime import datetime

CONST_NAME = "Albert"
calendar = {}
today = datetime.now()

def welcome():
    print("Welcome %s" % CONST_NAME)
    sleep(1)
    print("Connecting to your calendar, please wait...")
    sleep(2)
    print("Calendar is ready")
    print(today.strftime("%A %B %d, %Y"))
    print(today.strftime("%H:%M:%S"))
    sleep(1)
    print("What would you like to do?: ")

def start_calendar():
    welcome()
    start = True
    while start:
        user_choice = input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
        if user_choice == "V" or user_choice == "v":
            if len(calendar) == 0:
                print("You have no events")
            else:
                for iCal in calendar:
                    print(iCal)
        elif user_choice == "U" or user_choice == "u":
            date = input("What date?: ")
            update = input("Enter the update: ")
            calendar[date] = update
            print("Updating...")
            sleep(1)
            print("Calendar has benn updated successfully")
            print(calendar)
        elif user_choice == "A" or user_choice == "a":
            event = input("Enter event: ")
            date = input("Enter date MM/DD/YYYY: ")
            if len(date) != 10 or int(date[6:10]) < int(today.strftime("%Y")):
                print("Wrong date")
                try_again = input("Wanna try again? Y for Yes, N for No: ")
                try_again = try_again.upper()
                if try_again == "Y":
                    continue
                else:
                    start = False
            else:
                calendar[date] = event
                print("Event added successfully")
                sleep(1)
                print(calendar)
        elif user_choice == "D" or user_choice == "d":
            if len(calendar) < 1:
                print("There's no event to delete")
                try_again = input("Wanna try again? Y for Yes, N for No: ")
                try_again = try_again.upper()
                if try_again == "Y":
                    continue
                else:
                    start = False
            else:
                event = input("What event?: ")
                for date in calendar.keys():
                    if event == calendar[date]:
                        del calendar[date]
                        print("Event has been deleted")
                        sleep(1)
                        print(calendar)
                        break
                    else:
                        print("Such event doesn't exist")
        elif user_choice == "X" or user_choice == "x":
            start = False
        else:
            print("Command not found")
            start = False

start_calendar()
