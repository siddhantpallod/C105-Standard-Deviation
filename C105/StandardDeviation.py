import csv
import math

with open('data.csv', newline = '') as a:
    readData = csv.reader(a)
    newData = list(readData)

# newData.pop(0)
data = newData[0]

def mean(data):
    l = len(data)
    total = 0

    for b in data:
        total += int(b)

    mean = total/l
    return mean

squaredList = []

for a in data:
    number = int(a) - mean(data)
    number = number**2
    squaredList.append(number)

totalSum = 0

for c in squaredList:
    totalSum = totalSum + c

result = totalSum / (len(data) - 1)

standardDeviation = math.sqrt(result)

print(standardDeviation)