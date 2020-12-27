import math
from rplidar import RPLidar
#import time #could be useful

lidar = RPLidar('COM4', baudrate=115200, timeout=1, logger=None)
lidar.connect()
# RPLidar('COM4', baudrate=115200, timeout=1, logger=None) //if using windows pc
#RPLidar('/dev/ttyUSB0') //if using linux

lidar.start_motor()

health = lidar.get_health()
print(health)

def convertToXY(angleReadings, distanceReadings):
    xSum = 0
    ySum = 0
    xDist = []
    yDist = []
    xDistances = 0
    yDistances = 0
    totalDims = 5
    squareWidth = 1800  # this needs to change -> corresponds to the x
    squareHeight = 1500  # this needs to change -> corresponds to the y
    lswidth = squareWidth / 3
    lsheight = squareHeight / 3
    lswidth2 = 2 * squareWidth / 3
    lsheight2 = 2 * squareHeight / 3

    for indx in range(1):
        xDistances = float(distanceReadings) * math.cos(math.radians(angleReadings))
        yDistances = float(distanceReadings) * math.sin(math.radians(angleReadings))
        if xDistances < squareWidth and yDistances < squareHeight:
            xDist.append(xDistances)
            yDist.append(yDistances)
            if (xDistances < lswidth and yDistances < lsheight) and (xDistances > 0 and yDistances > 0):
                print("inside live zone")
                print(xDistances)
                print(yDistances)
                separateValues()
            if (xDistances > lswidth or yDistances > lsheight) and (xDistances< lswidth2 or yDistances < lsheight2):
                print("inside deadzone")
                print(xDistances)
                print(yDistances)
                separateValues()
            if (xDistances > lswidth2 and yDistances > lsheight2) and (xDistances < squareWidth and yDistances < squareHeight):
                print("inside live zone 2")
                print(xDistances)
                print(yDistances)
                separateValues()

        # for entry in range(len(distanceReadings)):
        #     xSum += xDistances[entry]
        #     ySum += yDistances[entry]
        # print("x distance: %f :: y distance: %f" % (xDistances[entry], yDistances[entry]))
    #print(*xDist, sep=", ")
    #print(*yDist, sep=", ")
    return (xDist, yDist)

def separateValues():
    print("---------------")

for i, scan in enumerate(lidar.iter_scans()):
    for counter in range(len(scan)):
        angle = scan[counter][1]
        r_value = scan[counter][2]
        if (angle >= 90 and angle <= 180):
            angle = angle - 90
            convertToXY(angle, r_value)

lidar.stop()
