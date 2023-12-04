# Import external libraries
import random

# User explenation how the program works
print("U zal gevraagd worden om de 2 gebruikte talen in te geven." )
print("U zal ook gevraagd worden om het aantal woorden in te geven.")
print("Hierna zal een woord gevraagd worden in de eerste taal")
print("Daarna zal een woord gevraagd worden in de tweede taal.")
print("Dit zal zich blijven herhalen tot het aantal woorden bereikt is.")
print("Na het ingeven zal de applicatie een woord van de eerste taal vragen.")
print("De gebruiker moet dan de correcte vertaling ingeven.")
print("U zal dan het resultaat te zien krijgen van uw ingave.") 
print("Voer 'stop programma' in op eender welk moment om het programma te stoppen.")


# Function to check for stopping command
def check_to_stop_program(question):
        user_input = input(question)
        if user_input == 'stop programma':
                print_lines()
                exit()
        return user_input

# Function to print breakmark lines
def print_lines():
        print("----------")

# Initializing variables
# Initilaizing two lists to store user input
first_language_list = []
second_language_list = []


# User input variables
first_language = ''
second_language = ''
n_words = 0
word_first_language_list = ''
word_second_language_list = ''

# Program
print_lines()
first_language = check_to_stop_program('Wat is de eerste taal? ')
second_language = check_to_stop_program('Wat is de tweede taal? ')
n_words = int(check_to_stop_program('Hoeveel woorden zal u ingeven? '))

for i in range(n_words):
        word_first_language_list = check_to_stop_program('Wat is woord nummer {} in het {}? '.format(i+1, first_language))
        while word_first_language_list in first_language_list:
                word_first_language_list = check_to_stop_program('Wat is woord nummer {} in het {}? '.format(i+1, first_language))
        first_language_list.append(word_first_language_list)
        word_second_language_list = check_to_stop_program('Wat is woord nummer {} in het {}? '.format(i+1, second_language))
        second_language_list.append(word_second_language_list)

print_lines()

while True:
        random_rumber = random.randint(0,(len(first_language_list)-1))
        answer = check_to_stop_program("Wat is '{}'? ". format(first_language_list[random_rumber]))
        if answer == second_language_list[random_rumber]:
                print('Correct!')       
        else:
                print("Fout, {} is '{}'.".format(first_language_list[random_rumber], second_language_list[random_rumber]))

