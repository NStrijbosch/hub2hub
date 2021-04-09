from hub2hub import TechnicHub, ble_handler
from time import sleep_ms

# Initialize ble handler and a technic hub
ble = ble_handler()
Thub = TechnicHub(ble)

# connect to a technic hub: press green button on the technic hub
Thub.connect()

# WeDo distance sensor connected to port A
WeDoDistance = Thub.port.A.device

# Set mode to count of taps on the sensor
WeDoDistance.mode(1)

k = 0
while True:
    Thub.led(k%11)
    
    count, = WeDoDistance.get()
    
    print('Count: ', count)

    k+=1
    sleep_ms(1000)