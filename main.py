from debounce import debounceDec
from gpiozero import LED, OutputDevice
from beacontools import BeaconScanner,  IBeaconAdvertisement
from beacontools.scanner import  HCIVersion
from dotenv import load_dotenv
from time import  sleep
import os
load_dotenv() 

led = LED(14)
RELAY_PIN = 2
#relay = OutputDevice(RELAY_PIN, active_high=True, initial_value=False)
#relay.on()
#relay.off()
class iBeacon :
    def __init__(self, uuid , lastReadDate ):
        self._uuid = uuid
        self._lastReadDate = lastReadDate
    def uuid(self):
        return self._uuid 


led.on()
var = True
def distancec(rssi) :  
  return round(10**((-69-(rssi)) / (10 * 2)), 2)

@debounceDec(10)
def timeoutBle(*args, **kwargs):
    print('timeoutBle',args,kwargs)
    if led.is_active:
        scanner.stop()
        led.off()

def verifyBle(bt_addr, rssi, packet, additional_info):
    distance =distancec(rssi)
    isble =  os.getenv("MAC") == bt_addr
    isLongDistance = distance > 1
    if(isble ):#and not isLongDistance):
        timeoutBle(bt_addr, rssi, packet= packet, additional_info=additional_info)
    print("<%s, %d, %s> " % (bt_addr, rssi,distance))
    #print("<%s, %d, %s> %s %s" % (bt_addr, rssi,distance(rssi), packet, additional_info))

scanner = BeaconScanner(verifyBle,
    packet_filter=IBeaconAdvertisement #scan_parameters={"interval_ms":200,"window_ms":100}
)
scanner._mon.get_hci_version= lambda: HCIVersion.BT_CORE_SPEC_4_2


scanner.start()