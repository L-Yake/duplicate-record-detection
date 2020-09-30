import csv
import time


# Search both dictionaries for duplicate entries
def duplicate_check(key, title=False):
    """

    :param key: Accepts a dictionary key as a field for searching duplicates. (Ex. ['name', 'email', etc.]
    :param title: Accepts a string as a title and creates a new CSV-file. Recommended format: organization-abbreviation_YYYY-MM-DD.csv
    :return: Returns list of duplicate entries and number of duplicate entries found.
    """
    # Searches collection of 1000 currently enrolled members
    with open(r'current_members/current_members20203009.csv', mode='r') as member_file:
        current_members = csv.DictReader(member_file)
        current_members_list = list(current_members)

        # Collection of newly registered members
        with open(r'new_members/new_members_09-20-2020.csv', mode='r') as new_member_file:
            new_members = csv.DictReader(new_member_file, fieldnames=current_members.fieldnames)
            new_members_list = list(new_members)

            # Search each list of members for duplicate entries
            duplicates = [
                member
                for member in current_members_list
                for enrolled in new_members_list
                if member[key] == enrolled[key]
                ]

            # print(*duplicates, sep='\n')
            print(f'Number of duplicates found: {len(duplicates)}')

            # If the user declares a title, a new CSV will be created using the given title.
            if title:
                with open(f'new_members/{title}.csv', mode='w', newline='') as duplicates_file:
                    writer = csv.DictWriter(duplicates_file, fieldnames=current_members.fieldnames)
                    writer.writerows(duplicates)
                    time.sleep(1)
                    print('New file created!')


# duplicate_check('name', "ORG-ABBV_date")
