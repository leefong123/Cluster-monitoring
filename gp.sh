#!/bin/bash
#
# A simple script to keep running and displaying  the current pods running in default namespace


while true
do
	kubectl get po;
	sleep 1;
done;

