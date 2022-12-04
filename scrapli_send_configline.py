"""
Simple scrapli script using Cisco sandbox device
sending configuration change (this example creating,
ospf area and adding it to area 0)
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
    response = conn.send_configs(
        ["router ospf 40", 
        "network 40.40.40.40 0.0.0.0 area 40",
        ]) #using scrapli send_configs to send configuration lines to the host

print(response.result) #printing the response results to screen
