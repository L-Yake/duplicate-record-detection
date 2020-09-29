import random
import csv


member_list = []
with open(r'current_members/current_members.csv', mode='r') as csv_file:
    reader = csv.DictReader(csv_file)

    # Skips row containing field names ['index', 'name', etc...]
    # next(reader), unnecessary for now but neat!

    for line in reader:
        member_list.append(line)

    # Creates a csv file containing dummy personal information of people who registered twice by accident
    twice_enrolled = random.choices(member_list, k=10)
    with open('new_members/twice_enrolled.csv', mode='w', newline='') as new_file:
        writer = csv.DictWriter(new_file, fieldnames=reader.fieldnames)
        writer.writerows(twice_enrolled)



