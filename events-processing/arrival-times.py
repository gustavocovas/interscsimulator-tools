import sys
import pandas as pd
import xml.etree.ElementTree as ET

filename = sys.argv[1]

tree = ET.parse(filename)
root = tree.getroot()

arrival_times = []
avg_speeds = []
for child in root:
  if child.attrib['type'] == 'arrival':

    # Sample arrival event:
    # <event time="918" type="arrival" person="paraiso5_79" vehicle="paraiso5_79" link="40" legMode="car" trip_time="205" distance="2825" action="ok"/>

    trip_time = int(child.attrib['trip_time'])
    distance = int(child.attrib['distance'])

    arrival_times.append(trip_time)
    avg_speeds.append(float(distance) / trip_time)

df = pd.DataFrame(arrival_times, columns=['arrival_times'])
print(df.describe())

df = pd.DataFrame(avg_speeds, columns=['avg_speeds'])
print(df.describe())
