#!/bin/python3

import sys
import socket
from datetime import datetime

# Define the target

if len(sys.argv) == 2:
    target = socket.gethostname(sys.argv[1])
else:
    print("Invalid amount of arguments.")
    print("Syntax: Python3 scanner.py <ip>")


# Add a pretty banner

print("-" * 50)
print(f"Scanning target " + target)
print("Time started: ")
