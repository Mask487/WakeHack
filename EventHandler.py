import xml.etree.ElementTree as ET
import EventOBJ
import random

def addEvent(event):
   xml = ET.parse('events.xml')
   root = xml.getroot()

   attrib = {}
   element = ET.Element('event')

   date = ET.Element('date')
   date.text = event.getDate()

   tag = ET.Element('tag')
   tag.text = generateTag()

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
   element.append(tag)
   root.append(element)

   xml.write('events.xml')
def generateTag():
   xml = ET.parse('events.xml')
   root = xml.getroot()
   tagInt = random.randint(1000,9999)
   tagUsed = False
   for event in root.findall('event'):
      tag = event.find('tag')
      if tag is None:
         continue
      else:
         if tag.text is not str(tagInt):
            tagUsed = False
            continue
         else:
            tagUsed = True
   if tagUsed == False:
      return str(tagInt)
   else:
      generateTag()

def removeEvent(event):
   xml = ET.parse('events.xml')
   root = xml.getroot()
   events = xml.findall('event')

   for e in root.findall('event'):
      tag = e.find('tag')
      if tag.text is not event:
         continue
      else:
         root.remove(e)

   xml.write('events.xml')


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








