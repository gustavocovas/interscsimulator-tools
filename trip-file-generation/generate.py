import numpy as np

def generate_trips(name, origin, destination, link_origin, cars_per_trip, time_span_seconds, time_offset_seconds, cars_per_hour):
  total_trips = (time_span_seconds / 3600) * cars_per_hour
  generated = 0
  trips = []

  start_times = np.sort(np.random.randint(time_span_seconds, size=total_trips))

  for start_time in start_times:
    trip = (name + str(generated), origin, destination, link_origin, cars_per_trip, time_offset_seconds + start_time, 'car')
    trips.append(trip)

    generated += 1

  return trips

def trip_to_xml(trip):
  return '<trip name="{}" origin="{}" destination="{}" link_origin="{}" count="{}" start="{}" mode="{}"/>'.format(*trip)

print("<scsimulator_matrix>")

paraiso_trips = generate_trips(
  name='paraiso', 
  origin='1952545091', 
  destination='60609874', 
  link_origin='872', 
  cars_per_trip=1, 
  time_span_seconds=(3 * 3600), 
  time_offset_seconds=112,
  cars_per_hour=2500
)
for trip_xml in map(trip_to_xml, paraiso_trips):
  print(trip_xml)  

consolacao_trips = generate_trips(
  name='consolacao', 
  origin='60609819', 
  destination='1421376041', 
  link_origin='1425', 
  cars_per_trip=1, 
  time_span_seconds=(3 * 3600), 
  time_offset_seconds=115,
  cars_per_hour=2500
)
for trip_xml in map(trip_to_xml, consolacao_trips):
  print(trip_xml)  

print("</scsimulator_matrix>")