from hub2hub import TechnicHub, ble_handler
from time import sleep_ms

# Initialize ble handler and a technic hub
ble = ble_handler()
Thub = TechnicHub(ble)

# connect to a technic hub: press green button on the technic hub
Thub.connect()

# Color sensor
ColorSensor = Thub.port.A.device

# Set mode to ambient light
ColorSensor.mode(2)

k = 0
while True:
    Thub.led(k%11)
    
    ambient, = ColorSensor.get()
    
    print('Ambient light: ', ambient)

    k+=1
    sleep_ms(1000)