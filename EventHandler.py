import xml.etree.ElementTree as ET
#import EventObj

def addEvent(event):
   xml = ET.parse('events.xml')
   root = xml.getroot()

   attrib = {}
   ele = root.makeelement('event', attrib)
   root.append(ele)

   attrib = {'name' : 'date'}
   date = root[0][len(root)-1].makeelement('date', attrib)
   ET.SubElement(root[len(root)-1], 'date', attrib)
   root[len(root) - 1][0].text = "event.getdate"

   attrib = {'name': 'time'}
   time = root[0][len(root) - 1].makeelement('time', attrib)
   ET.SubElement(root[len(root) - 1], 'time', attrib)
   root[len(root) - 1][0].text = "event.gettime"

   attrib = {'name': 'desc'}
   desc = root[0][len(root) - 1].makeelement('desc', attrib)
   ET.SubElement(root[len(root) - 1], 'desc', attrib)
   root[len(root) - 1][0].text = "event.getdesc"

   attrib = {'name': 'priority'}
   priority = root[0][len(root) - 1].makeelement('priority', attrib)
   ET.SubElement(root[len(root) - 1], 'priority', attrib)
   root[len(root) - 1][0].text = "event.getpriority"

   attrib = {'name': 'rep'}
   rep = root[0][len(root) - 1].makeelement('rep', attrib)
   ET.SubElement(root[len(root) - 1], 'rep', attrib)
   root[len(root) - 1][0].text = "event.getrep"

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


def wipeEvents():
   xml = ET.parse('events.xml')
   root = xml.getroot()

   root.clear()

   xml.write('events.xml')








