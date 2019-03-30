import xml.etree.ElementTree as ET


xml = ET.parse('test.xml')
root = xml.getroot()
root.clear()
xml.write('test.xml')
events = ET.Element("events")
event = ET.SubElement(events, "event")
date = ET.SubElement(event, "date")
time = ET.SubElement(event, "time")
desc = ET.SubElement(event, "desc")
priority = ET.SubElement(event, "priority")
rep = ET.SubElement(event, "rep")

date1 = raw_input("What is your date? ")
time1 = raw_input("\nWhat is your time? ")
desc1 = raw_input("\nWhat is your desc? ")
priority1 = raw_input("\nWhat is your priority? ")
rep1 = raw_input("\nWhat is your rep? ")

date.text = date1
time.text = time1
desc.text = desc1
priority.text = priority1
rep.text = rep1

data = ET.tostring(events)
myfile = open("test.xml", 'w')
myfile.write(data)

print("test")
