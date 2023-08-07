# TODO Make this the demo script.
from PyTran import English
from PyTran import Start
from sys import argv


# Checking to see if there's a arg that the user made.
try:
    # Checking the user Args
    if argv[1].lower() == str("--demo"):
        print("Demo")
    elif argv[1].lower() == str("--help"):
        print("Help")
except:
    # No Args Made
    print("No Args")
