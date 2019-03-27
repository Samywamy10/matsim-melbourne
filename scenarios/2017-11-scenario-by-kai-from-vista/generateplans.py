import sys

populationSize = int(sys.argv[1])
from dateutil import parser
from datetime import timedelta
import xml.etree.ElementTree as ET
import math
import random

class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Shape:
    def __init__(self):
        self.min = Coordinate(math.inf,math.inf)
        self.max = Coordinate(-math.inf,-math.inf)

    def getRandomPosition(self):
        return Coordinate(random.uniform(self.min.x, self.max.x), random.uniform(self.min.y, self.max.y))

def getClosestRegion(startCoordinate, regions):
    closestDistance = math.inf
    closestDistanceRegion = regions[0]
    for region in regions:
        toMinPointDistance = distanceBetweenPoints(startCoordinate, region.min)
        toMaxPointDistance = distanceBetweenPoints(startCoordinate, region.max)
        if toMinPointDistance < closestDistance or toMaxPointDistance < closestDistance:
            closestDistance = min(toMinPointDistance, toMaxPointDistance)
            closestDistanceRegion = region
    return closestDistanceRegion

def distanceBetweenPoints(coordinate1, coordinate2):
    return math.sqrt((coordinate2.x - coordinate1.x)**2 + (coordinate2.y - coordinate1.y)**2)

class Polygon(Shape):
    def __init__(self,topLeft,topRight,bottomLeft,bottomRight):
        Shape.__init__(self)
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
        self.__calculateMinAndMax()
    
    def __calculateMinAndMax(self):
        #topLeft
        self.min.x = min(self.topLeft.x, self.min.x)
        self.max.x = max(self.topLeft.x, self.max.x)
        self.min.y = min(self.topLeft.y, self.min.y)
        self.max.y = max(self.topLeft.y, self.max.y)

        #topRight
        self.min.x = min(self.topRight.x, self.min.x)
        self.max.x = max(self.topRight.x, self.max.x)
        self.min.y = min(self.topRight.y, self.min.y)
        self.max.y = max(self.topRight.y, self.max.y)

        #bottomLeft
        self.min.x = min(self.bottomLeft.x, self.min.x)
        self.max.x = max(self.bottomLeft.x, self.max.x)
        self.min.y = min(self.bottomLeft.y, self.min.y)
        self.max.y = max(self.bottomLeft.y, self.max.y)

        #bottomRight
        self.min.x = min(self.bottomRight.x, self.min.x)
        self.max.x = max(self.bottomRight.x, self.max.x)
        self.min.y = min(self.bottomRight.y, self.min.y)
        self.max.y = max(self.bottomRight.y, self.max.y)

class Network(Shape):
    def __init__(self, networkXml):
        Shape.__init__(self)
        self.networkXml = networkXml
        self.__initNetwork()
        self.__calculateMinAndMax()
    
    def __initNetwork(self):
        self.root = self.networkXml.getroot()

    def __calculateMinAndMax(self):
        for child in self.root.iter('node'):
            self.min.x = min(float(child.attrib['x']),self.min.x)
            self.min.y = min(float(child.attrib['y']),self.min.y)
            self.max.x = max(float(child.attrib['x']),self.max.x)
            self.max.y = max(float(child.attrib['y']),self.max.y)

class XmlElement:
    def __init__(self, elementName):
        self.xmlElement = ET.Element(elementName)
    
    def getXml(self):
        return self.xmlElement

    def addSubElement(self, subElement):
        self.xmlElement.append(subElement)

class Population(XmlElement):
    def __init__(self):
        XmlElement.__init__(self,'population')
    
    def generatePopulation(self, populationSize, startRegion, endRegions):
        for personNumber in range(populationSize):
            person = Person(personNumber, self.xmlElement)
            plan = Plan()
            startCoordinate = startRegion.getRandomPosition()
            startActivity = Activity('At Home', startCoordinate, '01:00:00')
            plan.addActivity(startActivity)
            plan.addActivity(Leg('car'))
            endActivity = Activity('Go Home', getClosestRegion(startCoordinate, endRegions).getRandomPosition(), '03:00:00')
            plan.addActivity(endActivity)
            person.addPlan(plan)
            self.addPerson(person)

    def getTree(self):
        return ET.ElementTree(self.xmlElement)

    def addPerson(self, person):
        self.addSubElement(person.xmlElement)

class Person(XmlElement):
    def __init__(self, internalId, populationXml):
        XmlElement.__init__(self, 'person')
        self.__generateId()
        self.xmlElement.set('id',self.id)
        self.internalId = internalId
    
    def __generateId(self):
        self.id = str(random.randint(1000000000,9999999999))

    def addPlan(self, plan):
        self.addSubElement(plan.xmlElement)

class Plan(XmlElement):
    def __init__(self, selected = True):
        XmlElement.__init__(self, 'plan')
        if selected:
            self.xmlElement.set('selected','yes')
        else:
            self.xmlElement.set('selected','no')

    def addActivity(self, activity):
        self.addSubElement(activity.xmlElement)
    
    def addLeg(self, leg):
        self.addSubElement(leg.xmlElement)

class Activity(XmlElement):
    def __init__(self, typeName, coordinate, endTime):
        XmlElement.__init__(self, 'activity')
        self.xmlElement.set('type', typeName)
        self.xmlElement.set('x', str(coordinate.x))
        self.xmlElement.set('y', str(coordinate.y))
        self.xmlElement.set('end_time', endTime)

class Leg(XmlElement):
    def __init__(self, modeName):
        XmlElement.__init__(self, 'leg')
        self.xmlElement.set('mode',modeName)            



#safe zone above creek
above_creek = Polygon(Coordinate(1.614234761040829E7,-4560734.749976564), Coordinate(1.6143367207888365E7,-4560898.8048608275), Coordinate(1.6142285026590563E7, -4561169.767607265), Coordinate(1.614330436803581E7,-4561331.897382162))

#safe zone below creek
below_creek = Polygon(Coordinate(1.6143313774532782E7,-4566525.3373900475), Coordinate(1.6144027621899443E7,-4566781.843705078), Coordinate(1.6143215668665543E7,-4567264.97602887),Coordinate(1.6143947816956492E7,-4567382.626620158))




network = Network(ET.parse('net2.xml'))
population = Population()
population.generatePopulation(populationSize, network, [below_creek,above_creek])


tree = population.getTree()
header1 = '<?xml version="1.0" encoding="utf-8"?>'
header2 = '<!DOCTYPE population SYSTEM "http://www.matsim.org/files/dtd/population_v6.dtd">'

filename = "generatedplans.xml"

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
            startTime = addToTime(startTime,1)
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