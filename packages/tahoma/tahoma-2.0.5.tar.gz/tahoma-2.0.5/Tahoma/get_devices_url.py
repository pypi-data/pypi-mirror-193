#!/usr/bin/python3
#sudo python3 -m pip install pyoverkiz
#sudo python3 -m pip install tahoma-pzim -U
#tahoma-pzim.py by @pzim-devdata
#MIT Licence
version = 'tahoma-pzim - Version 2.0.5 - by @pzim-devdata'

import asyncio
import sys
import argparse
import os
import re
from getpass import getpass
import time
from pyoverkiz.const import SUPPORTED_SERVERS
from pyoverkiz.client import OverkizClient
from pyoverkiz.enums import OverkizCommand
from pyoverkiz.models import Command

async def getting_info() -> None:
    servers = SUPPORTED_SERVERS["somfy_europe"]

    passwd_file = os.path.dirname(os.path.abspath(__file__))+'/temp/identifier_file.txt'
    list_of_tahoma_devices = os.path.dirname(os.path.abspath(__file__))+'/temp/list_of_tahoma_devices.txt'
    list_of_tahoma_shutters = os.path.dirname(os.path.abspath(__file__))+'/temp/shutters.txt'
    list_of_tahoma_heaters = os.path.dirname(os.path.abspath(__file__))+'/temp/heaters.txt'
    list_of_tahoma_alarms = os.path.dirname(os.path.abspath(__file__))+'/temp/alarms.txt'
    list_of_tahoma_spotalarms = os.path.dirname(os.path.abspath(__file__))+'/temp/spotalarms.txt'
    list_of_tahoma_plugs = os.path.dirname(os.path.abspath(__file__))+'/temp/plugs.txt'



    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username")
    parser.add_argument("-p", "--password")
    parser.add_argument("-g", action='store_true') #store_true for not asking argument
    parser.add_argument("--getlist", action='store_true') #store_true for not asking argument
    args = parser.parse_args()

    try :
        f = open(passwd_file, 'r')
        content = f.read()
        f.close()
        if len(content.splitlines()[0]) > 0 :
            USERNAME = content.splitlines()[0]
        if len(content.splitlines()[1]) > 0 :
            PASSWORD = content.splitlines()[1]
    except: pass

    for arg in sys.argv:
        if args.password:
            PASSWORD = (f'{args.password}')
        if args.username:
            USERNAME = (f'{args.username}')

    f2 = open(list_of_tahoma_devices, 'w')
    f3 = open(list_of_tahoma_shutters, 'w')
    f4 = open(list_of_tahoma_heaters, 'w')
    f5 = open(list_of_tahoma_alarms, 'w')
    f6 = open(list_of_tahoma_spotalarms, 'w')
    f7 = open(list_of_tahoma_plugs, 'w')
    
    async with OverkizClient(USERNAME, PASSWORD, server=servers) as client:
        try:
            await client.login()
        except Exception as exception:  # pylint: disable=broad-except
            print(exception)
            return
        devices = await client.get_devices()
    try :
        for device in devices:
            print(f"\n{device.label},{device.id},{device.widget}")
            f2.write(f"{device.label},{device.id},{device.widget},{device.ui_class},{device.controllable_name}\n")
            if "Shutter" in device.widget or "PositionableTiltedScreen" in device.widget:
                f3.write(device.label+","+device.id+","+device.widget+"\n")
                print( "Device "+device.label+" controled by tahoma. Added to "+list_of_tahoma_shutters)
            elif "Heater" in device.widget :
                f4.write(device.label+","+device.id+","+device.widget+"\n")
                print( "Device "+device.label+" controled by tahoma. Added to "+list_of_tahoma_heaters)
            elif "MyFoxAlarm" in device.widget :
                f5.write(device.label+","+device.id+","+device.widget+"\n")
                print( "Device "+device.label+" controled by tahoma. Added to "+list_of_tahoma_alarms)
            elif "StatefulOnOffLight" in device.widget :
                f6.write(device.label+","+device.id+","+device.widget+"\n")
                print( "Device "+device.label+" controled by tahoma. Added to "+list_of_tahoma_spotalarms)
            elif "StatelessOnOff" in device.widget :
                f7.write(device.label+","+device.id+","+device.widget+"\n")
                print( "Device "+device.label+" controled by tahoma. Added to "+list_of_tahoma_plugs)
            else :
                print( "Device '"+device.label+"' NOT controlled by tahoma yet")
    except Exception as e :
        print(e)
    
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    print( "\nIf you want to add a device you have found in this list but which is not controlled by tahoma yet, please provide info about this device from this file at \nhttps://github.com/pzim-devdata/tahoma/issues and I will update the plugin ;-).")
    print( "\nThe list of devices has been succesfully imported to the file : "+list_of_tahoma_devices+"\n" )

try:
    asyncio.run(getting_info())
except NameError as e:
    print(e)
    print("\nYou didn't specified any USERNAME or PASSWORD.\nExecute tahoma --config or provide a temporary USERNAME and PASSWORD by executing tahoma -u <USERNAME> -p <PASSWORD> command")

