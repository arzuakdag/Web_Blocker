"""Code for scheduled access to specific sites"""

import time 
from datetime import datetime as dt 

# Hosts file need admin rights for modifying. Create temporary hosts file for modifications, testing, and backup. 
hosts_temp = r"C:\Users\strea\OneDrive\Desktop\hosts_tmp"

# Path to host file. 
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

# List of domains to block access to 
website_list = ["www.facebook.com","facebook.com"]

# Conditionals to determine applicable time frames, time intervals, and message informing of current time frame segment 
while True: 
    # Add time frame to determine when domain names are added to hosts file for blocking 
    if dt(dt.now().year, dt.now().month, dt.now().day,10) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):    
        print("Working hours...")
        with open(hosts_path, 'r+') as file: 
            content = file.read()
            for website in website_list: 
                if website in content: 
                    pass
                else:
                    # Add space between IP address and redirect website per hosts file instructions. 
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            """When applying read method the pointer goes to last bit of line. If append it would continue at that point. 
            By seek method pointer gets reapplied to beginning of code/file"""
            file.seek(0)
            """Start iterating through hosts content list and create new hosts file line by line by appending - do not 
            append for items that are part of the domain list."""
            for line in content: 
                if not any(website in line for website in website_list): 
                    file.write(line)
            # Apply truncation to delete superfluous additions and maintain one block of updated code on top of old code. 
            file.truncate()
        print("Fun hours...")
    time.sleep(5)

"""To run this program in the background: change file ext to .pyw enabling pythonw.exe which is specific program for running
Python programs in the backgroud. Lastly, use Taskscheduler to launch program as soon as machine starts - by creating 
Task and 'Run with highest privileges'. Select trigger to be at startup."""
