#! /bin/bash

x=0
while true
do
	x=$((++x))
	echo "﷽" > $1$x
done
