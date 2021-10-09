from debounce import debounceDec
from dotenv import load_dotenv
import time
import os
load_dotenv() 


def distancec(rssi) :  
  return round(10**((-69-(rssi)) / (10 * 2)), 2)

@debounceDec(10)
def timeoutBle(*args, **kwargs):
    print('timeoutBle',args,kwargs)
    if timeoutBle._led.is_active:
        #relay.off()
        timeoutBle._led.off()
        timeoutBle._scanner.stop()

def verifyBle(bt_addr, rssi, packet, additional_info):
    start = time.time()
    distance =distancec(rssi)
    isble =  os.getenv("MAC") == bt_addr
    isLongDistance = distance > 1
    if(isble ):#and not isLongDistance):
        timeoutBle(bt_addr, rssi, packet= packet, additional_info=additional_info)
    print("<%s, %d, %s> " % (bt_addr, rssi,distance))
    #print("<%s, %d, %s> %s %s" % (bt_addr, rssi,distance(rssi), packet, additional_info))
    print("Time Consumed")
    print("% s seconds" % (time.time() - start))