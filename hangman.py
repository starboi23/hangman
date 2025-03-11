#hangmanGame.py

import random
from collections import Counter

someWords = '''elephant giraffe platypus horse cow dog cat snake rhinocerous lion tiger bear cougar 
wilcat chicken turkey goat llama emu zebra sheep pig boar deer elk moose goose penguin donkey flamingo cheetah leopard'''
is_active = True
someWords = someWords.split(' ')
#this will choose our list
while is_active == True:
    word= random.choice(someWords)
    print(word)

    print("Guess the secret word: hint the word is an animal: ")

    for i in word:
        print('_', end=' ')
    print()

    playing = True

    letterGuessed = ''
    chances = len(word)+2
    correct = 0
    flag = 0 #updated when word is guessed correctly 

    try: 
        while(chances != 0) and flag == 0:
            print()
            chances -= 1
    
            try:
                guess = str(input("Enter a letter you think is in the word: ")).lower()
            except: 
                print("Enter only a letter")
                continue
            #validation of the guess
            if not guess.isalpha():
                print("Enter only a Letter: ")
                continue 
            elif len(guess)>1:
                print("Enter only a Single Letter: ")
                continue 
            elif guess in letterGuessed:
                print("You have already guessed that letter: ")
                continue 
            if guess in word:
                k = word.count(guess) #k stores the number of times a guessed letter is in the word
                for _ in range(k):
                    letterGuessed += guess #The letter guesses is addded as many times as it occured
        # print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                elif (Counter(letterGuessed) == Counter(word)):
                    print("The word is: ", end="")
                    print(word)
                    flag = 1
                    print("Congratulations, you won the game: ")
                    break 
                
                else:
                    print("_", end="")
            if chances <=0 and (Counter(letterGuessed) != Counter(word)):
                print()
                print("You Lost: Try again...")
                print("The word was: {}".format(word))
            
    except KeyboardInterrupt:
        print()
        print("Bye")
        exit()
        
    answer = input("Do you wish to continue?(Y for yes, N for no): ")
    if(answer != 'Y'):
        is_active = False