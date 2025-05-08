import csv
import random
# Initialize empty lists
when = []
who = []
name = []
residence = []
went = []
happened = []

# Read CSV file
with open('story_data.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        when.append(row[0].capitalize())
        who.append(row[1])
        name.append(row[2])
        residence.append(row[3])
        went.append(row[4])
        happened.append(row[5])

for i in range(1,7):
    print (f'{i}. {random.choice(when)},{random.choice(who)} that lived in {random.choice(residence)}, went to the {random.choice(went)} and  {random.choice(happened)}.')
       