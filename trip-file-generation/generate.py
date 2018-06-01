import numpy as np

def generate_trips_uniform(name, origin, destination, link_origin, cars_per_trip, time_span_seconds, time_offset_seconds, cars_per_hour):
  total_trips = int((time_span_seconds / 3600) * cars_per_hour)
  start_times = np.sort(np.random.randint(time_span_seconds, size=total_trips))

  return _generate_trips(start_times, name, origin, destination, link_origin, cars_per_trip, time_offset_seconds)
  

def generate_trips_convoy(name, origin, destination, link_origin, cars_per_trip, time_span_seconds, time_offset_seconds, cars_per_hour):
  total_trips = int((time_span_seconds / 3600) * cars_per_hour / cars_per_trip)
  start_times = list(range(0, total_trips * 120, 120))

  return _generate_trips(start_times, name, origin, destination, link_origin, cars_per_trip, time_offset_seconds)


def _generate_trips(start_times, name, origin, destination, link_origin, cars_per_trip, time_offset_seconds):
  generated = 0
  trips = []

  for start_time in start_times:
    trip = (name + str(generated), origin, destination, link_origin, cars_per_trip, time_offset_seconds + start_time, 'car')
    trips.append(trip)

    generated += 1

  return trips


def trip_to_xml(trip):
  return '<trip name="{}" origin="{}" destination="{}" link_origin="{}" count="{}" start="{}" mode="{}"/>'.format(*trip)

print("<scsimulator_matrix>")

paraiso_trips = generate_trips_uniform(
  name='paraiso', 
  origin='1952545091', 
  destination='60609874', 
  link_origin='872', 
  cars_per_trip=1, 
  time_span_seconds=(3 * 3600), 
  time_offset_seconds=112,
  cars_per_hour=2100
)
for trip_xml in map(trip_to_xml, paraiso_trips):
  print(trip_xml)  

consolacao_trips = generate_trips_uniform(
  name='consolacao', 
  origin='60609819', 
  destination='1421376041', 
  link_origin='1425', 
  cars_per_trip=1, 
  time_span_seconds=(3 * 3600), 
  time_offset_seconds=115,
  cars_per_hour=2100
)
for trip_xml in map(trip_to_xml, consolacao_trips):
  print(trip_xml)  

print("</scsimulator_matrix>")