#THIS SCRIPT PRODUCES VISUALS THAT MAY DISTURB EPILEPTIC VIEWERS!!! VIEW AT YOUR OWN RISK!!!
#THIS SCRIPT AND IT'S CREATOR IS NOT RESPONSIBLE FOR ANYTHING THAT HAPPENS TO YOU!!!
import sys
import time
import colorsys  # for HSV to RGB conversion

sys.set_int_max_str_digits(999999999)
sub = 1
step = 0
hue = 0.0  # start hue

while True:
    # Convert hue to RGB (values 0-255)
    r, g, b = [int(x * 255) for x in colorsys.hsv_to_rgb(hue, 1, 1)]
    print(f"\033[38;2;{r};{g};{b}m{sub}\033[0m")
    sub -= 1  # subtract 1
    hue += 0.01  # increase hue for next color
    if hue > 1.0:
        hue = 0.0
    step += 0.1
    time.sleep(1/step)