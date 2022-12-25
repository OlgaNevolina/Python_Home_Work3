# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётных позициях(не индексах).

from random import sample


def list_rand_nums(count: int):
    if count < 0:
        print("Отрицательное значение!")
        return[]
    list_nums = sample(range(1, count*2), count)  
    return list_nums

def sum(list_nums: list):
    sum_nums = 0
    for p in range(0, len(list_nums), 2):
        sum_nums += list_nums[p]
    return sum_nums

my_list = list_rand_nums(int(input("Введите количество чисел в списке: ")))   
print(my_list) 
print(sum(my_list))          