# Baby Names - Seperate Boy and Girl

import sys

data = sys.argv[1]

text = open(data, 'r').readlines()

males = ""
females = ""

for i in text:
    name, gender, id = i.split(',')
    if "M" in gender:
        males += name + "\n"
    elif 'F' in gender:
        females += name + "\n"

girls = open('girls.txt', 'w')
boys = open('boys.txt', 'w')

girls.write(females)
boys.write(males)

total = len(males) + len(females)
boy_percent = len(males) / total
girl_percent = len(females) / total

print("Boys: " , str(boy_percent)[2:4], " percent")
print("Girls: " , str(girl_percent)[2:4], " percent")