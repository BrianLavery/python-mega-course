with open("files/vegetables.txt", "a") as file:
    file.write("\nokra")
    # Cannot read in this file

# Can append and read as below
with open("files/vegetables.txt", "a+") as file:
    file.write("\nokra")
    file.seek(0) # moves cursor to beginning of file
    content = file.read()

print(content)