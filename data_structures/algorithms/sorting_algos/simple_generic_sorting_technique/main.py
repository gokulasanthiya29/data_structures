#Ascending Order Sort
def generic_sort(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[j] < lst[i]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
        i+=1
    return lst

lst = [2,1,6,5,0,8,12,10]
print(generic_sort(lst))


# Descending Order Sort
'''
def generic_sort(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            # line of change
            if lst[j] > lst[i]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
        # line of change
        i-=1
    return lst

lst = [2,1,6,5,0,8,12,10]
print(generic_sort(lst))
'''


