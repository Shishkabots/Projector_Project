import rplidar
from rplidar import RPLidar
import time

#import rospy
#from rplidar import laser_filters
lidar = RPLidar('COM4', baudrate=115200, timeout=1, logger=None)
lidar.connect()
#RPLidar('/dev/ttyUSB0')
#lidar.stop_motor()
#time.sleep(3)
lidar.set_pwm(1023)
lidar.start_motor()
#info = lidar.get_info()
#print(info)

health = lidar.get_health()
print(health)
#angle = lidar
#print(angle)

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
