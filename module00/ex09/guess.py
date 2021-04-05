from random import randint


def fct():
    print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!")
    print("\n\n")
    n = randint(1, 99)
    x = '0'
    attempt = 0
    while(int(x) != n):
        x = input("What's your guess between 1 and 99 ? ")
        attempt += 1
        if x == 'exit':
            print('Good bye !')
            return
        if (x.isdigit() == False):
            x = '0'
            print("That's not a number.")
        elif int(x) > n:
            print("Too high!")
        elif int(x) < n:
            print("Too low!")
        elif int(x) == n:
            print("Congratulations, you've got it!\nYou won in ",attempt, " attempts!")


fct()
 
