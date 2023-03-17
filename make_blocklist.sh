#!/bin/bash

cat blocklists/worldcities.csv | \
    awk -F, '{ print $1 }' | \
    tr -d '"' | \
    awk 'length($0) >= 4 && length($0) <= 7' | \
    sort | uniq > blocklists/worldcities.txt

