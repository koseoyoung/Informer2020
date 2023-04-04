import csv
from datetime import datetime


# Open the CSV file
with open('raw.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

time_index = rows[0].index('time')
initial_index = rows[0].index('srcip')
proto_index = rows[0].index('proto')

for i, row in enumerate(rows):
    converted = ''
    if i == 0: 
        converted = 'date'
    else: 
        unix_timestamp = int(row[time_index]) / 1000000
        converted = datetime.utcfromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')
        row[proto_index] = 0
        
    row[time_index], row[initial_index] =row[initial_index], converted


# Write the updated rows to a new CSV file
with open('updated_raw.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)