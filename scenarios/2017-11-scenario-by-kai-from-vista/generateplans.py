import sys

number_of_plans = int(sys.argv[1])
from dateutil import parser
from datetime import timedelta
import xml.etree.ElementTree as ET
import math
import random
network = ET.parse('net2.xml')
root = network.getroot()
min_x = math.inf
min_y = math.inf
max_x = -math.inf
max_y = -math.inf
for child in root.iter('node'):
    min_x = min(float(child.attrib['x']),min_x)
    min_y = min(float(child.attrib['y']),min_y)
    max_x = max(float(child.attrib['x']),max_x)
    max_y = max(float(child.attrib['y']),max_y)

population = ET.Element('population')


for person in range(number_of_plans):
    current_person = ET.SubElement(population,'person')
    current_person.set('id',str(random.randint(1000000000,9999999999)))
    current_plan = ET.SubElement(current_person,'plan')
    current_plan.set('selected','yes')

    start_activity = ET.SubElement(current_plan,'activity')
    start_activity.set('type','At Home')
    start_x = random.uniform(min_x, max_x)
    start_y = random.uniform(min_y, max_y)
    start_activity.set('x',str(start_x))
    start_activity.set('y',str(start_y))
    start_activity.set('end_time', '01:00:00')

    leg = ET.SubElement(current_plan, 'leg')
    leg.set('mode','car')

    end_x = start_x
    end_y = start_y
    #we want to move people to the nearest edge except for min x
    x_dist = math.inf
    x_param = "min"
    if start_x - min_x > max_x - start_x: #closer to max x
        x_dist = max_x - start_x
        x_param = "max"
    else: #closer to min_x
        x_dist = start_x - min_x

    if start_y - min_y > max_y - start_y: #closer to max y
        if max_y - start_y > x_dist: #dist to y is greater than dist to x
            if x_param == "min":
                end_x = min_x
            else:
                end_x = max_x
        else:
            end_y = max_y
    else: #closer to min_y
        if start_y - min_y > x_dist: #dist to y is greater than dist to x
            if x_param == "min":
                end_x = min_x
            else:
                end_x = max_x
        else:
            end_y = min_y
        
    end_activity = ET.SubElement(current_plan, 'activity')
    end_activity.set('type','Go Home')
    end_activity.set('x',str(end_x))
    end_activity.set('y',str(end_y))
    end_activity.set('start_time', '00:00:00')
    end_activity.set('end_time', '03:00:00')

tree = ET.ElementTree(population)
header1 = '<?xml version="1.0" encoding="utf-8"?>'
header2 = '<!DOCTYPE population SYSTEM "http://www.matsim.org/files/dtd/population_v6.dtd">'

filename = "sampleplansgenerated.xml"

tree.write(filename)

with open(filename, 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    f.write(header1 + '\n' + header2 + '\n')
    f.write(content)

networkChangeEvents = ET.Element('networkChangeEvents')
networkChangeEvents.set('xmlns','http://www.matsim.org/files/dtd')
networkChangeEvents.set('xmlns:xsi','http://www.w3.org/2001/XMLSchema-instance')
networkChangeEvents.set('xsi:schemaLocation','http://www.matsim.org/files/dtd http://www.matsim.org/files/dtd/networkChangeEvents.xsd')


#major flooding
startTime = '01:00:01'
def addToTime(currentTime, addSeconds):
    currentTime = parser.parse(currentTime) + timedelta(seconds=addSeconds)
    return currentTime.strftime("%H:%M:%S")

current = 0
with open("flooding.txt", 'r') as majorFloodingFile:
    for line in majorFloodingFile:
        if(line[0] == "#"):
            if current != 0:
                freespeed = ET.SubElement(networkChangeEvent,'freespeed')
                freespeed.set('type','absolute')
                freespeed.set('value','0.00000001') #value of 0 causes errors
            networkChangeEvent = ET.SubElement(networkChangeEvents,'networkChangeEvent')
            networkChangeEvent.set('startTime',startTime)
            startTime = addToTime(startTime,30)
            current += 1
        else:
            Id = line.strip()
            link = ET.SubElement(networkChangeEvent,'link')
            link.set('refId',Id)
    freespeed = ET.SubElement(networkChangeEvent,'freespeed')
    freespeed.set('type','absolute')
    freespeed.set('value','0.00000001')






networkChangeEventsFile = "networkChangeEvents.xml"


networkChangeEventsTree = ET.ElementTree(networkChangeEvents)
networkChangeEventsTree.write(networkChangeEventsFile)
with open(networkChangeEventsFile, 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    f.write(header1 + '\n')
    f.write(content)