# autobright

A python tool to automate screen brightness and keyboard backlight according to environmental brightness

## Architecture
**Implementation:**

A python script designed to be invoked as a shell command. The script will perform screen/keyboard brightness adjustment once when invoked. The script will be configured to run periodically via a systemd unit.


**Script:**

- Use OpenCV library to capture an image with the built-in webcam.
- Use thresholds to assess environmental brightness level.
- Use dbus to set new keyboard/display brightness values.
    - Optional functionality: Write new screen brightness values to `/sys/class/backlight/` and keyboard brightness values to `/sys/class/leds/
    
**Functionality:**
- A systemd unit that will start a python service for the application on startup after graphical target.
- Python service will use dbus to perform automatic brightness changes on session login/unlock.
    - Use opencv to pull a reference image frame from webcam
    - Estimate brightness based on average pixel brightness
    - Use thresholds to translate brightness to screen/keyboard light levels.
    - Set new brightness values via dbus or filesystem.

