# Everything for file object is a block under statement
# With content manager will automatically close the file
with open('./text/fruits.txt') as myfile:
    content = myfile.read()

print(content)