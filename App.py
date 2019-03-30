import EventOBJ
import EventHandler
import os


startMessage = "Welcome To The App You Dumb Bitch\n1 -- View Events\n2 -- Add Event\n3 -- Remove Event\n4 -- End\n"
input = 0
events = EventHandler.getAllEvents()

while int(input) != int(4):
    print(startMessage)
    input = raw_input("Please Enter What You Would Like To Do: ")
    #os.system('cls')
    if int(input) == int(1):
        if events.__len__() == 0:
            print("No Events")
            input = 0
        else:
            for e in events:
                print("Event")
                print("Date: " + e.getDate())
                print("Time: " + e.getTime())
                print("Description: " + e.getDescription())
                print("Priority: " + e.getPriority())
                print("---------------------------------\n")
            input = 0
    elif int(input) == int(2):
        date = raw_input("Please Enter Date(Format M D Y): ")
        time = raw_input("Please Enter Time: ")
        desc = raw_input("Please Enter Description: ")
        priority = raw_input("Please Enter Priority: ")
        rep = raw_input("Please Enter Repetition: ")

        event = EventOBJ.Event(date, time, desc, priority, rep)
        events = EventHandler.getAllEvents()

        if events.__contains__(event):
            print("Event Already Exists")
            input = 0
        else:
            EventHandler.addEvent(event)
            input = 0
    elif int(input) == int(3):
        print("Please Enter The Following Information Of The Event You Want Removed.")
        date = raw_input("Please Enter Date(Format M D Y): ")
        time = raw_input("Please Enter Time: ")
        desc = raw_input("Please Enter Description: ")
        priority = raw_input("Please Enter Priority: ")
        rep = raw_input("Please Enter Repetition: ")
        event = EventOBJ.Event(date, time, desc, priority, rep)
        EventHandler.removeEvent(event)

        input = 0
    elif int(input) == 4:
        print("Exiting...")
    else:
        input = raw_input("You Dumb Fucker, You Had Once Job. Put In A Damn Number 1-4:")
