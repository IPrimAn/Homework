List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0
for i in range(0, len(List), 2):
   index = index + List[i]
print(index * List[-1])
