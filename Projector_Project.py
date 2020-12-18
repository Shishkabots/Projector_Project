import math
import os #maybe needed for RPI
import time #might be helpful
#from shapely.geometry import Polygon #need to install shapely

totalDims = 5
squareWidth = 2 # this needs to change -> corresponds to the x
squareHeight = 2 # this needs to change -> corresponds to the y
distanceReadings = [5.65, 4.12, 5.94, 4.2] #feet or meters
angleReadings = [43.2, 41.4, 53.5, 48.5] #radians or degrees
xDistances = [0.0] * len(distanceReadings)
yDistances = [0.0] * len(distanceReadings)

#with open('data.rtf') as f:
 #   while True:
  #          c = f.read(1)
   #         if not c:
    #            break 
     #       print(c)

def convertToXY(distanceReadings):
    xSum = 0
    ySum = 0
    for indx in range(len(distanceReadings)):
        xDistances[indx] = distanceReadings[indx] * math.cos(math.radians(angleReadings[indx]))
        yDistances[indx] = distanceReadings[indx] * math.sin(math.radians(angleReadings[indx]))

    for entry in range(len(distanceReadings)):
        xSum += xDistances[entry]
        ySum += yDistances[entry]
        print("x distance: %f :: y distance: %f" % (xDistances[entry], yDistances[entry]))

    return (xSum, ySum, xDistances, yDistances)

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


results = convertToXY(distanceReadings)
finalLocalization(results[0], results[1], results[2], results[3])





####Assuming the person is represented as a circle####
#personPolygon = Polygon([(4.118673, 3.867691), (3.090458, 2.724605), (3.533247, 4.774910), (2.783004, 3.145614)])
#objectPolygon = Polygon([()]) #predetermined coordinates that will be stored separately somewhere else
#gridPolygon = Polygon([()]) #this is the harder part -> now we are trying to find 4 points instead of 1
