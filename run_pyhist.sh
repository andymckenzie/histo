#!/bin/bash
while IFS= read -r line; do
    stringarray=($line)
    for a in "${stringarray[@]}"; do echo "[$a] +"; done
done < gdc_manifest.2020-12-28_gbm_top_10.txt
