import sys
import re

a = []
pattern = r".*cat.*cat.*"
for line in sys.stdin:
    line = line.rstrip()
    if re.match(pattern, line)!=None:
        a.append(line)
for i in a:
    print(i)
