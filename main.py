from resources.dataf import *
from resources.cals import *
from resources.api import *

delta = 0
currentIndex = ReadIndex()['Mildex'] 
if currentIndex == 0:
    delta = initIndex()
    
else:
    delta = singleDayCal()
    print(delta)
newIndex= currentIndex+ delta
indexToWrite = { 'Mildex' : newIndex if newIndex >0 else 0 }
print("Tommorow's Forecasted Mildew Index is: " + str(newIndex))
writeIndex(indexToWrite)
