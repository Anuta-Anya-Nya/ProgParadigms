arr = [1, 5, 3, 8, 0, 7]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(arr1, arr2):
    result = []
    index_left = 0
    index_right = 0
    while len(arr1) > index_left and len(arr2) > index_right:
        if arr1[index_left] <= arr2[index_right]:
            result.append(arr1[index_left])
            index_left += 1
        else:
            result.append(arr2[index_right])
            index_right += 1
    while len(arr1) > index_left:
        result.append(arr1[index_left])
        index_left += 1
    while len(arr2) > index_right:
        result.append(arr2[index_right])
        index_right += 1
    return result
# def merge(arr1, arr2):
#     result = []

#     while(len(arr1)>0):
#         if arr1[0]<=arr2[0]:
#             result.append(arr1[0])
#             arr1.remove(arr1[0])
#         else:
#             result.append(arr2[0])
#             arr2.remove(arr2[0])
#     if(len(arr2)>0):
#         result.extend(arr2)
#     return result


# print(merge([2, 0, 89], [1,7]))
print(merge_sort(arr))
