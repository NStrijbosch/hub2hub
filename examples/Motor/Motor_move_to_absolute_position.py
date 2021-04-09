from hub2hub import TechnicHub, ble_handler
from time import sleep_ms

# Initialize ble handler and a technic hub
ble = ble_handler()
Thub = TechnicHub(ble)

# connect to a technic hub: press green button on the technic hub
Thub.connect()

# Servo motor connected to port A
Motor = Thub.port.A.motor

# move to 180 degrees and hold
Motor.run_to_position(180,stop_action = 2)

sleep_ms(1000)

# move to 0 and float
Motor.run_to_position(0, stop_action = 0)