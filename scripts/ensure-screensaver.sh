#!/bin/bash

pid=$(pidof xscreensaver)
if [ -z $pid ]
then 
	# start the applet
	exec xscreensaver -no-splash &
fi


