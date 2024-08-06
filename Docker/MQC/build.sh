#!/bin/bash


echo $@
first_arg=`echo $1`
shift
if [ "$first_arg" == "run" ]
then
            whoami
                cd /extra
                chmod -R 777 *

                python3 $@
                
                chmod -R 777 *
                           returnCode=$?
                else
                            returnCode=999
                                    echo "Unsupported command passed: $1 (instead pass one of these commands as first argument: python script)"
fi

echo "Return code is: \""$returnCode"\""

if [ $returnCode -ne 0 ];then

            exit 1;
    else

                exit 0;
fi
