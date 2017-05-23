import pprint
import pymongo
import pdb
#import pandas
import json
from bson import json_util
import requests
db = pymongo.MongoClient('localhost', 27017).StarHammer
from datetime import datetime, timedelta

stockArr= db.SP500.find()
first_part = "https://www.quandl.com/api/v3/datasets/WIKI/"
last_part = "/data.json?limit=1&api_key=Q7DSNVGYPQ9WnMmxEgVb"



for t in stockArr:
	print t["Symbol"]
	link = first_part + t["Symbol"] + last_part
	r = requests.get(link)
	quandl_stock_json = r.json()
	new = {
		"Symbol": t["Symbol"],
		"Date": quandl_stock_json["dataset_data"]["data"][0][0],
		"Open":quandl_stock_json["dataset_data"]["data"][0][1],
		"High":quandl_stock_json["dataset_data"]["data"][0][2],
		"Low":quandl_stock_json["dataset_data"]["data"][0][3],
		"Close":quandl_stock_json["dataset_data"]["data"][0][4],
		"Volume":quandl_stock_json["dataset_data"]["data"][0][5]
	}
	


	db.SP500Stocks.update({"Symbol":new["Symbol"], "Date":new["Date"]},new,upsert=True)

	
print "complete"
	
