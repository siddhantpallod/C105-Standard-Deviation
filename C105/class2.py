import csv
import pandas
import plotly.express as px

with open('class2.csv', newline = '') as a:
    readData = csv.reader(a)
    newData = list(readData)

newData.pop(0)

totalMarks = 0
totalEntries = len(newData)

for marks in newData:
    totalMarks += float(marks[1])

mean = totalMarks/totalEntries

print("Mean is ",mean)

df = pandas.read_csv('class2.csv')
fig = px.scatter(df, x = 'Student Number', y = 'Marks')

fig.show()