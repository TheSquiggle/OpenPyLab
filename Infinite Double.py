#THIS SCRIPT PRODUCES VISUALS THAT MAY DISTURB EPILEPTIC VIEWERS!!! VIEW AT YOUR OWN RISK!!!
#THIS SCRIPT AND IT'S CREATOR IS NOT RESPONSIBLE FOR ANYTHING THAT HAPPENS TO YOU!!!
import sys # for maximizing output size
import time # for adding a delay between prints, because APPERENTLY there is no wait command in Python, so I have to imprt the time module for 1 line of code.
import random # for generating random numbers
sys.set_int_max_str_digits(999999999) # this is to max out the output size, so I can print a lot of numbers without hitting the limit.
doubled = 1 # sets the initial value of doubled to 1
step = 0 # initializes the step counter

while True: # basically infinite loop
    doubled = doubled * 2 # doubles itself
    print(f"\033[{color_code}m{doubled}\033[0m") # prints doubled in a color based on its value
    color_code = random.randint (1, 100)  # random color code between 1 and 100
    step = step + 1 # increments the step counter
    time.sleep(1/step) # delay, gets faster each time