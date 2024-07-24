from resources.dataf import *
from resources.cals import *
from resources.api import *
from resources.sendemail import *
from datetime import datetime, timedelta
import pytz

pst = pytz.timezone('US/Pacific')
tommorow = (datetime.now(pst) + timedelta(1)).strftime('%Y-%m-%d')
delta = 0
currentIndex = ReadIndex()['Mildex'] 
if currentIndex == 0:
    delta = initIndex()
    
else:
    delta = singleDayCal()
newIndex= currentIndex+ delta
print(type(newIndex))
indexToWrite = { 'Mildex' : newIndex if newIndex >0 else 0 }
print("Tommorow's Forecasted Mildew Index is: " + str(newIndex))
writeIndex(indexToWrite)
msg = sendEmail(newIndex, tommorow)

