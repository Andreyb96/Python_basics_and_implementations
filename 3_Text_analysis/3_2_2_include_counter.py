s = input()
t = input()
k = 0
for i in range(len(s)):
    if s[i:].startswith(t):
        k += 1
print(k)