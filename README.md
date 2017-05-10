py-hawa & py-hawa-mobile
========================

py-hawa is a python script to retrive real-time air qualit index (AQI) value of a specific city from www.aqicn.org website.
py-hawa-mobile is a python which not only let the user to get real-time AQ value but also send mobile notifications on user's mobile.

Description
-----------
py-hawa let the user retrieve real-time air quality index (AQI) value of a specific city from www.aqicn.org website. The python
script send a query to the webiste containing a city name and access token. If the query request is successful, the website return
one json object containing real-time values. In addtion to py-hawa, py-hawa-mobile let the user send mobile notifications too.

Pre-Requisites
==============
  Sending Notifications Via Twilio
---------------------------------------------------
* TWILIO_ACCOUNT_SID : Your Twilio "account SID" - it's like your username for the Twilio API. This and the auth token (below) can be found [on your account dashboard](https://www.twilio.com/user/account).
* TWILIO_AUTH_TOKEN : Your Twilio "auth token" - it's your password for the Twilio API. This and the account SID (above) can be found [on your account dashboard](https://www.twilio.com/user/account).
* TWILIO_NUMBER : A Twilio number that you own, that can be used for making calls and sending messages. You can find a list of phone numbers you control (and buy another one, if necessary) [in the account portal](https://www.twilio.com/user/account/phone-numbers/incoming).

Retriving Data From AQICN Website
----------------------------------
* Access-Token: User need to get access token by registering on http://aqicn.org/data-platform/register/"
* if no access-token provided then demo access-token will be used and with demo access token only Shanghai's air quality 
  values can be retrieved."

 JSON Data:
 ----------
      {
        'status': 'ok',  # data retrived successfully
        'data': {
                  'time': {
                            's': '2016-12-11 11:00:00', # time of retrival
                            'tz': '+08:00', # +8 GMT
                            'v': 1481454000
                           }, 
                   'iaqi': {
                            'pm10': {'v': 31}, # PM10 value
                             'o3': {'v': 19},  # Ozone value 
                             'w': {'v': 6},    # Wnd value
                             'pm25': {'v': 65},# PM2.5 value 
                             'co': {'v': 6},   # Carbon monoxide value
                             'so2': {'v': 8},  # Sulphur-dioxide
                             'd': {'v': 4},    # dew value 
                             'p': {'v': 1026}, # Pssure value
                             'h': {'v': 54},   # Humidity value
                             'no2': {'v': 27}, # Nitrogen-dioxide
                             't': {'v': 13}    # Temperature value
                            }, 
                     'city': {
                            'url': 'url of the city'
                            'geo': ['longitude','latitude'], 
                            'name': 'name of city'
                            }, 
                      'idx': 1437, 
                      'aqi': 65 # air quality index value
                  }
      }

Dependencies
------------
py-udownloader depend on third party libraries and you will first need to install the application's dependencies. 
* urrlib
* twilio ( py-hawa-mobile)

Running the Script
--------------------
[Download the project source code directly](https://github.com/raosaif/py_hawa/archive/master.zip) or [clone the repository on GitHub](https://github.com/raosaif/py_hawa.git).  Navigate to the folder with the source code on your machine in a terminal window.

    $ 'usage: %s [-c city] [-a accesstoken] [-n notify] [-h help]' (py-hawah)
    $ 'usage: %s [-c city] [-a accesstoken] [-n notify] [-m mobileNotification] [-h help]' (py-hawa-mobile)
    
    "city: name of the city"
    "accesstoken: You need to get access token by registering on http://aqicn.org/data-platform/register/"
    "notify: True or False- show the notification tray on linux"
    "mobileNotification: For this feature to work, user need to rprovide twilio account credientials" (py-hawa-mobile)
    
    * ./py-hawa -c cityname -a accesstoken -n True
    * ./py-hawa-mobile -c cityname -a accesstoken -n True -m True
AQI Guide
---------
* http://aqicn.org/faq/2015-09-06/ozone-aqi-using-concentrations-in-milligrams-or-ppb/
* http://aqicn.org/faq/2015-03-15/air-quality-nowcast-a-beginners-guide/
* http://aqicn.org/faq/2013-02-02/why-is-pm25-often-higher-than-pm10/
* http://aqicn.org/faq/2016-11-20/nitrogen-dioxyde-no2-in-our-atmosphere/
* http://aqicn.org/faq/2016-08-10/ozone-aqi-scale-update/
* https://en.wikipedia.org/wiki/Air_pollution
