from hub2hub import TechnicHub, ble_handler
from time import sleep_ms

# Initialize ble handler and a technic hub
ble = ble_handler()
Thub = TechnicHub(ble)

# connect to a technic hub: press green button on the technic hub
Thub.connect()

# WeDo tilt sensor connected to port A
TiltSensor = Thub.port.A.device

# Set mode to angle
TiltSensor.mode(0)

k = 0
while True:
    Thub.led(k%11)
    
    angle_x, angle_y = TiltSensor.get()
    
    print('angle x: ', angle_x, 'angle y: ', angle_y)

    k+=1
    sleep_ms(1000)