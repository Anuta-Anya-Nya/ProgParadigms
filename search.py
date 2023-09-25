print("Task 2")
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]


def mse(arr1, arr2):
    if len(arr1) == len(arr2):
        return sum(map(lambda x, y: (x-y)**2, arr1, arr2))/len(arr1)
    else:
        return -1


print(mse(arr1, arr2))

print()

print("Task 3")

arr4 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
n = 2
i_min = 0
i_max = len(arr4)-1


def search(arr, n, i_min, i_max):

    if i_min > i_max:
        return -1   
    mid = (i_max + i_min) // 2
    if arr[mid] == n:
        return mid
    elif arr[mid] > n:
        return search(arr, n, i_min, mid-1)
    elif arr[mid] < n:
        return search(arr, n, mid+1, i_max)



print(search(arr4, n, i_min, i_max))