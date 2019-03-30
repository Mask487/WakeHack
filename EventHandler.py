import xml.etree.ElementTree as ET
import EventOBJ

def addEvent(event):
   xml = ET.parse('events.xml')
   root = xml.getroot()

   attrib = {}
   element = ET.Element('event')

   date = ET.Element('date')
   date.text = event.getDate()

   time = ET.Element('time')
   time.text = event.getTime()

   desc = ET.Element('desc')
   desc.text = event.getDescription()

   priority = ET.Element('priority')
   priority.text = event.getPriority()

   rep = ET.Element('rep')
   rep.text = event.getRepetition()

   element.append(date)
   element.append(time)
   element.append(desc)
   element.append(priority)
   element.append(rep)
   root.append(element)

   xml.write('events.xml')
def removeEvent(event):
   xml = ET.parse('events.xml')
   events = xml.findall('event')

   for e in events:
      #if e.find('date').text == event.getDate() and e.find('time').text == event.getTime() and e.find('desc').text == event.getDescription()


def getAllEvents():
    eventList = []

    xml = ET.parse('events.xml')

    events = xml.findall('event')

    for e in events:
        date = e.find('date').text
        time = e.find('time').text
        desc = e.find('desc').text
        priority = e.find('priority').text
        rep = e.find('rep').text

        temp = EventOBJ.Event(date, time, desc, priority, rep)

        eventList.append(temp)

    return eventList


def wipeEvents():
   xml = ET.parse('events.xml')
   root = xml.getroot()

   root.clear()

   xml.write('events.xml')








