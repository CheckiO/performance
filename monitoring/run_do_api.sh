#!/bin/bash

while true; do
  python3 run.py http://blank.checkio-service.info/api/current-user/?format=json results.api.txt
  sleep 1;
done