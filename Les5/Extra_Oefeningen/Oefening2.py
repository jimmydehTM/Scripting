start = ord('a')
alphabet = []
encryption = []
list_of_upper = []

# put the alfabeth in an array
for i in range(26):
    alphabet.append((chr(start+i)))

# Get user inputs
text = input("Give a text to cypher: ")
number = input("Give a ROT number: ")

#check if number input is an integer and positive, if not request new input
while number.isdigit() is False or int(number) < 0:
     number = (input('Give a ROT number: '))

#convert input to an integer
rot = int(number)

# check for spaces and replace with '#'
for x in text:
    text_without_spaces = text.replace(' ', '#')

# Make list of user text input
text_list = list(text_without_spaces)


# Look for upper case characters, save index of them in a list
for i in range(len(text_list)):
     if text_list[i].isupper():
        list_of_upper.append(i) 
        text_list[i] = text_list[i].lower()


# Look for spaces and append them to the encrypted list
for i in text_list:
        if i == '#':
             encryption.append(i)
             # Look what character in the alphabet corresponds with the input string, then add the rot number
        elif i in alphabet:
            number = alphabet.index(i)+rot
            # If the alphabet number + rot number is greater then list, do modulo 26 on rot number
            if number >= 25:
                 number = (number % 26)
            # Add the rotated letters to the encryption list
            encryption.append(alphabet[number])

# If there are uppercase characters, make the corresponding encrypted characters also uppercase
if len(list_of_upper) > 0:
     for i in list_of_upper:
          for x in range(len(encryption)):
              if i == x:
                   encryption[i] = encryption[i].upper()
        
          
# Print the encrypted string          
encryption = ''.join(encryption)
print(encryption)
