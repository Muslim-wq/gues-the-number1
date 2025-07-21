import random

while True:
 secret_number = random.randint(1, 5)
 user_input= input("Gues the Number 1 to 10: ")

 if  user_input is not None and user_input.isdigit():
    guess = int(user_input)
    if guess == secret_number:
     print("\nCorrect :)")
    else:
     print("\nIncorrect! The Number was " + str(secret_number))
 else:
    print("Please enter a number.")

 play_again = input("\nDo you want to play again? (yes/no): ")
 if play_again == 'yes':
     continue

 elif play_again == 'no':
     print("\nThank you for playing!:)")
     break

input("\nPress Enter to exit the program")



