import sys
import re

a = []
pattern = r"\ba+\b"
for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(pattern, "argh", line, count=1, flags=re.IGNORECASE)
    print(line)
for i in a:
    print(i)