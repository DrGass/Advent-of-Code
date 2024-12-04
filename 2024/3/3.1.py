import re

with open("3_input.txt", "r") as file:
    content = file.read()

ans = 0
pattern = r"mul\([0-9]+,[0-9]+\)"
matches = re.findall(pattern, content)
for match in matches:
    match = match.replace("mul", "")
    match = match.replace("(", "")
    match = match.replace(")", "")
    index = match.find(",")
    print(match[:index], " ", match[index + 1 :], ans)
    ans += int(match[:index]) * int(match[index + 1 :])
print(ans)
