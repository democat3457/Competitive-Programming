import re
line = input()
print(max(len(x.group(1)) for x in re.finditer("(u+)", line)))