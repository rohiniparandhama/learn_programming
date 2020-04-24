import requests
import json
import datetime,os,sys

try:
	url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
	response = requests.get(url = url)
	print(response.status_code)
	w_list = response.json()
	#to check if response contains 4 days data = 4 days * 24 hours= 96, so verify if list has 96 elements
	if(response.status_code==200):
		if len(w_list['list']) == 96:   #problem 1
			print("List contains data for 4 days..")
		else:
			print("Data error..")
		ch_temp=[]
		dt_list = []
		w_id = []
		for items in w_list['list']:
			dt_list.append(items['dt'])
			ch_temp.append(items['main'])
			w_id.append(items['weather'])
			for x,y in zip(dt_list, dt_list[1:]): #problem 2
				'''every hour has 3600 seconds, dt is the timestamp and 
				so to get timestamp of an hour we add 3600 to the dt of previous hour in 
				this way we can verify if data is present for every hour interval'''
				if y-x == 3600:
					print("Every hour forecast is included in the list")
				else:
					print("we are missing time interval") 
		for t in ch_temp: #problem 3
			if t['temp_min'] <= t['temp'] <= t['temp_max']:
				print("Temp is not less than temp_min or greater then temp_max")
			else:
				print("Temp does not meet the condition")
		temp_list = []
		for a in w_id:
			for b in a:
				temp_list.append(b)
				for m in temp_list:
					if m['id'] == 500: #problem 4
						print("Light rain")
					elif m['id'] == 800:
						print("Clear Sky") #problem 5
					else:
						print("Nothing")
	else:
		print(response.status_code)
except Exception as e:
	raise 
