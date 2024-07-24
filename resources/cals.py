
from resources.api import requestAPI
#function to get initial index conditions. Must have 3 straight days of temp 70-85F for 6+ hours.
#Add 20 to index for each day. So index = 60 before starting index calulations. 
#TODO create a Date Object that stores 24 hours of temps.
#TODO Logic should get number of days as a parameter and create that number of objects. Adding 24 hours to each one. 
#TODO Forecast for 30 days and add each days risk index into the day object. 
#if mildex is greater or equal to 60, start the daily calulation and update the index
class Day:
    def __init__(self, temps, date) -> None:
        self.temps=temps # assume in list of 24 temps. represent 24 hours
        self.date=date
        self.idxDel =calDelta()
        
        def calDelta(self) -> int:
            cHrs= 0 #count the # of consectuive hours between 70-85
            mHrs=0  #Keep the highest number of consectutive hours for the day
            highTemp = False #check if above 95f
            idx =0
            for temp in temps:
                mHrs = max(cHrs, mHrs)
                if temp >=70 and temp <=85:
                    cHrs = cHrs + 1
                else:
                    cHrs=0
                if temp >= 95:
                    highTemp=True # verify that this is changing 
            if mHrs>=6 and highTemp: #if 6 or more cont. hours and temp >= 95, add 10 points
                idx = idx + 10
            elif highTemp and mHrs<6:  #if temp >=95f, but not 6 or more cont between 70-85, sub 10
                idx = idx - 10
            elif mHrs>=6 and not highTemp: #if temp did not reach 95 and was between 70-85 for 6 or more cont hours, add  20 
                idx = idx + 20
            else:
                idx = idx - 10   # temp was not between 70-85 or over 95f
            return idx
            

def initIndex():
    apiData= requestAPI(True)
    temps= apiData['hourly']['temperature_2m']
    day1Hrs=0 
    day2Hrs=0
    day3Hrs=0
    maxDay1Hrs=0 
    maxDay2Hrs=0
    maxDay3Hrs=0 
    day1= temps[:24]
    day2= temps[24:48]
    day3= temps[48:72]
    #counts consectuive hours of temp between 70-85f. refactor later
    for x in day1:
        maxDay1Hrs = max(maxDay1Hrs,day1Hrs)
        if x>70 and x<85:
            day1Hrs = day1Hrs +1
        else:
            day1Hrs = 0
    for x in day2:
        maxDay2Hrs = max(maxDay2Hrs,day2Hrs)
        if x>70 and x<85:
            day2Hrs = day2Hrs +1
        else:
            day2Hrs = 0
    for x in day3:
        maxDay3Hrs = max(maxDay3Hrs,day3Hrs)
        if x>70 and x<85:
            day3Hrs = day3Hrs +1
        else:
            day3Hrs = 0
    if maxDay1Hrs>=6 and maxDay2Hrs>=6 and maxDay3Hrs >=6:
        return 60
    return 0



def singleDayCal():
    apiData = requestAPI(False)
    temps= apiData['hourly']['temperature_2m']
    hrs=0
    maxHrs = 0
    highTemp=False
    indexDelta=0
    for x in temps:
        maxHrs= max(maxHrs,hrs)
        if x>70 and x<85:
            hrs= hrs +1
        else:
            hrs = 0
        if x >=95:
            highTemp=True
    if maxHrs>=6 and highTemp:
        indexDelta = indexDelta + 10
    elif highTemp and maxHrs<6:
        indexDelta = indexDelta - 10
    elif maxHrs>=6 and not highTemp:
        indexDelta = indexDelta + 20
    else:
        indexDelta = indexDelta - 10   
    return indexDelta
