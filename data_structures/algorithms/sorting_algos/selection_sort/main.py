def selection_sort(lst):
    for i in range(len(lst)):
        min = i

        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min]:
                min = j

        temp = lst[min]
        lst[min] = lst[i]
        lst[i] = temp

    return lst

lst = [7, 5, 8, 6, 2]
print(selection_sort(lst))



