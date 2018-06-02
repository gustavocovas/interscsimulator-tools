#!/bin/bash

mvi_file=$1

echo "=> Playing movie events..."
java -cp ../vendor/matsim-0.9.0/matsim-0.9.0.jar:../vendor/otfvis-0.9.0/otfvis-0.9.0.jar \
  org.matsim.contrib.otfvis.RunOTFVis $mvi_file
