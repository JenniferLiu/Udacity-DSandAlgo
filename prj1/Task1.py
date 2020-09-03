"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def get_numbers(records, numbers=[]):
    for t in records:
        for i in range(2):
            if t[i] not in numbers:
                numbers.append(t[i])
    return numbers


def count_numbers():
    numbers = get_numbers(texts)
    numbers = get_numbers(calls, numbers)
    print(
        "There are {} different telephone numbers in the records.".format(len(numbers))
    )


count_numbers()

