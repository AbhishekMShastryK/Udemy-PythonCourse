import time
from datetime import datetime as dt

host_path = r"C:\Windows\System32\drivers\etc\hosts" #'r' to consider path as a row.

redirect="127.0.0.1" #To redirect to this IP address in working hours.
website_list=["www.facebook.com","facebook.com","www.instagram.com","instagram.com"]
#List of website to be blocked in working hours.

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,
    dt.now().month,dt.now().day,17):
    #Check if current time is between 8:00 to 16:00 hours.
        print("Working hours...")
        with open(host_path,'r+') as file: #'r+' is used to read as well as to write.
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect +" "+ website +"\n")
    else:
        with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)