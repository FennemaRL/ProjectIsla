import time
from aux import timeoutBle, verifyBle
from gpiozero import LED, OutputDevice
from beacontools import BeaconScanner
from beacontools.scanner import  HCIVersion
from dotenv import load_dotenv
from debounce import t_pool
import asyncio
from bleak import BleakScanner
from bleak import BleakScanner
load_dotenv() 

relay = OutputDevice(2, active_high=True, initial_value=False)
led = LED(14)

scanner = BeaconScanner(verifyBle,
    #packet_filter=IBeaconAdvertisement #scan_parameters={"interval_ms":200,"window_ms":100}
)
scanner._mon.get_hci_version= lambda: HCIVersion.BT_CORE_SPEC_5_2


timeoutBle._led =led
timeoutBle._relay =relay
timeoutBle._canFollow=True
led.on()
relay.on()
timeoutBle()


async def main():

    start0 = time.time()
    while timeoutBle._canFollow:
        start = time.time()
        devices = await BleakScanner.discover(timeout=4)
        for d in devices:
            if timeoutBle._canFollow:
                verifyBle(d)
        print("Time Consumed")
        print("% s seconds" % (time.time() - start))
    t_pool.executor.shutdown()
    asyncio.get_event_loop().stop()
    print("Time Consumed")
    print("% s seconds" % (time.time() - start0))
asyncio.run(main())