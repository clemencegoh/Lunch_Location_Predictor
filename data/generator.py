"""
Generator for fake data points used to train and test
implementation for model
"""

import csv
import random
import string


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


print(getDaysOfTheWeek(28))
print(generateRandomData(groups=12, datapoints=28))
