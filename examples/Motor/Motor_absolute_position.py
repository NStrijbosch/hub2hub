from hub2hub import TechnicHub, ble_handler
from time import sleep_ms

# Initialize ble handler and a technic hub
ble = ble_handler()
Thub = TechnicHub(ble)

# connect to a technic hub: press green button on the technic hub
Thub.connect()

# Servo motor connected to port A
Motor = Thub.port.A.motor

# Set mode to absolute position
Motor.mode(3)

k = 0
while True:
    Thub.led(k%11)
    
    # Get measurement
    absolute_position, = motor.get()
    
    print('Absolute position: ', absolute_position)

    k+=1
    sleep_ms(1000)