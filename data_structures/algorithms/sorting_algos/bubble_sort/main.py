def bubble_sort(lst):
    for i in range(len(lst) - 1, 0 , -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp

    return lst

lst = [5,6,3,8,2,0]
print(bubble_sort(lst))






