myList = [1, 2, 3, 4, 5]
myList2 = [6, 7, 8, 9, 10]
myList3 = [a*b for a,b in zip(myList, myList2)] 

print(myList3)