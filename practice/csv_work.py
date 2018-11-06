import csv
import os

print(os.getcwd())

path = os.path.dirname(__file__)
os.chdir(path)
print(os.getcwd())

filename = 'sitka_weather_07-2014.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    highs = []
    for row in reader:
        highs.append(int(row[1]))

    print(highs)

for index, column_header in enumerate(header_row):
    print(index, column_header)
