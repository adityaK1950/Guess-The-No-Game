# Guess the Number

n=27
number_of_guesses = 1
print("Number of guesses is limited to only 5 Times:")

while number_of_guesses <= 5:
    guess_number = int(input("Guess the number: "))
    
    if guess_number  < n:
        print("You entered a lesser number, Please enter a greater number.")
    elif guess_number > n:
        print("You entered a greater number, Please enter a smaller number.")
    else:
        print("You have guessed the correct number!  YOU WON! 🥳🤩🥳")
        print(number_of_guesses, "no. of guesses took to finish.")
        break
    
    print(5 - number_of_guesses, "no. of guesses left")
    number_of_guesses += 1
        
if number_of_guesses > 5:
    print("GAME OVER! YOU LOST DUFFER 😔💔")