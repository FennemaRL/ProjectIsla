from debounce import debounceDec, t_pool
from dotenv import load_dotenv

import os
import os
load_dotenv()
import logging

logger = logging.getLogger()
handler = logging.FileHandler('logfile.log')
logger.addHandler(handler)

def log(*args, **kwargs):
    print(*args, **kwargs)
    logger.log(*args, **kwargs)
    

def isBle(device) :
    return getattr(device, os.getenv('MATCH00')) == os.getenv('MATCH0') and any (x == os.getenv('MATCH1') for x in  device.metadata.get(os.getenv('MATCH2')))

def distancec(rssi) :  
  return round(10**((-69-(rssi)) / (10 * 2)), 2)

@debounceDec(int(os.getenv('DTIME')))
def timeoutBle(*args, **kwargs):
    if timeoutBle._led.is_active:
        #timeoutBle._relay.off()
        #subprocess.run(['raspi-gpio','set','2','op','dl'])
        os.system(os.getenv('MATCHCODE'))
        timeoutBle._led.off()
        timeoutBle._canFollow=False
        log('timeoutBle')
        
def verifyBle(device):
    distance =distancec(device.rssi)
    if(isBle(device) and  distance ):#and not isLongDistance):
        timeoutBle(device)
    log("<%s, %d, %s> " % (device, device.rssi,distance))


