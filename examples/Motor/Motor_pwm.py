from hub2hub import TechnicHub, ble_handler
from time import sleep_ms

# Initialize ble handler and a technic hub
ble = ble_handler()
Thub = TechnicHub(ble)

# connect to a technic hub: press green button on the technic hub
Thub.connect()

# Servo motor connected to port A
Motor = Thub.port.A.motor

# Start at power
Motor.pwm(50)

# Wait 1 second
sleep_ms(1000)

# Set power to 0
Motor.pwm(0)