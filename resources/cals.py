
from datetime import datetime as dt
#from resources.api import requestAPI
#function to get initial index conditions. Must have 3 straight days of temp 70-85F for 6+ hours.
#Add 20 to index for each day. So index = 60 before starting index calulations. 
#TODO create a Date Object that stores 24 hours of temps.
#TODO Logic should get number of days as a parameter and create that number of objects. Adding 24 hours to each one. 
#TODO Forecast for 30 days and add each days risk index into the day object. 
#if mildex is greater or equal to 60, start the daily calulation and update the index
class Day:
    def __init__(self, temps: list, date: str) -> None:
        """
        Create a new Day object.

        Parameters
        ----------
        temps : list
            A list of 24 temperatures representing 24 hours.
        date : str
            The date of the day in the format 'YYYY-MM-DD'.

        Attributes
        ----------
        temps : list
            A list of 24 temperatures representing 24 hours.
        date : str
            The date of the day in the format 'YYYY-MM-DD'.
        idxDel : int
            The delta for the index based on the temperatures.
        """
        self.temps = temps
        self.date = date
        self.idxDel = self.calculate_delta()
        
    def calculate_delta(self) -> int:
        """Calculate the delta for the index based on the temperatures."""
        consecutive_hours = 0
        max_consecutive_hours = 0
        high_temperature_reached = False
        delta = 0

        for temp in self.temps:
            max_consecutive_hours = max(consecutive_hours, max_consecutive_hours)

            if 70 <= temp <= 85:
                consecutive_hours += 1
            else:
                consecutive_hours = 0

            if temp >= 95:
                high_temperature_reached = True

        if max_consecutive_hours >= 6 and high_temperature_reached:
            delta += 10
        elif high_temperature_reached and max_consecutive_hours < 6:
            delta -= 10
        elif max_consecutive_hours >= 6 and not high_temperature_reached:
            delta += 20
        else:
            delta -= 10

        return delta
            
def getDate(timestamp:str):
    format_str = "%Y-%m-%dT%H:%M"
    date_time = dt.strptime(timestamp, format_str)
    return date_time.strftime('%Y-%m-%d')


def createObjects(forecast:list):
    #temps will be a dictionary; key1: time key2: temp via requestAPI method
    daysLst =[] #store list of objects
    hoursLst=[] #store ints of temps for each hour for 1 day
    count=0 # count for counting hours in a day. 24 means 1 day has elasped.
    for i,temp in enumerate(forecast['temperature_2m']):
        #print(temp)
        if count ==23: #Reached end of day. Start tracking next day
           date=getDate(forecast['time'][i])
           hoursLst.append(temp)
           newDay = Day(hoursLst,date)
           daysLst.append(newDay)
           count=0
           hoursLst = []
        else:
        #add each hour temp to hoursLst
            hoursLst.append(temp)
            count = count +1 
    return daysLst 






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
