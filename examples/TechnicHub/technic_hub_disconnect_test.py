from hub2hub import TechnicHub, ble_handler
from time import sleep_ms

# Initialize ble handler and a technic hub
ble = ble_handler()
Thub = TechnicHub(ble)

# connect to a technic hub: press green button on the technic hub
Thub.connect()

Thub.led(8)

sleep_ms(2000)

Thub.disconnect()

sleep_ms(10000)

Thub.connect()
    
    
