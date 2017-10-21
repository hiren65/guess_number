import random


secreate_number = random.randint(1,10)
print(secreate_number)

while True:
    Guess_number = int(input("What is your number :"))
    if secreate_number == (Guess_number):
        print("Greate your guess number {} match with secrate number {}".format(Guess_number,secreate_number))
        break
    else:
        print("Sorry you miss it, try again")
        continue

