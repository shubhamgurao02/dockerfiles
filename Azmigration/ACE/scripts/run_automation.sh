#!/bin/bash
echo $@
Xvfb :10 -ac -nolisten tcp -nolisten unix &
export DISPLAY=:10
export BASH_VERSION=1
if [ "$1" == "build" ]
then
	/opt/ibm/ace-12.0.12.2/ibmint package --input-path $1 --output-bar-file $2 
fi
if [ "$1" == "Buildandoverride" ]
then
    /opt/ibm/ace-12.0.12.2/ibmint package --input-path $1 --output-bar-file $2 
    if [ $? -eq 0 ]
    then
    /opt/ibm/ace-12.0.12.2/ibmint package --input-path $1 --output-bar-file $2 --overrides-file $3
fi
echo "Return code is: \""$?"\""
if [ $? -ne 0 ];then
    exit 1;
else
    exit 0;
fi
