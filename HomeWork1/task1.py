def sort_list_imperative(numbers):
    # императивный стиль
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-i-1):
            if numbers[j] < numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
    return numbers

list=[4, 1, 0, 9, 3]
print(sort_list_imperative(list))