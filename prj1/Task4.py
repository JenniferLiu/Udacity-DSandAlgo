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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def get_numbers(records, col):
    numbers = []
    for r in records:
        if r[col] not in numbers:
            numbers.append(r[col])
    return numbers


def get_telemarket_numbers(texts, calls):
    calls0 = get_numbers(calls, 0)
    calls1 = get_numbers(calls, 1)
    texts0 = get_numbers(texts, 0)
    texts1 = get_numbers(texts, 1)
    nums = list(set(calls0) - set(calls1) - set(texts0) - set(texts1))
    print("These numbers could be telemarketers: ")
    for n in sorted(nums):
        print(n)


get_telemarket_numbers(texts, calls)
