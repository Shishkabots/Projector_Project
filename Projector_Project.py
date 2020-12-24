import math
import os #maybe needed for RPI
import time #might be helpful
#from shapely.geometry import Polygon #need to install shapely


totalDims = 5
squareWidth =  1800 # this needs to change -> corresponds to the x
squareHeight = 1500 # this needs to change -> corresponds to the y
lswidth = squareWidth/3
lsheight = squareHeight/3
lswidth2 = 2 * squareWidth/3
lsheight2 = 2 * squareHeight/3
# distanceReadings = [5.65, 4.12, 5.94, 4.2] #feet or meters
# angleReadings = [43.2, 41.4, 53.5, 48.5] #radians or degrees

#with open('data.rtf') as f:
 #   while True:
  #          c = f.read(1)
   #         if not c:
    #            break 
     #       print(c)

def readFileData(file):
    fp = open(file)
    angleReadings = []
    distanceReadings = []
    nums = []
    all_lines = fp.readlines()

    all_lines = all_lines[3:]
    for line in all_lines:
        nums = line.strip().split(' ')
        ang = int(float(nums[0]))
        if ang >90 and ang < 180:
            angleReadings.append(ang - 90)
            distanceReadings.append(nums[1])
    print(len(angleReadings))
    print(len(distanceReadings))
    fp.close()     
    return (angleReadings, distanceReadings)

def convertToXY(angleReadings, distanceReadings):
    xSum = 0
    ySum = 0
    xDist = []
    yDist = []
    xDistances = [0.0] * len(distanceReadings)
    yDistances = [0.0] * len(distanceReadings)
    
    for indx in range(len(distanceReadings)):
        xDistances[indx] = float(distanceReadings[indx]) * math.cos(math.radians(angleReadings[indx]))
        yDistances[indx] = float(distanceReadings[indx]) * math.sin(math.radians(angleReadings[indx]))
        if xDistances[indx] < squareWidth and yDistances[indx] < squareHeight:
            xDist.append(xDistances[indx])
            yDist.append(yDistances[indx])
            if (xDistances[indx] < lswidth and yDistances[indx] < lsheight) and (xDistances[indx] > 0 and yDistances[indx] >0)  :
                 print ("inside live zone")
                 print (xDistances[indx])
                 print (yDistances[indx])
            if (xDistances[indx] > lswidth or yDistances[indx] > lsheight) and (xDistances[indx] < lswidth2 or yDistances[indx] < lsheight2) :
                 print ("inside deadzone")
                 print (xDistances[indx])
                 print (yDistances[indx])
            if (xDistances[indx] > lswidth2 and yDistances[indx] > lsheight2) and (xDistances[indx] < squareWidth and yDistances[indx] < squareHeight) :
                print ("inside live zone 2")
                print (xDistances[indx])
                print (yDistances[indx])

            
    # for entry in range(len(distanceReadings)):
    #     xSum += xDistances[entry]
    #     ySum += yDistances[entry]
        #print("x distance: %f :: y distance: %f" % (xDistances[entry], yDistances[entry]))
    print (*xDist, sep = ", ")
    print (*yDist, sep = ", ")
    return (xDist, yDist)

####Assuming the person is represented as a point####
def finalLocalization(xSum, ySum, xDistances, yDistances):
    x1 = (xSum / len(xDistances))
    y1 = (ySum / len(yDistances))
    xAvg = ((xSum / len(xDistances)) * 100) / 100
    yAvg = ((ySum / len(yDistances)) * 100) / 100
    print("\nUnrounded raw coordinates: %f, %f" % (x1, y1))
    print("\nInitial raw coordinates: %d, %d" % (xAvg, yAvg))

    finalXLocation = xAvg / squareWidth
    finalYLocation = (yAvg / squareHeight)
    print("Final mapped coordinates: %d, %d" % (finalXLocation, finalYLocation))



angleReadings, distanceReadings = readFileData('livetest4.txt')
results = convertToXY(angleReadings, distanceReadings)
#finalLocalization(results[0], results[1], results[2], results[3])






####Assuming the person is represented as a circle####
#personPolygon = Polygon([(4.118673, 3.867691), (3.090458, 2.724605), (3.533247, 4.774910), (2.783004, 3.145614)])
#objectPolygon = Polygon([()]) #predetermined coordinates that will be stored separately somewhere else
#gridPolygon = Polygon([()]) #this is the harder part -> now we are trying to find 4 points instead of 1
