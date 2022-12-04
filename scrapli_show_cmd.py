"""
Simple scrapli script using Cisco sandbox device
"""

from scrapli.driver.core import IOSXEDriver #importing IOSXEDriver from scrapli

my_device = {
    "host": "sandbox-iosxe-latest-1.cisco.com",
    "auth_username": "developer",
    "auth_password": "C1sco12345",
    "auth_strict_key": False,
}
# above, creating an object called my_device to hold the hostname and credentials that scrapli will use to connect

conn = IOSXEDriver(**my_device) # creating an object called conn, linking to IOSXEDriver and using my_device creds
conn.open() #opening the connection to my_device
response = conn.send_command("Show IP interface brief") #creating the object response and using send_command to send command to host

print(response.result) #printing the response results to screen
conn.close() #closing the connection to the host
