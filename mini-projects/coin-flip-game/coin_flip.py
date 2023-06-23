import random

coin = ['head', 'tail']

if __name__ == '__main__':
    #user needs to pick head or tail to flip coin
    user_input = input("Head or Tail: ")
    toss = random.choice(coin)

    while True:
        if user_input.lower() != 'head' and user_input.lower() != 'tail':
            print("I can't understand that. Try typing 'head' or 'tail'.")
        elif user_input.lower() != toss:
            print("You lose, better luck next time!")
            break
        else:
            print("Congrats, you win!")
            break
        user_input = input("Head or Tail: ")
