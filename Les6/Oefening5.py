list_of_numbers = [0,0]


def find_upper_or_lower(string):   
    for i in string:
        if i.isupper():
            list_of_numbers[0] += 1
        if i.islower():
            list_of_numbers[1] += 1
    return list_of_numbers

user_input = input("Geef een wachtwoord (minstens 2 hoofdletters en minstens 3 kleine letters) ")
find_upper_or_lower(user_input)

while list_of_numbers[0] < 2 or list_of_numbers[1] < 3:
    list_of_numbers = [0,0]
    user_input = input("Geef een wachtwoord (minstens 2 hoofdletters en minstens 3 kleine letters) ")
    find_upper_or_lower(user_input)

        




