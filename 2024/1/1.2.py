import csv
import pprint

column1, column2 = [], []
for column in csv.reader(open("1_input.txt"), delimiter=" "):
    if len(column) > 1:
        column1.append(int(column[0]))
        column2.append(int(column[3]))
column1.sort()
column2.sort()

values = {}
for i in range(len(column1)):
    if column1[i] not in values:
        values[column1[i]] = 1
    else:
        values[column1[i]] += 1

values2 = {}
for i in range(len(column2)):
    if column2[i] not in values2:
        values2[column2[i]] = 1
    else:
        values2[column2[i]] += 1

values2.get(95229)

sum = 0
for key, value in values.items():
    if values2.get(key) is not None:
        sum += key * value * values2.get(key)

    print(f"key: {key}, value: {value}, value2: {values2.get(key)}, sum: {sum}")

# if column1[i] in values:
# else:
#     sum += 0

print(sum)
