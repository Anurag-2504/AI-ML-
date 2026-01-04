'''Q10. Let's create a "Number Guessing Game". Given a secret number (already
    decided by you), write a program that asks the user to guess it and prints:
    • "Too h i g h " if the guess is above the number
    • "Too low" if the guess is below
    • "Correct!" if the guess matches
'''

def guessing_game():
    secret_number = 21   
    guess = None

    while guess != secret_number:
        guess = int(input("Guess the number: "))

        if guess > secret_number:
            print("Too high")
        elif guess < secret_number:
            print("Too low")
        else:
            print("Correct!")

guessing_game()

'''
    Output:
        Guess the number: 22
        Too high
        Guess the number: 20
        Too low
        Guess the number: 21
        Correct!
'''    
