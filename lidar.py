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
            
def convertToXY(angleReadings, distanceReadings):
    xSum = 0
    ySum = 0
    xDistancesList = []
    yDistancesList = []
    
    for indx in range(len(distanceReadings)):
        xPos = (float(distanceReadings) * math.cos(math.radians(angleReadings)))
        yPos = (float(distanceReadings) * math.sin(math.radians(angleReadings)))
        if xPos <= xBorder and yPos <= yBorder:
          xDistancesList.append (xPos)
          yDistancesList.append (yPos)

    for entry in range(len(xDistancesList)):
        xSum += xDistancesList[entry]
        ySum += yDistancesList[entry]
        #print("x distance: %f :: y distance: %f" % (xDistancesList[entry], yDistances[entry]))

    return (xSum, ySum, xDistancesList, yDistancesList)

lidar.stop()
lidar.stop_motor()
