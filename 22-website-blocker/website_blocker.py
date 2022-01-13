import time
from datetime import datetime as dt

hosts_temp = "/home/brian/code/courses/python/202110-python-mega-course/22-website-blocker/hosts"
hosts_admin = "/etc/hosts"
hosts_path = hosts_admin

redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.instagram.com", "instagram.com"]

while True:
    if 8 <= dt.now().hour < 21:
        print("working hours")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            file.seek(0, 2) # Moves cursor to very end of file
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("fun hours")
        with open(hosts_path, 'r+') as file:
            content = file.readlines() # produces a list with each line as a list item
            file.seek(0) # moves pointer to the top of the file
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)