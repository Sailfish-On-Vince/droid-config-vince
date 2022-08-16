#!/bin/bash
echo "droid-get-bt-address: Setting up bluetooth address"
if [ ! -f /var/lib/bluetooth/board-address ];then
  bt_mac=$(cat /data/misc/bluedroid/bt_config.conf|grep Address|awk '{print $NF}')
  echo $bt_mac > /var/lib/bluetooth/board-address
fi
