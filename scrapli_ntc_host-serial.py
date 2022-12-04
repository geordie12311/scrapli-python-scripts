"""
Simple scrapli script to connect to multiple hosts
to pull out the hostname, serial number details using texfm
structured data.
"""
import json
from scrapli.driver.core import IOSXEDriver #importing IOSXEDriver from scrapli

devices = [
    {
        "host": "vIOS1",
        "auth_username": "cisco",
        "auth_password": "cisco123",
        "auth_strict_key": False,
        "ssh_config_file": True,
    },
    {
        "host": "vIOS2",
        "auth_username": "cisco",
        "auth_password": "cisco123",
        "auth_strict_key": False,
        "ssh_config_file": True,
    },
    {
        "host": "vIOS3",
        "auth_username": "cisco",
        "auth_password": "cisco123",
        "auth_strict_key": False,
        "ssh_config_file": True,
    },
]
# above, creating an object called devices to hold the hostnames and credentials that scrapli will use to connect

for device in devices:
    with IOSXEDriver(**device) as conn: #using a for loop with content manager to connect to the hosts
        response = conn.send_command("show version") #creating the object response and using send_command to send command to hosts
        struct_result = response.textfsm_parse_output() #creating an object called struct_result and using texfsm to parse the output into structured data
        for info in struct_result: #creating an object called info to capture output of struct_result
            
            print(f"Device {info['hostname']} has a serial number of {info['serial'][0]}") 
            #using the output from info to pull out the device hostname / serial numbers. Note [0] removes the [' from the output of serial
