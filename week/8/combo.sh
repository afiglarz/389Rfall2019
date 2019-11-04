#!/bin/bash

gnome-terminal -x bash -c "./pass_run; exec bash" &
nc ec2-18-222-89-163.us-east-2.compute.amazonaws.com 1337 

