import requests
from datetime import date, timedelta
  
#TODO add forecasting for up to 16 days using start and end date. Max forecast days is 16. 
def requestAPI(lat:int, long:int, timezone: str, forecast:int):
    #startDate = (date.today() -timedelta(days=4)).strftime('%Y-%m-%d')
    #endDate = (date.today() -timedelta(days=2)).strftime('%Y-%m-%d')
    startDate = (date.today() + timedelta(days=1)).strftime('%Y-%m-%d')
    endDate = (date.today() + timedelta(days=1)).strftime('%Y-%m-%d')
    lat= 45.1470196
    long= -123.29627
    timezone = "Los_Angeles"
    url= "https://api.open-meteo.com/v1/forecast?latitude=" + str(lat) +"&longitude=" + str(long) +"&hourly=temperature_2m&temperature_unit=fahrenheit&timezone=America%2F" + timezone +"&forecast_days=" + str(forecast)
    response = requests.get(url)
    return response.json()['hourly']

#https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&temperature_unit=fahrenheit&timezone=America%2FLos_Angeles&start_date=2024-08-06&end_date=2024-08-10

