#/usr/bin/python3
import requests
import json
import time
import sys
import csv

ips = sys.argv[1]

fips = open(ips, "r"); lips = fips.read().splitlines(); fips.close();
jsonResult = {'Data':[]}

for ip in lips:
	getjson = requests.get("http://ip-api.com/json/"+ip)
	print(getjson.text)
	jsonResult['Data'].append(json.loads(getjson.text))

	finw = open("resultIP.json", "a+")
	finw.write(","+getjson.text+"\n")
	time.sleep(1.5)

data_file = open('csvResult.csv', 'w') 
csv_writer = csv.writer(data_file)
count = 0

for data in jsonResult['Data']:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())
data_file.close()
