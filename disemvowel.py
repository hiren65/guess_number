def disemvowel(word):
    myList = list(word)
    print(myList)
    for item in word:
        if item == "a" or item == "e" or item == "i" or item == "o" or item == "u" :
            myList.remove(item)
        if item == "a".upper() or item == "e".upper() or item == "i".upper() or item == "o".upper() or item == "u".upper() :
            myList.remove(item)
    word = ''.join(myList)


    return word


tindo = disemvowel("hireniAa")

print(tindo)


