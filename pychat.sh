#!/bin/bash

clear

figlet pychat
echo "Programmed by Anonycodexia"
echo ""
sleep 1
echo "What would you like to be ?"
echo ""
echo "1=> SERVER"
echo "2=> CLIENT"
echo ""
echo "Enter your choice number..."
read like

if [ $like == "1" ];
then

kill -9 $(ps -A | grep python | awk '{print $1}')

python server.py
fi
if [ $like == "2" ];
then
python client.py
fi
