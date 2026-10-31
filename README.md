# autobright

A python tool to automate screen brightness and keyboard backlight according to environmental brightness

## Architecture
**Implementation:**

A python script designed to be invoked as a shell command. The script will perform screen/keyboard brightness adjustment once when invoked. The script will be configured to run periodically via a cron job.

**Script:**

- Use OpenCV library to capture an image with the built-in webcam.
- Use thresholds to assess environmental brightness.
- Write new screen brightness values to `/sys/class/backlight/` and keyboard brightness values to `/sys/class/leds/`
