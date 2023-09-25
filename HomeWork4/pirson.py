from functools import reduce
import math

x = [1, 2, 3, 4]
y = [10, 20, 29, 82]

#среднее
def average(arr):
    sum_all = reduce(lambda x,y: x + y, arr)
    return sum_all / len(arr) 

#разница между значением и средним
def diff_average(arr):
    average_number=average(arr);
    return list(map(lambda x: x - average_number, arr)) 

#произведение соответствующих значений
def multipl(arr1, arr2):
    return list(map(lambda x,y: x * y, arr1, arr2)) 

#суммирование элементов массива
def summ_elem(arr):
    return reduce(lambda x,y: x + y, arr)

#произведение суммы элементов квадратов значений 
def multipl_square(arr1, arr2):
    arr_x = list(map(lambda x: x**2, arr1))
    arr_y = list(map(lambda x: x**2, arr2))
    return summ_elem(arr_x) * summ_elem(arr_y) 


def pirson(arr1, arr2): 
    diff_average_x = diff_average(x)
    diff_average_y = diff_average(y)
    return summ_elem(multipl(diff_average_x, diff_average_y)) / math.sqrt(multipl_square(diff_average_x, diff_average_y))


print(pirson(x, y))