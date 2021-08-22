list = [12, 15, 18, 20, 25, 30, 36, 48]

print(list)

n = int(input('Enter the item that you want to search: '))

pos = -1


def search(list, n):
    lb = 0
    ub = len(list)-1
    
    while lb<=ub:
        mid=(lb+ub)//2
        if list[mid] == n:
            globals() ['pos'] = mid
            return True
        elif list[mid] < n:
            lb = mid
        else:
            ub = mid
            
    

if search(list, n):
    print("Item found at " + str(pos) + '.')
    
else:
    print("Item is not there in the list.")


            
            
            
            
            
            
            
