import asyncio
from bleak import BleakScanner
import os
import rx 
from rx import create
import datetime
import json
beacon=create()

beacon.subscribe(
    on_next = lambda i: print("Received {0}".format(i)),
    on_error = lambda e: print("Error Occurred: {0}".format(e)),
    on_completed = lambda: print("Done!"),
)
class iBeacon :
    def __init__(self, uuid , lastReadDate ):
        self._uuid = uuid
        self._lastReadDate = lastReadDate
    def uuid(self):
        return self._uuid 



def distance(rssi): 
   return round(10**(-69-(rssi)) / (10 * 2), 2)
#
#def changeToSleepMode():
#
#def changeToNormalMode():


def notifyStop():
    print('notifyActions')

def startStop():
    print('startStop')
    notifyStop()


def verifyBle():
    print('verifyBel')
    beacon
    mustStop = True
    if mustStop:
        startStop()

async def run():
    devices = await BleakScanner.discover()
    for d in devices:
        json.dump(d)
        if True:
            beacon.next(iBeacon(d.rssi,datetime.datetime.now()))
        rx.timer(
        5.0,
        1000).subscribe(lambda _: verifyBle())
    



loop = asyncio.get_event_loop()
loop.run_until_complete(run())