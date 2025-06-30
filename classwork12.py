import csv

import faker
from faker import Faker
import random


fake = faker.Faker()

headers = ['ID', 'name', 'surname', 'age']

with open('classwork.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    for _ in range(50):

        writer.writerow([_+1, fake.first_name(), fake.last_name(), random.randint(20,80)])



