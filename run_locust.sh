#!/bin/bash
TIMESTAMP=$(date +"%Y%m%d%H%M%S")
OUTPUT_FOLDER="load_test/locust_results/output_$TIMESTAMP"
mkdir -p "$OUTPUT_FOLDER"
locust -f load_test/locustfile.py --host=https://harmonyharbor.azurewebsites.net --headless -u 500 -r 20 -t 15m --csv="$OUTPUT_FOLDER"
