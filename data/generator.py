"""
Generator for fake data points used to train and test
implementation for model
"""

import csv
import random
import string

"""
Methods for getting data written into a csv
"""

def readFromLocations():
    with open('locations.csv', mode='r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            print(row)


def appendIntoCSV(item: [str]):
    locations = []
    with open('locations.csv', mode='r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            locations = row
            break  # workaround since it is appending 2 empty rows below

    with open('locations.csv', mode='w') as f:
        locations += item
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(locations)


def writeIntoCSV(item: [str]):
    with open('locations.csv', mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(item)


"""
Generator functions
"""


def getDaysOfTheWeek(n: int, start_day: int = 0):
    """

    :param n: n number of days
    :param start_day: starting day, monday being 0
    :return: list of size n with repeating days
    """
    l = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    returnlist = []
    for i in range(start_day, n + start_day, 1):
        returnlist.append(l[i % 7])  # 0 - 6 only
    return returnlist


def generateRandomData(groups: int = 5, datapoints: int = 7, start_day: int = 0):
    """
    Generates random data and puts it into locations.csv
    2 groups set as default since 1 group will be on weekends and 1 on weekdays
    7 default
    starts from monday @ day 0
    :return: array of locations
    """
    choices = []
    for i in range(groups):
        choices.append(''.join(random.choice(string.ascii_letters) for j in range(6)))

    writeIntoCSV(choices)

    returnlist = []
    for i in range(start_day, datapoints + start_day, 1):
        day = i % 7
        if day != 5 and day != 6:  # use weekday choice
            returnlist.append(random.choice(choices[:2]))
        else:
            returnlist.append(random.choice(choices[2:]))

    return returnlist


def genWithProbOf(weekday_probs=[0.7, 0.2, 0.1], weekend_probs=[1.0], datapoints=12, start_day=0):
    total_datapoints = len(weekday_probs) + len(weekend_probs)
    choices = []
    for i in range(total_datapoints):
        choices.append(''.join(random.choice(string.ascii_letters) for j in range(6)))

    print('generated location choices:', choices)

    returnlist = []
    for i in range(start_day, datapoints + start_day, 1):
        day = i % 7
        if day != 5 and day != 6:  # use weekday choice
            returnlist += random.choices(choices[:len(weekday_probs)], weights=weekday_probs)
        else:
            returnlist += random.choices(choices[-len(weekend_probs):], weights=weekend_probs)
    return returnlist


def EncodeDaysToOneHotVector(days: [str]):
    l = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_vectors = []
    for d in days:
        new_day_vector = [0] * 7
        new_day_vector[l.index(d)] = 1
        day_vectors.append(new_day_vector)
    return day_vectors


def EncodeLocationsToGroups(locations: [str]):
    unique_locations = list(set(locations))
    loc_vectors = []
    for single_loc in locations:
        loc_vectors.append(unique_locations.index(single_loc))

    return loc_vectors


def showGeneratedExample(num_days=5, num_groups=12):
    generated_days = getDaysOfTheWeek(num_days)
    generated_locations = generateRandomData(groups=num_groups, datapoints=num_days)
    print("days:", generated_days)
    print("locs:", generated_locations)

    # convert
    day_vectors = EncodeDaysToOneHotVector(generated_days)
    print("days vector form:", day_vectors)

    loc_numbers = EncodeLocationsToGroups(generated_locations)
    print("locs vector form:", loc_numbers)


# showGeneratedExample(12)