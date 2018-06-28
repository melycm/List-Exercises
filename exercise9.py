
a = [[1,2], [3,4]]
b = [[5,6], [7,8]]

c = [sum(a + b) for a, b in zip(a, b)]


print(c)