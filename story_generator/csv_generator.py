import csv

# Lists with 20 entries each
when = [
    'A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th Jan',
    'This morning', 'Last summer', 'Two days ago', 'Last week', 'This evening',
    'On New Year\'s Eve', 'During the holidays', 'In the afternoon', 'Early this year',
    'At midnight', 'On my birthday', 'In spring', 'In autumn', 'On Christmas Eve', 'This weekend'
]

who = [
    'a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat',
    'a lion', 'a penguin', 'a dog', 'a fox', 'a bear',
    'a snake', 'a horse', 'a frog', 'an owl', 'a goat',
    'a kangaroo', 'a giraffe', 'a monkey', 'a deer', 'a wolf'
]

name = [
    'Ali', 'Miriam', 'Daniel', 'Hoouk', 'Starwalker',
    'Luna', 'Kai', 'Ella', 'Zane', 'Nova',
    'Leo', 'Sasha', 'Jade', 'Ravi', 'Nina',
    'Omar', 'Tara', 'Yuna', 'Hugo', 'Bea'
]

residence = [
    'Barcelona', 'India', 'Germany', 'Venice', 'England',
    'Tokyo', 'New York', 'Madrid', 'Cape Town', 'Paris',
    'Cairo', 'Toronto', 'Dublin', 'Rome', 'Sydney',
    'Amsterdam', 'Dubai', 'Seoul', 'Beijing', 'Istanbul'
]

went = [
    'cinema', 'university', 'seminar', 'school', 'laundry',
    'museum', 'concert', 'park', 'market', 'library',
    'zoo', 'cafe', 'theater', 'restaurant', 'aquarium',
    'garden', 'mall', 'stadium', 'art gallery', 'beach'
]

happened = [
    'made a lot of friends', 'ate a burger', 'found a secret key', 'solved a mystery', 'wrote a book',
    'danced in the rain', 'discovered a treasure', 'met a stranger', 'learned something new', 'sang a song',
    'built a robot', 'won a prize', 'helped someone', 'lost a hat', 'saw a ghost',
    'painted a picture', 'learned to juggle', 'saved a kitten', 'got a surprise', 'baked cookies'
]

# Combine data
rows = zip(when, who, name, residence, went, happened)

# Write to CSV
with open('story_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['When', 'Who', 'Name', 'Residence', 'Went', 'Happened'])
    writer.writerows(rows)

print("✅ 'story_data.csv' with 20 entries created successfully.")
