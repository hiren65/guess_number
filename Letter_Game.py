import random

#Make a list of words

main_library = [ "Orange", "Apple", "Banana", "Strawberry","Raspberry", "Pitch",
                 "Almond", "Lime", "Grape"]
secrate_word = ""
myguess_list = []

def combine_word(input_list):
    my_word = ""
    for item in input_list:
        my_word = my_word + item
    return my_word
def compare_word(word1, word2,inputGuessList):
    if len(word1)>=len(word2):
        count = 0
        tito = list(word1)
        pn = "positive"
        #print("1 {} 2 {}".format(word1,word2))
        for item in list(word2):
                #print("first {}".format(word2))
                #print("positive going {} and {}".format(item,tito[count]))
                if item == tito[count]:
                    print("")
                    # print("positive {}".format(inputGuessList))
                    #print(inputGuessList)


                else:
                    print("Nagative selection of {}".format(item))
                    del inputGuessList[-1]
                    word2[:-1]
                    #print("leted {}".format(word2))
                    pn = "nagative"
                    break
                    print("Nagative Selection")
                count += 1

        if pn == "positive":
            print("Positive Selection")
        else:
            print("Nagative Selection")

    return word2



def play_game():
    #pick random word
    secrate_word = (random.choice(main_library)).lower()
    myguess_list = []
    myword = ""
    while True:
        enter_word = input("Enter your guessed letter >")

        if enter_word == "close":
            print("bye")
            break
        if enter_word.lower()=="show":
            print(secrate_word)
            continue
        if len(enter_word)>1:
            print("please enter single alphabet")
            continue
        myguess_list.append(enter_word)
        #print("nnn {}".format(myguess_list))

        myword = combine_word(myguess_list)

        #print("nw {}".format(myword))
        myword = compare_word(secrate_word,myword,myguess_list)
        print(myword)

        if myword==secrate_word:
            print(myword)
            print("Bingo you did it and you won!!")
            repeat = input("you want to play again?answer 'y' or for no press any key and enter ")
            if repeat.lower()=="y":
                play_game()
                #continue
            else:
                print("bye")
                break
        #print(myword)



play_game()

#tt = ["t","i","k"]
#dito = combine_word(tt)
#print(dito)

#compare_word("wer","e")

