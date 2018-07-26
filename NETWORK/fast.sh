#!/bin/bash   

for ip in $(seq 0 255); do
nc -zv -w 1 192.168.2.$ip 8080 2>&1 | grep succeeded &
done

