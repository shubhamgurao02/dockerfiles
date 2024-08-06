#!/bin/bash

#Print out arguments

echo $@

#Prepare XVFB to allow running IIT in headless mode

Xvfb :10 -ac -nolisten tcp -nolisten unix &
export DISPLAY=:10

#The following works around the issue where mqsiprofile wont run
export BASH_VERSION=1

#Switch based on command passed, and call ant, passing the appropriate arguments as build properties

if [ "$1" == "build" ]
then
	ant -buildfile /buildconductor/iib/build-iib-100-linux/build.xml assembleApp -Dbars.list="$2" -Dbar.$2.applications.list="$3" -Dbar.$2.deployAsSource="true" -DpipelineEvents.url="" -DbuildLabel="" -DuserId="" -DengineId="" -DpipelineEvents.application="" -DBUILD_HOME="/builds" -DBUILD_TOOLS="/buildconductor/iib" -Dpbc.platform="bamboo" -DIIT_BIN="/opt/ibm/ace-12.0.3.0/tools/iibt" -DMQSI_BIN="/opt/ibm/ace-12.0.3.0/server/bin" -DCURL_BIN="/usr/bin/curl"
	antReturnCode=$?
fi

if [ "$1" == "overrideAndDeploy" ]
then

    rm -rf /builds/load/.broker

    echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>
            <IntegrationNodeConnectionParameters Version=\"10.0.0\" host=\"$3\" integrationNodeName=\"$5\" listenerPort=\"$4\" userName=\"$7\" xmlns=\"http://www.ibm.com/xlmns/prod/websphere/iib/8/IntegrationNodeConnectionParameters\"/>" >> /builds/load/.broker

    BROKER_FILE="/builds/load/.broker"

    cat /builds/load/.broker

    ant -buildfile /buildconductor/iib/build-iib-100-linux/build.xml overrideAndDeployApp -Dbars.list="$2" -DIIB_EXEC_GRP="$6" -Dbar.$2.brokerFile="$BROKER_FILE" -Diib.userId="$7" -Diib.password="$8" -Dbar.$2.applications.list="$9" -Dbar.$2.properties="${10}" -DpipelineEvents.url="" -DbuildLabel="" -DuserId="" -DengineId="" -DpipelineEvents.application="" -DBUILD_HOME="/builds" -DBUILD_TOOLS="/buildconductor/iib" -Dpbc.platform="bamboo" -DIIT_BIN="/opt/ibm/ace-12.0.3.0/tools/iibt" -DMQSI_BIN="/opt/ibm/ace-12.0.3.0/server/bin" -DCURL_BIN="/usr/bin/curl"
	antReturnCode=$?
fi

if [ "$1" == "overrideAndDeployBrokerFile" ]
then

    cp /builds/load/$8 /builds/load/$8.temp

    BROKER_FILE="/builds/load/$8.temp"

    #cat $BROKER_FILE

    #If brokerfile does not have userid and password then add them

    if ! grep -q password= "$BROKER_FILE"; then
        sed -i "s/\/>/ userName=\"$4\" password=\"$5\"\/>/g" $BROKER_FILE
    fi

    #cat $BROKER_FILE

    ant -buildfile /buildconductor/iib/build-iib-100-linux/build.xml overrideAndDeployApp -Dbars.list="$2" -DIIB_EXEC_GRP="$3" -Dbar.$2.brokerFile="$BROKER_FILE" -Diib.userId="$4" -Diib.password="$5" -Dbar.$2.applications.list="$6" -Dbar.$2.properties="$7" -DpipelineEvents.url="" -DbuildLabel="" -DuserId="" -DengineId="" -DpipelineEvents.application="" -DBUILD_HOME="/builds" -DBUILD_TOOLS="/buildconductor/iib" -Dpbc.platform="bamboo" -DIIT_BIN="/opt/ibm/ace-12.0.3.0/tools/iibt" -DMQSI_BIN="/opt/ibm/ace-12.0.3.0/server/bin" -DCURL_BIN="/usr/bin/curl"
	antReturnCode=$?
fi

if [ "$1" == "overrideAndDeployIntegrationServer" ]
then

    rm -rf /builds/load/.broker
    
    echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>
            <IntegrationNodeConnectionParameters Version=\"10.0.0\" host=\"$3\" listenerPort=\"$4\" userName=\"$6\" xmlns=\"http://www.ibm.com/xlmns/prod/websphere/iib/8/IntegrationNodeConnectionParameters\"/>" >> /builds/load/.broker

    BROKER_FILE="/builds/load/.broker"

    cat /builds/load/.broker

    ant -buildfile /buildconductor/iib/build-iib-100-linux/build.xml overrideAndDeployApp -Dbars.list="$2" -DIIB_EXEC_GRP="$5" -Dbar.$2.brokerFile="$BROKER_FILE" -Diib.userId="$6" -Diib.password="$7" -Dbar.$2.applications.list="$8" -Dbar.$2.properties="$9" -DpipelineEvents.url="" -DbuildLabel="" -DuserId="" -DengineId="" -DpipelineEvents.application="" -DBUILD_HOME="/builds" -DBUILD_TOOLS="/buildconductor/iib" -Dpbc.platform="bamboo" -DIIT_BIN="/opt/ibm/ace-12.0.3.0/tools/iibt" -DMQSI_BIN="/opt/ibm/ace-12.0.3.0/server/bin" -DCURL_BIN="/usr/bin/curl"
	antReturnCode=$?
fi

echo "ANT: Return code is: \""$antReturnCode"\""

if [ $antReturnCode -ne 0 ];then

    exit 1;
else

    exit 0;
fi
