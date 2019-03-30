import EventOBJ
import EventHandler
import os


startMessage = "Welcome To Wake Scheduler\n1 -- View Events\n2 -- Add Event\n3 -- Remove Event\n4 -- End\n"
decision = 0
events = EventHandler.getAllEvents()

while decision != int(4):
    print(startMessage)
    decision = int(input("Please Enter What You Would Like To Do: "))
    events = EventHandler.getAllEvents()
    if decision == int(1):
        if events.__len__() == 0:
            print("No Events")
            decision = 0
        else:
            for e in events:
                print("Event: " + e.getTag())
                print("Date: " + e.getDate())
                print("Time: " + e.getTime())
                print("Description: " + e.getDescription())
                print("Priority: " + e.getPriority())
                print("---------------------------------\n")
            decision = 0
    elif decision == int(2):
        date = input("Please Enter Date(Format M D Y): ")
        time = input("Please Enter Time: ")
        desc = input("Please Enter Description: ")
        priority = input("Please Enter Priority: ")
        rep = input("Please Enter Repetition: ")

        event = EventOBJ.Event(date, time, desc, priority, rep)
        events = EventHandler.getAllEvents()

        if events.__contains__(event):
            print("Event Already Exists")
            decision = 0
        else:
            EventHandler.addEvent(event)
            decision = 0
    elif decision == int(3):
        event = input("Please Enter The Tag Of The Event You Want Removed: ")
        EventHandler.removeEvent(event)

        decision = 0
    elif decision == int(4):
        print("Exiting...")
    else:
        decision = input("You Dumb Fucker, You Had Once Job. Put In A Damn Number 1-4:")
