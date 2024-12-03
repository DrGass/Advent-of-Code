import csv

sum_of_valid = 0

for row in csv.reader(open("2_input.txt"), delimiter=" "):
    numbers_2 = [int(x) for x in row]
    good = False
    for i in range(len(numbers_2)):
        numbers = numbers_2[:i] + numbers_2[i + 1 :]
        print(numbers, " ", numbers_2)
        inc_or_dec = numbers == sorted(numbers) or numbers == sorted(
            numbers, reverse=True
        )
        ok = True
        for j in range(len(numbers) - 1):
            difference = abs(numbers[j] - numbers[j + 1])
            if not 1 <= difference <= 3:
                ok = False
        if inc_or_dec and ok:
            good = True
    if good:
        sum_of_valid += 1

print(sum_of_valid)
