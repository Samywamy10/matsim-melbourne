import sys

number_of_plans = int(sys.argv[1])

import xml.etree.ElementTree as ET
import math
import random
tree = ET.parse('net2.xml')
root = tree.getroot()
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
    end_activity.set('end_time', '03:00:00')

tree = ET.ElementTree(population)
tree.write("sampleplansgenerated.xml")