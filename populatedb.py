import pprint
import pymongo
import pdb
#import pandas
import json
from bson import json_util
import requests
db = pymongo.MongoClient('localhost', 27017).StarHammer
from datetime import datetime, timedelta

import csv
with open('S&P_500.csv', 'rb') as f:
	 reader = csv.reader(f)
	 for row in reader:
	 	data_set = str(row[0])
	 	symbol =  {"Symbol": data_set}
	 	db.SP500.insert_one(symbol)