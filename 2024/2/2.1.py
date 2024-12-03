import csv

sum_of_valid = 0

for row in csv.reader(open("2_input.txt"), delimiter=" "):
    numbers = [int(x) for x in row]
    inc_or_dec = numbers == sorted(numbers) or numbers == sorted(numbers, reverse=True)
    ok = True
    for i in range(len(numbers) - 1):
        difference = abs(numbers[i] - numbers[i + 1])
        if not 1 <= difference <= 3:
            ok = False
    if inc_or_dec and ok:
        sum_of_valid += 1

print(sum_of_valid)
