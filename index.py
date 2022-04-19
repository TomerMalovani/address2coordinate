# read excel with pandas and edit i
import os

import pandas as pd
import urllib.request
import json
from dotenv import load_dotenv

load_dotenv()


key=os.getenv('GEO_API')

def addressToCoordinate(address):
	formated_address = urllib.parse.quote(address)
	req_url='https://maps.googleapis.com/maps/api/geocode/json?address='+ formated_address +'&key='+key
	print(req_url)
	contents =urllib.request.urlopen(req_url)
	respond = json.loads(contents.read().decode())
	if len(respond['results'])==0:
		return {"lat":"","lng":""}
	res = respond['results'][0]['geometry']
	print(str(res['location']['lat']) + " " + str(res['location']['lng']))
	return {"lat":str(res['location']['lat']),"lng":str(res['location']['lng'])}









def main():
	file_path="."
	# create new xlsx file
	# read xlsx file

	importFile = pd.read_excel("./import.xlsx")

	df = pd.DataFrame(columns=['id','customerId','name','address1','address2','zip','city','region','country','lat','lng'])
	df.to_excel(file_path+"/mojo.xlsx", index=False)

	# read xlsx file
	df = pd.read_excel(file_path+"/mojo.xlsx")
	

	
	for i in range(1,len(importFile.index)):
		resData= addressToCoordinate(importFile.loc[i, 'city'] + " " + importFile.loc[i, 'address1'] )
		df.loc[i, 'customerId'] = importFile.loc[i, 'customerId']
		# should choose how to read data
		# df.loc[i, 'name'] = importFile.loc[i, 'name']
		# df.loc[i, 'city'] = importFile.loc[i, 'city']
		df.loc[i, 'country'] = "IL"
		df.loc[i, 'lng'] = resData['lng']
		df.loc[i, 'lat'] = resData['lat']
		print(resData)
		df.to_excel(file_path+"/mojo.xlsx", index=False)
            


main()