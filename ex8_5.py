import random

quantity = 2
participants = {
    "603d2cec9993c627f0982404": "test@test.com",
    "603f79022922882d30dd7bb6": "test11@test.com",
    "60577ce4b536f8259cc225d2": "test2@test.com",
    "605884760742316c07eae603": "vitanlhouse@gmail.com",
    "605b89080c318d66862db390": "elhe2013@gmail.com",
}
#print(len(participants))

def get_random_winners(quantity, participants):
    winner_list = []
    participants_list = []
    if quantity > len(participants):
        return []
    else:
        for key in participants:
            participants_list.append(key)
    random.shuffle(participants_list)
    winner_list = random.sample(participants_list, k=quantity)
    return winner_list

print(get_random_winners(quantity, participants))