from decimal import Decimal, getcontext

number_list1 = [3, 5, 77, 23, 0.57]
number_list2 = [31, 55, 177, 2300, 1.57]


def decimal_average(number_list, signs_count):
    sum = 0
    avg = 0
    getcontext().prec = signs_count
    for number in number_list:
        sum += Decimal(number)
    avg = Decimal(sum)/len(number_list)
    return avg
    

print(decimal_average(number_list1, 6))# поверне 21.714
print(decimal_average(number_list2, 9))# поверне 512.91400