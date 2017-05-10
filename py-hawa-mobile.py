#!/usr/bin/env python3
import urllib.request
import requests
import json
import sys
import os
import io
import getopt
from twilio.rest import Client



def main(argv):

	def usage():
		print(('usage: %s [-c city] [-a accesstoken] [-n notify] [-m mobileNotification] [-h help] ...' % argv[0]))
		return 100
	try:
	    (opts, args) = getopt.getopt(argv[1:], 'c:a:n:m:h')
	except getopt.GetoptError:
		return usage()

	def help():
		print("py-hawa let the user know the real-time air quality values"
			"\ncity: name of the city"
			"\naccesstoken: You need to get access token by registering on http://aqicn.org/data-platform/register/"
			"\nif no accesstoken provided then demo accesstoken will be used and with demo access token only Shanghai's air quality values can be retrieved."
			"\nnotify: True or False- show the notification tray on linux"
			"\nmobileNotification: For this feature to work, user need to rprovide twilio account credientials")

	def registerTwilio():
		print()

	city = 'shanghai'
	accesstoken = 'demo'
	notify = ''
	sendTrayNotification = None
	ACCOUNT_SID = ''
	AUTH_TOKEN = ''
	toNum = ''  # the number with your registered on twilio account
	fromNum = '' # your twilio account number. 
	sendMobileNotification = None

	for (k, v) in opts:
		if k == '-c': 
			city= v 

		elif k == '-a': 
			accesstoken = v

		elif k == '-n': 
			if v != True and v != False:
				return help()
			else:
				sendTrayNotification = v

		elif k == '-m':
			if v == True:
				if len(ACCOUNT_SID) < 5 or len(AUTH_TOKEN) < 5 or len(toNum) < 5 or len(fromNum) < 5:
					sendMobileNotification = False
					return registerTwilio()

				else:
					sendMobileNotification = v

		elif k == '-h' : return help()



	CurrentValue = ''

	url = 'http://api.waqi.info/feed/'+city+'/?token=' + accesstoken
	print('URL: ',url)

	r = requests.get(url, auth=('user', 'pass'))
	if r.status_code == 200:
		data = r.json()
		print (data)
		value = data['data']['iaqi']['pm25']['v']
		toDisplay = str(value)

		if value > 0 and value < 50:
			notify = 'notify-send "Air Quality Alert:" "Current Value: Healthy - "' + toDisplay
			CurrentValue = 'Current Reading: ' + str(toDisplay) + ' Healthy'

		elif value > 50 and value < 100:
			notify = 'notify-send "Air Quality Alert:" "Current Value: Moderate - "' + toDisplay
			CurrentValue = 'Current Reading: ' + str(toDisplay) + ' Moderate'

		elif value > 100 and value < 150:
			notify = 'notify-send "Air Quality Alert:" "Current Value: Sensitive - "' + toDisplay
			CurrentValue = 'Current Reading: ' + str(toDisplay) + ' Sensitive (Mask Recommended)'

		elif value > 150 and value < 200:
			notify = 'notify-send "Air Quality Alert:" "Current Value: UnHealhty - "' + toDisplay
			CurrentValue = 'Current Reading: ' + str(toDisplay) + ' UnHealthy (Wear Mask)'

		elif value > 200 and value < 250:
			notify = 'notify-send "Air Quality Alert:" "Current Very Unhealhty - "' + toDisplay
			CurrentValue = 'Current Reading: ' + str(toDisplay) + ' Very Healthy (Please Wear Mask)'


		elif value > 250 and value > 300:
			notify = 'notify-send "Air Quality Alert:" "Current Value: Hazardous -  "' + toDisplay
			CurrentValue = 'Current Reading: ' + str(toDisplay) + ' UnHealthy (Please Please Wear Mask)'

	else:
		notify = 'notify-send "Error: " "Unable to Connect"'


	if sendTrayNotification:
		os.system(notify)
	else:
		print('[Debug] Tray Notification is off.')

	msg_body = CurrentValue

	if sendMobileNotification:
		client = Client(ACCOUNT_SID, AUTH_TOKEN) #
		client.api.account.messages.create(to=toNum, from_=fromNum, body=msg_body)
	else:
		print('[Debug] Mobile notification is turned off.')


if __name__ == '__main__':
    sys.exit(main(sys.argv))