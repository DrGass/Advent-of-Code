import re

with open("3_input.txt", "r") as file:
    content = file.read()

ans = 0
enabled = True
pattern = r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)"
matches = re.findall(pattern, content)
for match in matches:
    if "do()" in match:
        print("enabled", match)
        enabled = True
    elif "don't()" in match:
        print("disabled", match)
        enabled = False
    elif enabled:
        print("Summing", match)
        match = match.replace("mul", "")
        match = match.replace("(", "")
        match = match.replace(")", "")
        index = match.find(",")
        ans += int(match[:index]) * int(match[index + 1 :])
    else:
        print("Skipping", match)
print(ans)

# ans = 0
# initial_pattern = r"do\(\).*?don't\(\)"
# content = content.replace("\n", "")
# content = content.replace(" ", "")
# print(content)
# matches2 = re.findall(initial_pattern, content)
# pattern = r"mul\([0-9]+,[0-9]+\)"
# matches2 = "".join(matches2)
# matches = re.findall(pattern, matches2)
# print(matches, len(matches))
# for match in matches:
#     match = match.replace("mul", "")
#     match = match.replace("(", "")
#     match = match.replace(")", "")
#     index = match.find(",")
#     ans += int(match[:index]z) * int(match[index + 1 :])
# print(ans)

# 50272739 without first do
# 57487139 with first do
# 57487139 after changes
# 88802350 Should be the correct answer
# 86056442 Somehow? XD
