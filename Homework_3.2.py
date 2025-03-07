List = [1,2,3,4,5]
count_list = len(List)
if count_list == 0:
    print([])
elif count_list == 1:
    print(List[0])
else:
    last_num = List.pop(-1)
    List.insert(0, last_num)
    print(List)

