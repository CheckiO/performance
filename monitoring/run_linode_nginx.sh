#!/bin/bash

while true; do
  python3 run.py http://linode.checkio-service.info/robots.html results.nginx.txt
  sleep 1;
done