import sys

import numpy as np

cycle = 90

def generate_trips_uniform(name, origin, destination, link_origin, cars_per_trip, time_span_seconds, time_offset_seconds, cars_per_hour):
  total_trips = int((time_span_seconds / 3600) * cars_per_hour)
  start_times = np.sort(np.random.randint(time_span_seconds, size=total_trips))

  return _generate_trips(start_times, name, origin, destination, link_origin, cars_per_trip, time_offset_seconds, 'car_following')
  

def generate_trips_convoy(name, origin, destination, link_origin, cars_per_trip, time_span_seconds, time_offset_seconds, cars_per_hour):
  if cars_per_trip == 0:
    return []
  
  total_trips = int((time_span_seconds / 3600) * cars_per_hour / cars_per_trip)
  start_times = list(range(0, total_trips * cycle, cycle))

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

dr_ratio = float(sys.argv[1])

paraiso_regular_cars = 2359 * (1-dr_ratio)
paraiso_dr_cars = 2359 * dr_ratio

consolacao_regular_cars = 3067 * (1-dr_ratio)
consolacao_dr_cars = 3067 * dr_ratio

paraiso_offset = cycle - 8 + 13  # Cycle time - time to get to first signalized intersection + start time
consolacao_offset = cycle - 5 - 58

paraiso_regular_trips = generate_trips_uniform(
  name='paraiso_regular_', 
  origin='1952545091', 
  destination='60609874', 
  link_origin='872', 
  cars_per_trip=1, 
  time_span_seconds=3600, 
  time_offset_seconds=paraiso_offset, 
  cars_per_hour=paraiso_regular_cars
)
for trip_xml in map(trip_to_xml, paraiso_regular_trips):
  print(trip_xml)  

paraiso_dr_trips = generate_trips_convoy(
  name='paraiso_dr_', 
  origin='1952545091', 
  destination='60609874', 
  link_origin='872', 
  cars_per_trip=int(paraiso_dr_cars/(3600/cycle)), 
  time_span_seconds=3600, 
  time_offset_seconds=paraiso_offset, 
  cars_per_hour=paraiso_dr_cars
)
for trip_xml in map(trip_to_xml, paraiso_dr_trips):
  print(trip_xml)  

consolacao_regular_trips = generate_trips_uniform(
  name='consolacao_regular', 
  origin='60609819', 
  destination='1421376041', 
  link_origin='1425', 
  cars_per_trip=1, 
  time_span_seconds=3600, 
  time_offset_seconds=consolacao_offset, 
  cars_per_hour=consolacao_regular_cars
)
for trip_xml in map(trip_to_xml, consolacao_regular_trips):
  print(trip_xml)  

consolacao_dr_trips = generate_trips_convoy(
  name='consolacao_dr_', 
  origin='60609819', 
  destination='1421376041', 
  link_origin='1425', 
  cars_per_trip=int(consolacao_dr_cars/(3600/cycle)), 
  time_span_seconds=3600, 
  time_offset_seconds=consolacao_offset, 
  cars_per_hour=consolacao_dr_cars
)
for trip_xml in map(trip_to_xml, consolacao_dr_trips):
  print(trip_xml)  

print("</scsimulator_matrix>")