from random import randrange

min = 1
max = 10
quantity = 5

def get_numbers_ticket(min, max, quantity):
    result_list = []
    if min < 1 or max > 1000 or not  min < quantity < max:
        return []
    else:
        i = 0
        while i < quantity:
            new_number = randrange(min, (max+1))
            if new_number not in result_list:
                result_list.append(new_number)
                i += 1
            else:
                continue
    return sorted(result_list)

print(get_numbers_ticket(min, max, quantity))