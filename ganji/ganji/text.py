import re
with open('urls.txt', 'r') as f:
    line = f.read().strip()
    result = re.split(r"[\n]", line)
print(result)