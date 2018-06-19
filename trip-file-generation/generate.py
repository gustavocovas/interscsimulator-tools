import numpy as np

def generate_trips_uniform(name, origin, destination, link_origin, cars_per_trip, time_span_seconds, time_offset_seconds, cars_per_hour):
  total_trips = int((time_span_seconds / 3600) * cars_per_hour)
  start_times = np.sort(np.random.randint(time_span_seconds, size=total_trips))

  return _generate_trips(start_times, name, origin, destination, link_origin, cars_per_trip, time_offset_seconds, 'car_following')
  

def generate_trips_convoy(name, origin, destination, link_origin, cars_per_trip, time_span_seconds, time_offset_seconds, cars_per_hour):
  if cars_per_trip == 0:
    return []
  
  total_trips = int((time_span_seconds / 3600) * cars_per_hour / cars_per_trip)
  start_times = list(range(0, total_trips * 120, 120))

  return _generate_trips(start_times, name, origin, destination, link_origin, cars_per_trip, time_offset_seconds, 'freespeed')


def _generate_trips(start_times, name, origin, destination, link_origin, cars_per_trip, time_offset_seconds, traffic_model):
  generated = 0
  trips = []

  for start_time in start_times:
    trip = (name + str(generated), origin, destination, link_origin, cars_per_trip, time_offset_seconds + start_time, 'car', traffic_model)
    trips.append(trip)

    generated += 1

  return trips


def trip_to_xml(trip):
  return '<trip name="{}" origin="{}" destination="{}" link_origin="{}" count="{}" start="{}" mode="{}" traffic_model="{}"/>'.format(*trip)

print("<scsimulator_matrix>")

dr_ratio = 1

regular_trips = 1980 * (1-dr_ratio)
dr_trips = 1980 * dr_ratio

paraiso_regular_trips = generate_trips_uniform(
  name='paraiso_regular_', origin='1952545091', destination='60609874', link_origin='872', 
  cars_per_trip=1, time_span_seconds=3600, time_offset_seconds=112, cars_per_hour=regular_trips
)
for trip_xml in map(trip_to_xml, paraiso_regular_trips):
  print(trip_xml)  

paraiso_dr_trips = generate_trips_convoy(
  name='paraiso_dr_', origin='1952545091', destination='60609874', link_origin='872', 
  cars_per_trip=int(dr_trips/(3600/120)), time_span_seconds=3600, time_offset_seconds=112, cars_per_hour=dr_trips
)
for trip_xml in map(trip_to_xml, paraiso_dr_trips):
  print(trip_xml)  

consolacao_regular_trips = generate_trips_uniform(
  name='consolacao_regular', origin='60609819', destination='1421376041', link_origin='1425', 
  cars_per_trip=1, time_span_seconds=3600, time_offset_seconds=115, cars_per_hour=regular_trips
)
for trip_xml in map(trip_to_xml, consolacao_regular_trips):
  print(trip_xml)  

consolacao_dr_trips = generate_trips_convoy(
  name='consolacao_dr_', origin='60609819', destination='1421376041', link_origin='1425', 
  cars_per_trip=int(dr_trips/(3600/120)), time_span_seconds=3600, time_offset_seconds=115, cars_per_hour=dr_trips
)
for trip_xml in map(trip_to_xml, consolacao_dr_trips):
  print(trip_xml)  

print("</scsimulator_matrix>")