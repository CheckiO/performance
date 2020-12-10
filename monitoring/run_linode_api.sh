#!/bin/bash

while true; do
  python3 run.py http://linode.checkio-service.info/api/current-user/?format=json results.api.txt
  sleep 1;
done