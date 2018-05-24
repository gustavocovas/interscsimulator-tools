import sys
import pandas as pd
import xml.etree.ElementTree as ET

filename = sys.argv[1]

tree = ET.parse(filename)
root = tree.getroot()

arrival_times = []
for child in root:
  if child.attrib['type'] == 'arrival':
    arrival_times.append(int(child.attrib['trip_time']))

df = pd.DataFrame(arrival_times, columns=['arrival_times'])
print(df.describe())