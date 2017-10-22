import random


secreate_number = random.randint(1,10)
#print(secreate_number)
count = 0

while (count<5):



    Guess_number = input("Guess between 1 to 10, What is your number :")
    if Guess_number == "show":
        print(secreate_number)
        continue
    elif Guess_number=="Help":
        print("Type word 'show' to print secrate random number")
        continue
    if Guess_number.isdigit()==False :
        print("Wrong Input, Please enter integer")
        continue
    Int_Guess = int(Guess_number)
    count = count + 1
    if secreate_number == (Int_Guess):
        print("Greate, You win, your guess number {} match with secrate number {}".format(Guess_number,secreate_number))
        moderator = input("you want to play again? answer yes or no!! ")
        if moderator == "yes":
            count = 0
            secreate_number = random.randint(1,10)
            continue
        else:
            print("ok, Bye Bye !!!")
        break
    else:
        if count == 5:
            print("Sorry your trial excceed 5 times and your secreat randum number was {}".format(Guess_number))
            moderator = input("you want to play again? answer in yes or no! ")
            if moderator=="yes":
                count = 0
                secreate_number = random.randint(1, 10)
                continue
            else:
                print("Bye Bye!!!")
        if secreate_number<Int_Guess:
            print("Sorry, You guess is greater than secreate no, you miss it!")
            #print("Sorry you miss it, try again")
        if secreate_number>Int_Guess:
            print("Sorry, You guess is less than secreate no, you miss it!")
            #print("Sorry you miss it, try again")

        continue

