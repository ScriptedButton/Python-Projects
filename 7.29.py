import sys

file = sys.argv[1]

services = {}

file = open(file, 'r')
file_text = file.readlines()

for i in file_text:
    name, service, price, date = i.split(";")
    print("Name: " + name)
    print("Service: " + service)
    if not service in services:
        services[service] = int(price)
    else:
        services[service] += int(price)
    print("Price: " + price)
    print("Date: " + date)
    print("--")

print("-- Price Summary --")
for i in services:
    print(i + ": " + "$" + str(services[i]))