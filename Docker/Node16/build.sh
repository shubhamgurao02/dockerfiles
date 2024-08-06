#!/bin/bash
echo $@
if [ "$1" == "build" ]
then
            whoami
                        node -v
                        cd /extra/$2
                        npm install 
                        npm run build 
                       returnCode=$?
                else
                            returnCode=999
                                    echo "Unsupported command passed: $1 (instead pass one of these commands as first argument: playbook)"
fi

echo "Return code is: \""$returnCode"\""

if [ $returnCode -ne 0 ];then

            exit 1;
    else

                exit 0;
fi
