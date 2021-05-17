#!/bin/sh
cd /
touch /dev/.coldboot_done
export LD_LIBRARY_PATH=/usr/libexec/droid-hybris/system/lib64/:/vendor/lib64:/system/lib64

# Save systemd notify socket name to let droid-init-done.sh pick it up later
echo $NOTIFY_SOCKET > /run/droid-hal/notify-socket-name

/sbin/droid-hal-init

