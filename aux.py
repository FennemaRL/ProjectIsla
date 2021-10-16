from debounce import debounceDec, t_pool
from dotenv import load_dotenv
import time
import os
load_dotenv()

def isBle(device) :
    return getattr(device, os.getenv('MATCH00')) == os.getenv('MATCH0') and any (x == os.getenv('MATCH1') for x in  device.metadata.get(os.getenv('MATCH2')))

def distancec(rssi) :  
  return round(10**((-69-(rssi)) / (10 * 2)), 2)

@debounceDec(int(os.getenv('DTIME')))
def timeoutBle(*args, **kwargs):
    if timeoutBle._led.is_active:
        timeoutBle._relay.on()
        timeoutBle._led.off()
        timeoutBle._canFollow=False
        print('timeoutBle')
        
def verifyBle(device):
    distance =distancec(device.rssi)
    if(isBle(device) and  distance ):#and not isLongDistance):
        timeoutBle(device)
    print("<%s, %d, %s> " % (device, device.rssi,distance))


