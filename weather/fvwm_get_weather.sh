#!/bin/bash 

cd $HOME/.fvwm/weather

#/usr/bin/wget -q -O -  http://rss.theweathernetwork.com/weather/caon0523 | dos2unix|  sed -n '/<item>/,/<\/item>/p' | ./parser.pl | sed -f ./fvwm_weather_icons.sed > WeatherMenu
/usr/bin/wget -q -O -  http://rss.theweathernetwork.com/weather/caon0523 | dos2unix|  sed -n '/<item>/,/<\/item>/p' | ./parser.pl | sed -f ./fvwm_weather_icons.sed 

