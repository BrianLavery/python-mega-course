a = 3

while a > 0:
    print(a)
    a -= 1

username = ''

while len(username) < 6:
    username = input('Enter username: ')

print(username)

# Break statement approach
while True:
    username = input('Enter username: ')
    if len(username) >= 6:
        break