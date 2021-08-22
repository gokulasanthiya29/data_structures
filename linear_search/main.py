list = [122, 346, 635, 749, 861, 28, 24, 29, 1977, 2000, 2010]

pos = -1

n = int(input("Enter the item which you're searching for: "))

def search(list, n):
    
    for i in range(len(list)):
        if list[i] == n:
            globals() ['pos'] = i
            return True
    return False

if search(list, n):
    print("Item found. It's at the index," + str(pos) + '.')
    
    
else:
    print("not found")
    