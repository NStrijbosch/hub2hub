from hub2hub import TechnicHub, ble_handler
from time import sleep_ms

# Initialize ble handler and a technic hub
ble = ble_handler()
Thub = TechnicHub(ble)

# connect to a technic hub: press green button on the technic hub
Thub.connect()

# Servo motor connected to port A
Motor = Thub.port.A.motor

# Set speed to 50
Motor.run_at_speed(50)

# Wait 1 second
sleep_ms(1000)

# Set speed to 0
Motor.run_at_speed(0)