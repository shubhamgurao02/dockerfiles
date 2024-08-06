#!/bin/bash -x

echo mqsistopmsgflow $*

# Prepare the parameters

# The application containing the msgflow
export IIB_APP=$1

# The msgflow
export IIB_MSG_FLOW=$2

# Local IIB_BROKER
export IIB_BROKER=$3

# IIB execution group
export IIB_EXEC_GRP=$4

# The home for the IIB binaries
export IIB_BIN=$5

# The PBC root
export PBC_ROOT=$6

# Remote broker host
export IIB_REMOTEBROKER_HOST=$7

# Remove broker port
export IIB_REMOTEBROKER_PORT=$8

# Remote broker queue manager
export IIB_REMOTEBROKER_QMGR=$9

shift

# Switch setting
export TRACE_FILE=$9

echo This script is copyright of Prolifics 2014. All rights reserved. You are not permitted to make copy, modify, or redistribute it.
echo Stop Message Flow
echo --------------------------------------------------
echo IIB app=$IIB_APP
echo IIB message flow=$IIB_MSG_FLOW
echo IIB remote broker host name=$IIB_REMOTEBROKER_HOST
echo IIB remote broker port=$IIB_REMOTEBROKER_PORT
echo IIB remote broker queue mgr=$IIB_REMOTEBROKER_QMGR
echo IIB execution group=$IIB_EXEC_GRP
echo IIB binaries=$IIB_BIN
echo PBC root=$PBC_ROOT
echo TRACE_FILE=$TRACE_FILE
echo ---------------------------------------------------

# Set the MQSI profile
. $IIB_BIN/mqsiprofile

[ -f /opt/IBM/StandardsProcessingEngine9.0.0/speiib_900.sh ] || /opt/IBM/StandardsProcessingEngine9.0.0/speiib_900.sh

if [ -z $IIB_BROKER ]
then
	echo "$IIB_BIN/mqsistopmsgflow -i $IIB_REMOTEBROKER_HOST -p $IIB_REMOTEBROKER_PORT -q $IIB_REMOTEBROKER_QMGR -e $IIB_EXEC_GRP -k $IIB_APP -m $IIB_MSG_FLOW -v $TRACE_FILE"
	$IIB_BIN/mqsistopmsgflow -i $IIB_REMOTEBROKER_HOST -p $IIB_REMOTEBROKER_PORT -q $IIB_REMOTEBROKER_QMGR -e $IIB_EXEC_GRP -k $IIB_APP -m $IIB_MSG_FLOW -v $TRACE_FILE
else
	echo "$IIB_BIN/mqsistopmsgflow $IIB_BROKER -e $IIB_EXEC_GRP -k $IIB_APP -m $IIB_MSG_FLOW -v $TRACE_FILE"
    $IIB_BIN/mqsistopmsgflow $IIB_BROKER -e $IIB_EXEC_GRP -k $IIB_APP -m $IIB_MSG_FLOW -v $TRACE_FILE
fi