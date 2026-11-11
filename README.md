# autobright

A python tool to automate screen brightness and keyboard backlight according to environmental brightness

## Architecture
**Implementation:**

A python script designed to be invoked as a shell command. The script will perform screen/keyboard brightness adjustment once when invoked. Ambient brightness is estimated via the installed webcam via OpenCV. The brightness of the display and keybaord are adjusted by writing files in `/sys/class/backlight/` and `/sys/class/firmeare-attributes/`. The script will be configured to run periodically via a systemd unit.


**Why Not Dbus?**

I initially tried to implement as a Dbus service. This failed as the keyboard backlight is not exposed by DBus. My next plan was to trigger autobrightness and control display backlight with Dbus and control keyboard backlight with filesystem writes. This failed as writing to the filesystem requires root privilige, while also needing to be executed by the user in order to view the user Dbus session.

