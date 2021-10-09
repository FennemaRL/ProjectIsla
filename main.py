from aux import timeoutBle, verifyBle
from gpiozero import LED, OutputDevice
from beacontools import BeaconScanner,  IBeaconAdvertisement
from beacontools.scanner import  HCIVersion
from dotenv import load_dotenv
load_dotenv() 

relay = OutputDevice(2, active_high=True, initial_value=False)
led = LED(14)

scanner = BeaconScanner(verifyBle,
    #packet_filter=IBeaconAdvertisement #scan_parameters={"interval_ms":200,"window_ms":100}
)
scanner._mon.get_hci_version= lambda: HCIVersion.BT_CORE_SPEC_5_2
timeoutBle._scanner = scanner
timeoutBle._led =led
timeoutBle._relay =relay

led.on()
relay.on()
timeoutBle()
scanner.start()