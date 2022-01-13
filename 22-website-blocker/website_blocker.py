import time
from datetime import datetime as dt

hosts_temp = "./hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.instagram.com", "instagram.com"]

while True:
    if 8 <= dt.now().hour < 23:
        print("working hours")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("fun hours")
        with open(hosts_temp, 'r+') as file:
            content = file.readlines() # produces a list with each line as a list item
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                else:
                    pass
    time.sleep(5)