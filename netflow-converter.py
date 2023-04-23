import csv
from datetime import datetime


# Open the CSV file
with open('urg16-raw.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

time_index = rows[0].index('ts')
initial_index = rows[0].index('srcip')
type_index = rows[0].index('type')
proto_index = rows[0].index('proto')

count = 0

rows = rows[:14240]

for i, row in enumerate(rows):
    count += 1
    converted = ''
    if i == 0: 
        converted = 'date'
    else: 
        unix_timestamp = int(float(row[time_index]) / 1000000)
        converted = datetime.utcfromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')
        row[proto_index] = 0
        
    row[time_index], row[initial_index] =row[initial_index], converted
    
    del row[type_index] # delete all same values coloumn or string instead of integer values 
    del row[proto_index] # delete all same values coloumn or string instead of integer values 

print("count: ", count)

# Write the updated rows to a new CSV file
with open('updated_urg16.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)