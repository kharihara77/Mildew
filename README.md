## Mildew Predictor
This a mildew risk index predictor/calculator for vineyards. 

Index calculations:
1. The index calculations begin when the temperature is between 70-85°F for 6 or
more continuous hours for 3 consecutive days.
2. Starting with the index at 0 on the first day, add 20 points for each day when the
temperature is between 70-85°F.
3. Until the index reaches 60, if a day has fewer than 6 continuous hours of
temperatures between 70-85°F, reset the index to 0.
4. When the index reaches 60, if a day has fewer than 6 continuous hours of
temperatures between 70-85°F, subtract 10 points.
5. For a day when the temperature is between 70-85°F for 6 or more continuous
hours, add 20 points.
6. For a day when the temperatures reach 95°F for more than 15 minutes, subtract 10
points.
7. For a day when the temperatures reach 95°F for more than 15 minutes and the
temperature is between 70-85°F for 6 or more continuous hours, add 10 points.

Currently, location can be changed with updates to LAT and LONG

mildex.pkl contains the persistent mildew risk index that will used each day of calculation.

## Usage
If wanting to sendemail with index, change "from_email" and "from_password" in sendemail.py. If using GMAIL, must use APP password.  
run main.py. 

## CronJob 
change file path of pickle in dataf to absoulte file path if using cronjob/n

## Todo
Add Fields for user input LAT LONG

Take 30 day forecast and 

