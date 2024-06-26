alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift % 26
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for letter in start_text:
    if letter not in alphabet:
      end_text += letter
    else:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
  print(f"The {cipher_direction}d text is: {end_text}")

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
restart = input("Would you like to go again? Type 'yes' if you would like to go again. Otherwise type 'no'.").lower()
while restart == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  restart = input("Would you like to go again? Type 'yes' if you would like to go again. Otherwise type 'no'.").lower()

if restart == "no":
  print("Goodbye")
