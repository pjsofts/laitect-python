import random
secret = random.randint(1, 10)
counter = 0
while True:
    guess = int(input("Please enter your guess:"))
    counter = counter +1
    if guess ==secret:
        print(f"You win with {counter} guesses")
        break
    if counter == 5:
        print("you lose")
        break
    if guess>secret:
        print("Your guess is larger")
    else:
        print("Your guess is smaller")
