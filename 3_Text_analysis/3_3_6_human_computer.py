import sys
import re

a = []
pattern = r"human"
for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(pattern, 'computer', line)
    print(line)
for i in a:
    print(i)