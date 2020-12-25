import rplidar
from rplidar import RPLidar
import time


lidar = RPLidar('/dev/ttyUSB0')
lidar.connect()
#RPLidar('COM4', baudrate=115200, timeout=1, logger=None)

lidar.start_motor()

#lidar.set_pwm(1023)
#info = lidar.get_info()
#print(info)

health = lidar.get_health()
print(health)


for i, scan in enumerate(lidar.iter_scans()):
    for counter in range(len(scan)):
        angle = scan[counter][1]
        r_value = scan[counter][2]
        if (scan[counter][1] >= 270):
            #print(type(angle))
            print(str(angle) + " degrees")
            print(str(r_value) + " mm")
            print('%d: Got %d measurements' % (i, len(scan)))
            if i > 10:
                break
            print("---------------")

lidar.stop()
lidar.stop_motor()
