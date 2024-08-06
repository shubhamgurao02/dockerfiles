#!/bin/bash


echo $@


if [ "$1" == "build" ]
then
    whoami
    mvn --version
    cd /extra/$2
    mvn clean package
    returnCode=$?
elif [ "$1" == "buildandtest" ]
then
    whoami
    mvn --version
    cd /extra/$2
    mvn clean package
    if [ "$?" == "0" ]
    then
        mvn sonar:sonar -Dsonar.host.url=$3 -Dsonar.login=$4 -Dsonar.password=$5
    fi
elif [ "$1" == "test" ]
then
    cd /extra/$2
    mvn sonar:sonar -Dsonar.host.url=$3 -Dsonar.login=$4 -Dsonar.password=$5
    returnCode=$?
else
    returnCode=999
    echo "Unsupported command passed: $1 (instead pass one of these commands as first argument: script)"
    
fi

echo "Return code is: \""$returnCode"\""

if [ $returnCode -ne 0 ];then
    
    exit 1;
else
    
    exit 0;
fi

 #podman run  -v `pwd`:/extra 58b3ff03742c buildtest . http://10.11.12.149:9000/projects admin admin123