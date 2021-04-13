from hub2hub import TechnicHub, ble_handler
from time import sleep_ms

# Initialize ble handler and a technic hub
ble = ble_handler()
Thub = TechnicHub(ble)

# connect to a technic hub: press green button on the technic hub
Thub.connect()

k = 0
while True:
    Thub.led(k%11)
    
    yaw, pitch, roll = Thub.motion.yaw_pitch_roll()
    shaken = Thub.motion.was_gesture(3)
    
    print('Roll angle: ', roll, 'Shaken?: ', shaken)

    k+=1
    sleep_ms(1000)
    
    
