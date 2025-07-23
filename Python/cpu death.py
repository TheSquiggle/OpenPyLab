# WARNING
# YOUR CPU WILL BE STRESSED TO THE MAX!!!
# THIS SCRIPT IS NOT RESPONSIBLE FOR ANY DAMAGE TO YOUR SYSTEM!!!

import subprocess
import os

folder = os.path.dirname(__file__)

while True:
    for filename in os.listdir(folder):
        if filename.endswith(".py") and filename != os.path.basename(__file__):
            subprocess.Popen(
                ["start", "python", os.path.join(folder, filename)],
                shell=True
            )  # Opens each script in a new command prompt window