

### This program takes static/given JSON data as input and writes them in a CSV file
### Note that, the final csv file will have no header

import json
import csv


users = '{"user_info":[{"name": "Alex", "email": "alex@gmail.com", "job": "Developer"},{"user": "Rider", "email": "rider@gmail.com", "job": "Tester"}]}'
### Note that JSON data given here in string format

user_parsed = json.loads(users)
user_data = user_parsed['user_info']

# open a csv file for writing the data
file = open('user_info0902.csv', 'w')

# create the csv writer object
csvwriter = csv.writer(file)
count = 0

for x in user_data:
      csvwriter.writerow(x.values())
file.close()
