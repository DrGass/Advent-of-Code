import csv

column1, column2 = [], []
for column in csv.reader(open("1_input.txt"), delimiter=" "):
    if len(column) > 1:
        column1.append(int(column[0]))
        column2.append(int(column[3]))
column1.sort()
column2.sort()

values = []
for i in range(len(column1)):
    values.append(abs(column1[i] - column2[i]))

print(sum(values))
