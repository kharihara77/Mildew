import requests
from datetime import date, timedelta
  
def createUrl(days:int ,lat:float, long: float, timezone: str) -> str:
    #url="https://api.open-meteo.com/v1/forecast?latitude=" + str(lat) +"&longitude=" + str(long) +"&hourly=temperature_2m&temperature_unit=fahrenheit&timezone=America%2FLos_Angeles&past_days=" + str(days) + "&forecast_days=0" 
    url="https://api.open-meteo.com/v1/forecast?latitude=" + str(lat) +"&longitude=" + str(long) +"&hourly=temperature_2m&temperature_unit=fahrenheit&timezone=America%2FLos_Angeles&past_days=" + str(days) + "&forecast_days=1"  
    return url

def requestAPI(initBool: bool):
    #startDate = (date.today() -timedelta(days=4)).strftime('%Y-%m-%d')
    #endDate = (date.today() -timedelta(days=2)).strftime('%Y-%m-%d')
    lat= 45.1470196
    long= -123.29627
    timezone = "Los_Angeles"
    #check whether to start a 3 day calulation or daily update
    if initBool:
       response = requests.get(createUrl(2, lat, long,timezone))
    else:
        response = requests.get(createUrl(0, lat, long, timezone)) 
    return response.json() 
