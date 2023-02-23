import requests
import json                 
import csv


base_url = 'https://reqres.in/api/users?page=2'
resp = requests.get(base_url)
print(resp.json())


with open ('api2.csv', 'w') as optput_file:
    writer = csv.writer(optput_file)
    writer.writerow(resp)
