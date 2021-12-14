import time
# os is not among built-in python modules
# os is written in python
# built-in modules are written in C
# to find where os is you write 'sys.prefix' in python3 after imported sys
# /usr for me on linux
# Then from there go to /usr/lib/python3.8 and os.py is a file
# Can use dir(os) to see what have available
# path is on os and then exists is a method on path to check if a file exists
# We use that to modify while loop below
import os

while True:
    if os.path.exists("./files/084-demo.txt"):
        with open("./files/084-demo.txt") as file:
            print(file.read())
    else:
        print('File does not exist')
    time.sleep(10)
