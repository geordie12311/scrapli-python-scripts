"""
Simple scrapli script using Cisco sandbox device
sending configuration from a file located in the 
same directory
"""

from scrapli.driver.core import IOSXEDriver #importing IOSXEDriver from scrapli

my_device = {
    "host": "sandbox-iosxe-latest-1.cisco.com",
    "auth_username": "developer",
    "auth_password": "C1sco12345",
    "auth_strict_key": False,
}
# above, creating an object called my_device to hold the hostname and credentials that scrapli will use to connect

with IOSXEDriver(**my_device) as conn: # creating an object called conn, linking to IOSXEDriver and using my_device creds
    response = conn.send_configs_from_file("configtest.txt") #using scrapli send_configs_from_file to send configuration from a file in local directory

print(response.result) #printing the response results to screen