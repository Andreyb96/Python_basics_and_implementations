import sys
import re

a = []
pattern = r"\\"
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line)!=None:
        print(line)
for i in a:
    print(i)