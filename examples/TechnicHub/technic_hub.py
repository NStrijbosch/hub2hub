from hub2hub import TechnicHub, ble_handler
from time import sleep_ms

# Initialize ble handler and a technic hub
ble = ble_handler()
Thub = TechnicHub(ble)

# connect to a technic hub: press green button on the hub
Thub.connect()

k = 0
while True:
    Thub.led(k%11)
    
    yaw, pitch, roll = Thub.motion.yaw_pitch_roll()
    
    print('Roll angle: ', roll)

    k+=1
    sleep_ms(1000)