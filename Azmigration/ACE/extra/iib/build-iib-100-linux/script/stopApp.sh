#!/bin/bash -x

echo mqsistopmsgflow $*

# Prepare the parameters

# The application to stop
export IIB_APP=$1

# Local IIB_BROKER
export IIB_BROKER=$2

# IIB execution group
export IIB_EXEC_GRP=$3

# The home for the IIB binaries
export IIB_BIN=$4

# The PBC root
export PBC_ROOT=$5

# Remote broker host
export IIB_REMOTEBROKER_HOST=$6

# Remove broker port
export IIB_REMOTEBROKER_PORT=$7

# Remove broker file
export IIB_BROKER_FILE=$8

echo This script is copyright of Prolifics 2018. All rights reserved. You are not permitted to make copy, modify, or redistribute it.
echo Stop Application
echo --------------------------------------------------
echo IIB app=$IIB_APP
echo IIB remote broker host name=$IIB_REMOTEBROKER_HOST
echo IIB broker file=$IIB_BROKER_FILE
echo IIB remote broker port=$IIB_REMOTEBROKER_PORT
echo IIB execution group=$IIB_EXEC_GRP
echo IIB binaries=$IIB_BIN
echo PBC root=$PBC_ROOT
echo ---------------------------------------------------

# Set the MQSI profile
. $IIB_BIN/mqsiprofile

[ -f /opt/IBM/StandardsProcessingEngine9.0.0/speiib_900.sh ] || /opt/IBM/StandardsProcessingEngine9.0.0/speiib_900.sh

if [ -z $IIB_BROKER ]
then
	echo "$IIB_BIN/mqsistopmsgflow -n $IIB_BROKER_FILE -e $IIB_EXEC_GRP -k $IIB_APP"
	$IIB_BIN/mqsistopmsgflow -n $IIB_BROKER_FILE -e $IIB_EXEC_GRP -k $IIB_APP
else
	echo "$IIB_BIN/mqsistopmsgflow $IIB_BROKER -e $IIB_EXEC_GRP -k $IIB_APP"
    $IIB_BIN/mqsistopmsgflow $IIB_BROKER -e $IIB_EXEC_GRP -k $IIB_APP
fi
