import requests, urllib.request, urllib.error, urllib.parse, sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication
import datetime as dt
import pandas as pd
from  bs4 import BeautifulSoup
from collections import Counter 



def Bing_local():
	#NEED USER INPUT FROM TEXTBOX
	postcode = input('Please enter postcode: ')
	df = requests.get('http://dev.virtualearth.net/REST/v1/Locations/UK/' + postcode + '?&key=Aji5eQh4Mr28uTRc3lVr4lKi1bMiDgzOR3KKDn1s39RtCQj2h1IKyomDtrSLxh9F').json()
	location = df['resourceSets'][0]['resources'][0]['point']['coordinates']
	locationstr = str(location)
	latitude_temp, longitude_temp = locationstr.split(',')
	
	latitude = latitude_temp.replace('[','').replace(' ','')
	longitude = longitude_temp.replace(']','').replace(' ','')
	print (' ')
	print ('latitude is: ' + latitude + ' longitude is: ' + longitude)
	print (' ')

	return latitude, longitude

#find all decision types possible 
def DecisionTypes():
	one = ''
	test = []
	outcomes_list = []
	counter = 20
	r = requests.get('https://data.police.uk/docs/method/crime-street/')
	r_html = r.text

	soup = BeautifulSoup(r.content, "html.parser")
	table = soup.findAll('td', class_ = 'desc')

#remove html script from decision type
	for counter in range(20,47):
		john = str(table[counter]).replace('<td class="desc">','').replace('</td>','')
		
		outcomes_list.append(john)
		counter += 1
	
	
	

	'''Court result unavailable
	Court case unable to proceed
	Local resolution
	Investigation complete; no suspect identified
	Offender deprived of property
	Offender fined
	Offender given absolute discharge
	Offender given a caution
	Offender given a drugs possession warning
	Offender given a penalty notice
	Offender given community sentence
	Offender given conditional discharge
	Offender given suspended prison sentence
	Offender sent to prison
	Offender otherwise dealt with
	Offender ordered to pay compensation
	Suspect charged as part of another case
	Suspect charged
	Defendant found not guilty
	Defendant sent to Crown Court
	Unable to prosecute suspect
	Formal action is not in the public interest
	Action to be taken by another organisation
	Further investigation is not in the public interest
	Under investigation
	Status update unavailable'''
	
	



def GetData():

	# Experimental idea, automate crime type names, works but don't need
	'''
	crime_types = requests.get('https://data.police.uk/api/crime-categories?date=2017-08').json()

	antisocial = crime_types[1]
	bicycle = crime_types[4]

	print ('anti: ' + str(antisocial))
	print (str(bicycle))
	'''
	
	latitude, longitude = Bing_local()
	crimelink = 'https://data.police.uk/api/crimes-street/all-crime?&lat=' + latitude + '&lng=' + longitude
	decisionlink = 'https://data.police.uk/api/outcomes-at-location?lat=' +  latitude + '&lng=' + longitude
	print ('crimelink: ' + crimelink)
	print (' ')
	print ('decisionlink: ' + decisionlink)
	print (' ')
#get data
	crimes = requests.get(crimelink).json()
	decision = requests.get(decisionlink).json()
#find no of crimes/of which type/outcome
	No_Crimes_types = Counter(player['category'] for player in crimes)
	No_decision_types = Counter(names['category']['name'] for names in decision)
	print (No_decision_types)
	print ('len: ' + str(len(crimes)))
	print ('len: ' + str(len(decision)))
	print ('decision totals: ' + str(No_decision_types))
	
	print(' ')

	
	No_anti_social = (No_Crimes_types['anti-social-behaviour'])
	No__bicycle_theft = 	(No_Crimes_types['bicycle-theft'])
	No_burglary = (No_Crimes_types['burglary'])
	No_criminal_damage_arson = (No_Crimes_types['criminal-damage-arson'])
	No_drugs = (No_Crimes_types['drugs'])
	No_other_theft = (No_Crimes_types['other-theft'])
	No_possession_weapons = (No_Crimes_types['possession-of-weapons'])
	No_public_order = (No_Crimes_types['public-order'])
	No_robbery = (No_Crimes_types['robbery'])
	No_shoplifting = (No_Crimes_types['shoplifting'])
	No_theft_person = (No_Crimes_types['theft-from-the-person'])
	No_vehicle_crime = (No_Crimes_types['vehicle-crime'])
	No_violent_crime = (No_Crimes_types['violent-crime'])
	No_other_crime = (No_Crimes_types['other-crime'])
#weighted crime
	anti_social_W = No_anti_social * 0.01
	bicycle_theft_W = No__bicycle_theft * 0.01
	burglary_W = No_burglary * 0.1
	criminal_damage_arson_W = No_criminal_damage_arson * 0.05
	drugs_W = No_drugs * 0.02
	other_theft_W = No_other_theft * 0.05
	possession_weapons_W = No_possession_weapons * 0.15
	public_order_W = No_public_order * 0.01
	robbery_W = No_robbery * 0.1
	shoplifting_W = No_shoplifting * 0.05
	theft_person_W = No_theft_person * 0.1
	vehicle_crime_W = No_vehicle_crime * 0.05
	violent_crime_W = No_violent_crime * 0.3
	other_crime_w = No_other_crime * 0.01

	Safety_rating = anti_social_W + bicycle_theft_W + burglary_W + criminal_damage_arson_W +drugs_W + other_theft_W + possession_weapons_W + public_order_W + robbery_W + shoplifting_W + theft_person_W + vehicle_crime_W + violent_crime_W + other_crime_w
	
	print ('DANGER LEVEL: ' + str(Safety_rating))

	return Safety_rating


	#crimes = requests.get('https://data.police.uk/api/' + postcode + '/neighbourhoods').json()

GetData()
#DecisionTypes()

