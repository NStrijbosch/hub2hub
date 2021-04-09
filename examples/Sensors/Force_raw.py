from hub2hub import TechnicHub, ble_handler
from time import sleep_ms

# Initialize ble handler and a technic hub
ble = ble_handler()
Thub = TechnicHub(ble)

# connect to a technic hub: press green button on the technic hub
Thub.connect()

# Force sensor connected to port A
ForceSensor = Thub.port.A.device

# Set mode to raw force
Force.mode(4)

k = 0
while True:
    Thub.led(k%11)
    
    raw_force, = ForceSensor.get()
    
    print('Raw force: ', raw_force)

    k+=1
    sleep_ms(1000)