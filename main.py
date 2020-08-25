from subprocess import Popen
import sys

filename = "~/auto-interact/instagram.py"
while True:
        print("\nStarting " + filename)
        p = Popen("python3 " + filename, shell=True)
        p.wait()
