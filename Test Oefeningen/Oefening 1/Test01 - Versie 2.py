import random

def print_explanation():
    print("U zal gevraagd worden om de 2 gebruikte talen in te geven.")
    print("U zal ook gevraagd worden om het aantal woorden in te geven.")
    print("Hierna zal een woord gevraagd worden in de eerste taal")
    print("Daarna zal een woord gevraagd worden in de tweede taal.")
    print("Dit zal zich blijven herhalen tot het aantal woorden bereikt is.")
    print("Na het ingeven zal de applicatie een woord van de eerste taal vragen.")
    print("De gebruiker moet dan de correcte vertaling ingeven.")
    print("U zal dan het resultaat te zien krijgen van uw ingave.")
    print("Voer 'stop programma' in op eender welk moment om het programma te stoppen.")

def print_line():
    print("-" * 10)

def is_word_already_used(word_to_check, word_combinations):
    for word_combination in word_combinations:
        word = word_combination[0]
        if word == word_to_check:
            return True

    return False

def check_input(question = ''):
    input_result = input(question)
    if input_result == "stop programma":
        print_line()
        exit()
    return input_result

words_first_language = []
words_second_language = []

print_line()
print_explanation()
print_line()
first_language = check_input("Wat is de eerste taal? ")
second_language = check_input("Wat is de tweede taal? ")
n_words = int(check_input("Hoeveel woorden zal u ingeven? "))
for i in range(n_words):
    word = check_input("Wat is woord nummer " + str(i + 1) + " in het " + first_language + "? ")
    while word in words_first_language:
        word = check_input("Wat is woord nummer " + str(i + 1) + " in het " + first_language + "? ")
    translation = check_input("Wat is woord nummer " + str(i + 1) + " in het " + second_language + "? ")
    words_first_language.append(word)
    words_second_language.append(translation)

print_line()

while True:
    random_number = random.randint(0, (len(words_first_language) - 1))
    word = words_first_language[random_number]
    answer = check_input("Wat is '" + word + "'? ")
    if answer == words_second_language[random_number]:
        print("Correct!")
    else:
        print("Fout, " + word + " is '" + words_second_language[random_number] + "'.")