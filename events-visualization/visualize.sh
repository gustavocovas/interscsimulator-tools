#!/bin/bash

events_file=$1
network_file=$2

echo "Events file: "$events_file
echo "Network file: "$network_file
echo "==="

echo "=> Gzipping events..."
gzip --stdout $events_file > $events_file.gz && \
echo "=> ok"

echo "=> Converting events..."
java -cp ../vendor/matsim-0.9.0/matsim-0.9.0.jar:../vendor/otfvis-0.9.0/otfvis-0.9.0.jar \
  org.matsim.contrib.otfvis.RunOTFVis --convert $events_file.gz $network_file $events_file.mvi 1 && \
echo "=> ok. Written events mvi at "$events_file".mvi"

echo "=> Playing movie events..."
java -cp ../vendor/matsim-0.9.0/matsim-0.9.0.jar:../vendor/otfvis-0.9.0/otfvis-0.9.0.jar \
  org.matsim.contrib.otfvis.RunOTFVis $events_file.mvi

