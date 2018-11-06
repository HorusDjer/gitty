import os, csv, time

path = os.path.dirname(__file__)

os.chdir(path)

# t0 = time.time()

with open('volunteer.csv', 'r') as file_object:
    reader = csv.reader(file_object)
    headers = next(reader)
    count = 0
    for row in reader:
        count = count + 1

import csv

with open('volunteer.csv', 'r') as file_object:
    reader = csv.reader(file_object)

    count = 0
    for row in reader:
        count = count + 1

print(count)


import csv

with open('volunteer.csv', 'r') as volunteer_file:
    csv_reader = csv.DictReader(volunteer_file)

    totalPeople = 0
    for row in csv_reader:
        totalPeople = totalPeople + 1

print(totalPeople)

print(headers)

print(count)

"""with open('volunteer.csv', 'r') as file_object:
    row_count = sum(1 for line in csv.reader(file_object))
print('Elapsed time : ', time.time() - t0)
print(row_count)"""

with open('volunteer.csv', 'r', newline='') as file_object:
    reader = csv.DictReader(file_object)
    headers = next(reader)
    
    count = 0
    volunteers = 0
    donors = 0
    for row in reader:
        if row['Volunteer'].lower() == 'yes':
            print(row[1:9])
            volunteers += 1
        if row['Donor'].lower() == 'yes':
            donors += 1
        count = count + 1


print("Number of volunteer:", volunteers, "\nNumber of donors:", donors)

import csv

with open('volunteer.csv', 'r') as file_object:
    reader = csv.DictReader(file_object)

    count = 0
    totalVolunteers = 0
    totalDonors = 0
    for row in reader:
        count = count + 1
        if row["Volunteer"] == "Yes":
                totalVolunteers = totalVolunteers + 1
        if row["Donor"] == "Yes":
                totalDonors = totalDonors + 1

print(count, totalDonors, totalVolunteers)

person = {
    "EID": 2907071,
    "Last Name": "Colvin", 
    "First Name": "Claudette",
    "Address": "588 Example St.",
    "City": "Montgomery",  
    "State": "AL",
    "Zip5": 36108,
    "Email 1": "claudette.colvin43@example.com",
    "Email 2": "",
    "Phone 1": "3342423935",
    "Phone 2": "3345555934",
    "Volunteer": True,
    "Precinct Captain": True
    }
