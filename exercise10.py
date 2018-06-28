a = [[1,2], [3,4], [9,10]]
b = [[5,6], [7,8], [11,12]]

c = [sum(a + b) for a, b in zip(a, b)]


print(c)