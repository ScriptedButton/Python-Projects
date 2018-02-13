import sys

letters = []
frequencies = {}

file = sys.argv[1]

file_text = open(file, 'r').read()

counter = 0
for i in file_text:
    if i.isalpha():
        letters.append(i.upper())
        letters.sort()
        frequencies[i.upper()] = 0
        counter += 1

for i in letters:
    frequencies[i.upper()] += 1

total = 0
for i in frequencies:
    total += frequencies[i.upper()]

sortedvalues = sorted(frequencies.keys(), key=lambda x:x.lower())
for i in sortedvalues:
    frequency = str(frequencies[i] / total)[2:4]
    if int(frequency) < 1:
        frequency = "<1"
    print(i + " : " + frequency + "%")
highest = max(frequencies, key=frequencies.get)
lowest = min(frequencies, key=frequencies.get)
print("Most frequent: " + highest)
print("Least frequent: " + lowest)
