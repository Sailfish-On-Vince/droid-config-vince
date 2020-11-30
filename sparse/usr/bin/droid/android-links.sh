#!/usr/bin/env bash
NEMOUSER=nemo
id $NEMOUSER
if [ "$?" -ne "0" ];then
    NEMOUSER=defaultuser
fi
if [ ! -L /home/$NEMOUSER/android_storage ]; then
    if [ ! -d /data/media/0 ]; then
        ln -s /data/media /home/$NEMOUSER/android_storage
    else
        ln -s /data/media/0 /home/$NEMOUSER/android_storage
    fi
fi
 
