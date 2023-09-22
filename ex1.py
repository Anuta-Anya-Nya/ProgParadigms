arr = [1, 2, 3, 4, 5]
target = 3
def myFunc(arr, target):
    for item in arr:
        if(item==target):
            return True
    return False


print(myFunc(arr, target))