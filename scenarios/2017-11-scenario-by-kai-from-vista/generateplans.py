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
    
    @staticmethod
    def distanceBetweenPoints(coordinate1, coordinate2):
        return math.sqrt((coordinate2.x - coordinate1.x)**2 + (coordinate2.y - coordinate1.y)**2)

class Shape:
    def __init__(self):
        self.min = Coordinate(math.inf,math.inf)
        self.max = Coordinate(-math.inf,-math.inf)

    def getRandomPosition(self):
        return Coordinate(random.uniform(self.min.x, self.max.x), random.uniform(self.min.y, self.max.y))

    @staticmethod
    def getClosestShapeFromCoordinate(startCoordinate, shapes):
        closestDistance = math.inf
        closestDistanceShape = shapes[0]
        for shape in shapes:
            toMinPointDistance = Coordinate.distanceBetweenPoints(startCoordinate, shape.min)
            toMaxPointDistance = Coordinate.distanceBetweenPoints(startCoordinate, shape.max)
            if toMinPointDistance < closestDistance or toMaxPointDistance < closestDistance:
                closestDistance = min(toMinPointDistance, toMaxPointDistance)
                closestDistanceShape = shape
        return closestDistanceShape

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

    def getTree(self):
        return ET.ElementTree(self.xmlElement)

    def writeTreeToFile(self, filename, header2 = ''):
        tree = self.getTree()
        header1 = '<?xml version="1.0" encoding="utf-8"?>'
        tree.write(filename)
        with open(filename, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(header1 + '\n' + header2 + '\n')
            f.write(content)

class Population(XmlElement):
    def __init__(self):
        XmlElement.__init__(self,'population')
    
    def generatePopulation(self, populationSize, startPolygon, endPolygons):
        for personNumber in range(populationSize):
            person = Person(personNumber, self.xmlElement)
            plan = Plan()
            startCoordinate = startPolygon.getRandomPosition()
            startActivity = Activity('At Home', startCoordinate, '01:00:00')
            plan.addActivity(startActivity)
            plan.addActivity(Leg('car'))
            endActivity = Activity('Go Home', Shape.getClosestShapeFromCoordinate(startCoordinate, endPolygons).getRandomPosition(), '03:00:00')
            plan.addActivity(endActivity)
            person.addPlan(plan)
            self.addPerson(person)

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

class NetworkChangeEvents(XmlElement):
    def __init__(self):
        XmlElement.__init__(self, 'networkChangeEvents')
        self.xmlElement.set('xmlns','http://www.matsim.org/files/dtd')
        self.xmlElement.set('xmlns:xsi','http://www.w3.org/2001/XMLSchema-instance')
        self.xmlElement.set('xsi:schemaLocation','http://www.matsim.org/files/dtd http://www.matsim.org/files/dtd/networkChangeEvents.xsd')
    
    def addNetworkChangeEvent(self, networkChangeEvent):
        self.addSubElement(networkChangeEvent.xmlElement)

    @staticmethod
    def addToTime(currentTime, addSeconds):
        currentTime = parser.parse(currentTime) + timedelta(seconds=addSeconds)
        return currentTime.strftime("%H:%M:%S")
        
    def generateNetworkChangeEvents(self, inputfile):
        current = 0
        startTime = '01:00:01'
        with open(inputfile, 'r') as floodingFile:
            for line in floodingFile:
                if(line[0] == "#"):
                    networkChangeEvent = NetworkChangeEvent(startTime)
                    startTime = self.addToTime(startTime,1)
                    if current != 0:
                        freespeed = Freespeed()
                        networkChangeEvent.addFreespeed(freespeed)
                    self.addNetworkChangeEvent(networkChangeEvent)
                    current += 1
                else:
                    id = line.strip()
                    link = Link(id)
                    networkChangeEvent.addLink(link)

class NetworkChangeEvent(XmlElement):
    def __init__(self, startTime = '01:00:01'):
        XmlElement.__init__(self, 'networkChangeEvent')
        self.xmlElement.set('startTime', startTime)
    
    def addFreespeed(self, freespeed):
        self.addSubElement(freespeed.xmlElement)
    
    def addLink(self, link):
        self.addSubElement(link.xmlElement)

class Freespeed(XmlElement):
    def __init__(self, speed = 0.000001):
        XmlElement.__init__(self, 'freespeed')
        self.xmlElement.set('type','absolute')
        self.xmlElement.set('value',format(speed, 'f'))

class Link(XmlElement):
    def __init__(self, id):
        XmlElement.__init__(self, 'link')
        self.xmlElement.set('refId', id)


#safe zone above creek
aboveCreek = Polygon(Coordinate(1.614234761040829E7,-4560734.749976564), Coordinate(1.6143367207888365E7,-4560898.8048608275), Coordinate(1.6142285026590563E7, -4561169.767607265), Coordinate(1.614330436803581E7,-4561331.897382162))

#safe zone below creek
belowCreek = Polygon(Coordinate(1.6143313774532782E7,-4566525.3373900475), Coordinate(1.6144027621899443E7,-4566781.843705078), Coordinate(1.6143215668665543E7,-4567264.97602887),Coordinate(1.6143947816956492E7,-4567382.626620158))

network = Network(ET.parse('net2.xml'))
population = Population()
population.generatePopulation(populationSize, network, [belowCreek,aboveCreek])
population.writeTreeToFile("generatedplans.xml", '<!DOCTYPE population SYSTEM "http://www.matsim.org/files/dtd/population_v6.dtd">')

networkChangeEvents = NetworkChangeEvents()
networkChangeEvents.generateNetworkChangeEvents("flooding.txt")
networkChangeEvents.writeTreeToFile("networkChangeEvents.xml")