# When open file we create an object in RAM
# Open opens a file and creates object in memory - needs an argument
myfile = open('./text/fruits.txt')

# To read the file need to specify
print(myfile.read())

# At this point the cursor is now at the end of the file
# So these lines won't print anything
print(myfile.read())
print(myfile.read())

print('Line 13')

myfile.close() # not mandatory but good practice

# To print many times save content as variable
samefile = open("./text/fruits.txt")
content = samefile.read()
samefile.close # close at this point after have content

print(content)
print(content)

# Files remain open in memory until program execution ends

# These will not work now - get error as closed files
myfile.read()
samefile.read()