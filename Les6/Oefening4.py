import random

random_list = []
number_of_throws = 0

def randomList(length, lower, upper): 
    for i in range(length):
        number = random.randrange(lower, upper)
        random_list.append(number)
    return random_list


def filter_list(input_list):
    return set(input_list)

user_input = input("Hoeveel worpen wil je doen? ")

while user_input != '':
    int(user_input)
    number_of_throws += 1
    uitslag = randomList(int(user_input),1,6)
    if len(filter_list(random_list)) == 1:
        print('Je gooide {}'.format(uitslag))
        print("Je gooide JOKER na {} keer gooien!".format(number_of_throws))
    else: print('Je gooide {}'.format(uitslag))

    random_list = []
    user_input = input("Hoeveel worpen wil je doen? ")
    

    