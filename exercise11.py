t = [1, 2, 3, 3, 2, 5, 6, 7, 8, 5]
s = []
for i in t:
    if i not in s:
        s.append(i)

print(s)