
from resources.api import requestAPI
#function to get initial index conditions. Must have 3 straight days of temp 70-85F for 6+ hours.
#Add 20 to index for each day. So index = 60 before starting index calulations. 
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


#if mildex is greater or equal to 60, start the daily calulation and update the index
#if 6 or more cont. hours and temp >= 95, add 10 points
#if temp >=95f, but not 6 or more cont between 70-85, sub 10
#if temp did not reach 95 and was between 70-85 for 6 or more cont hours, add  20 
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
