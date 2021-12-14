# Sleep function is not available in the automatically available python code

# Use this syntax to look in built in modules
import sys
sys.builtin_module_names

# Import a module then use dir to work out what have for it
import time
dir(time) # => Has a sleep method

# Use this to look at method
help(time.sleep)