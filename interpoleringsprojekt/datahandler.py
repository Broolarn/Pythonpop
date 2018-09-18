#interpolation#interpolation

import gspread
import numpy as np
import string
import json
from oauth2client.service_account import ServiceAccountCredentials


def loaddatafromweebsheet():
	scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
	creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
	gclient = gspread.authorize(creds)
	sheet = gclient.open("be0101tab9utveng2017").sheet1
	return sheet

def writetoxml(toxml,titles):
	

	if(toxml):
		endat = len(toxml[:][0]) 
		data = {}  
		for i in range(0,len(titles)-1):
			data[titles[i]] = []
			for u in range(0,endat):
				#print(toxml[i][u])
				data[titles[i]].append({(titles[i]): toxml[i][u]

					})
				#example of data
		# data['people'] = []  
		# data['people'].append({  
		#     'name': 'Scott',
		#     'website': 'stackabuse.com',
		#     'from': 'Nebraska'
		# })
		
		with open('data.txt', 'w') as outfile:  
   			json.dump(data, outfile)
	else:
		print("Could not write/was nothing to be written")
		data = {} 
		
	return data

def setupsheet(sheet):
	# read in from sheet
	pythonsheets = sheet.get_all_records()
	Year = sheet.col_values(1);
	Pop = sheet.col_values(2); 
	Births = sheet.col_values(3);
	Deaths = sheet.col_values(4);
	Immigrations = sheet.col_values(5);
	Emigrations = sheet.col_values(6);
	Marriages = sheet.col_values(7);
	Divorces = sheet.col_values(8);
	
	
	Firstslot = 3 #data börjar på 3
	Year = Year[Firstslot::] # ska bli int 
	Pop = Pop[Firstslot::]  # ska bli int , omformatera
	Births = Births[Firstslot::] # ska bli int , omformater
	Deaths = Deaths[Firstslot::]
	Immigrations = Immigrations[Firstslot::] # ska bli int
	Emigrations = Emigrations[Firstslot::]
	Marriages  = Marriages[Firstslot::]
	Divorces  = Divorces[Firstslot::]

	Cattegorarray  = [Year,Pop,Births,Deaths,Immigrations,Emigrations,Marriages,Divorces]

	
	for n in range ( 0, len(Cattegorarray)): 
		chaning = Cattegorarray[n]
		for i in range (0,len(Year)):
			temp = str(chaning[i:i+1]).replace('\\xa0','').replace("'","")
			temp = ''.join(c for c in temp if c not in '(){}<>[]\\"')
			if(temp == '..'):
				temp = 0

			#if(temp):
			temp = int(temp)#last step
			chaning[i] = temp
		Cattegorarray[n] = chaning;
		
	
	return Cattegorarray;

def Gettitles(sheet):

	pythonsheets = sheet.get_all_records()
	Year = sheet.col_values(1);
	Pop = sheet.col_values(2);
	Births = sheet.col_values(3);
	Deaths = sheet.col_values(4);
	Immigrations = sheet.col_values(5);
	Emigrations = sheet.col_values(6);
	Marriages = sheet.col_values(7);
	Divorces = sheet.col_values(8);

	#convert to arrays 
	Cattegorislot = 2
	
	Namearray = [Year[Cattegorislot],Pop[Cattegorislot],Births[Cattegorislot],Deaths[Cattegorislot],Immigrations[Cattegorislot],Marriages[Cattegorislot],Divorces[Cattegorislot]]

	return Namearray;
