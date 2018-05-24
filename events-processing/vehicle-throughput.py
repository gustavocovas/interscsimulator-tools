import sys
import pandas as pd
import xml.etree.ElementTree as ET

filename = sys.argv[1]
link_id = sys.argv[2]

tree = ET.parse(filename)
root = tree.getroot()

entered_link_times = []

for child in root:
  # Sample event:
  # <event time="2897" type="entered link" person="2_11" link="8" vehicle="2_11" action="ok" />
  if child.attrib['type'] == 'entered link' and child.attrib['link'] == link_id:
    entered_link_times.append(int(child.attrib['time']))

df = pd.DataFrame(entered_link_times, columns=['entered_link_times'])
print(df.describe())

