"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
from collections import defaultdict

numbers = defaultdict(lambda: 0)
for c in calls:
    numbers[c[0]] += int(c[3])
    numbers[c[1]] += int(c[3])

sorted_numbers = sorted(numbers.items(), key=lambda x: x[1], reverse=True)

print(
    "{} spent the longest time, {} seconds, on the phone during September 2016.".format(
        sorted_numbers[0][0], sorted_numbers[0][1]
    )
)
