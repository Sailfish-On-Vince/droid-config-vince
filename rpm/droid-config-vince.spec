# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc
%define device vince
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Redmi 5 Plus
%define dcd_path ./
# Adjust this for your device
%define pixel_ratio 1.5
# We assume most devices will
%define have_modem 1

# Device-specific usb-moded configuration
Provides: usb-moded-configs

# Device-specific ofono configuration
Provides: ofono-configs
Obsoletes: ofono-configs-mer
Obsoletes: bluez5-configs-mer
Conflicts: bluez5-configs-mer

Obsoletes: qt5-qpa-surfaceflinger-plugin

# Community HW adaptations need this
%define community_adaptation 1

# OTA via self-hosted repo needs to have all adaptation-community repos removed
Conflicts: community-adaptation-testing
Obsoletes: community-adaptation-testing

# For bluez5
%define ofono_enable_plugins bluez5,hfp_ag_bluez5
%define ofono_disable_plugins bluez4,dun_gw_bluez4,hfp_ag_bluez4,hfp_bluez4,dun_gw_bluez5,hfp_bluez5

Obsoletes: audioflingerglue
Obsoletes: pulseaudio-modules-droid-glue
Requires: pulseaudio-modules-droid >= 14.2.89
Requires: ohm-plugin-accessories >= 1.7.0

%include droid-configs-device/droid-configs.inc
%include patterns/patterns-sailfish-device-adaptation-vince.inc
%include patterns/patterns-sailfish-device-configuration-vince.inc
