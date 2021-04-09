from hub2hub import TechnicHub, ble_handler
from time import sleep_ms

# Initialize ble handler and a technic hub
ble = ble_handler()
Thub = TechnicHub(ble)

# connect to a technic hub: press green button on the technic hub
Thub.connect()

# Color/Distance sensor connected to port A
BoostSensor = Thub.port.A.device

# Set mode to distance 
BoostSensor.mode(1)

k = 0
while True:
    Thub.led(k%11)
    
    distance, = BoostSensor.get()
    
    print('distance: ', distance)

    k+=1
    sleep_ms(1000)