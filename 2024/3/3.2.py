import re

with open("3_input.txt", "r") as file:
    content = file.read()

ans = 0
initial_pattern = r"do\(\).*?don't\(\)"
content = content.replace("\n", "")
content = content.replace(" ", "")
print(content)
matches2 = re.findall(initial_pattern, content)
pattern = r"mul\([0-9]+,[0-9]+\)"
matches2 = "".join(matches2)
matches = re.findall(pattern, matches2)
print(matches, len(matches))
for match in matches:
    match = match.replace("mul", "")
    match = match.replace("(", "")
    match = match.replace(")", "")
    index = match.find(",")
    ans += int(match[:index]) * int(match[index + 1 :])
print(ans)

# 50272739 without first do
# 57487139 with first do
# 57487139 after changes
# 88802350 Should be the correct answer
# 86056442 Somehow? XD
