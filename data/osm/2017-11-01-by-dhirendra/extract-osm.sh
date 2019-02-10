#!/usr/bin/env bash

#
# Example script for extracting rectangular bounds from Australia OSM
# Author: dsingh
#


#DIR=`dirname "$0"`
#cd $DIR

# download the latest OSM extract for Australia from:
# http://download.gisgraphy.com/openstreetmap/pbf/AU.tar.bz2

PBF_ARCHIVE=AU.tar.bz2
printf "\nDownloading the latest OSM extract for Australia...\n\n"
wget -c -N http://download.gisgraphy.com/openstreetmap/pbf/$PBF_ARCHIVE


printf "\nExtracting PBF from archive...\n\n"
tar -jxvf tmp.tar.bz2

# Mount Alexander Shire bounding box
top=-37.81393
left=144.94140
bottom=-37.82480
right=144.96511

printf "\nExtracting Mount Alexander Shire region (bounding box [$top,$right $bottom,$left]) ... \n\n"
osmosis  --read-pbf file=AU  \
    --bounding-box top=$top left=$left bottom=$bottom right=$right \
    --write-xml file=- | bzip2 > mount-alexander-shire.osm.bz2

#osmosis --read-xml city.osm --tf accept-ways highway=* --used-node --write-xml highways.osm

printf "\nExtracting Mount Alexander Shire roads ... \n\n"
bzcat mount-alexander-shire.osm.bz2 | osmosis  --read-xml enableDateParsing=no file=- --tf accept-ways highway=* --used-node --write-xml file=- | bzip2 > mount-alexander-shire-roads.osm.bz2


#cd -
