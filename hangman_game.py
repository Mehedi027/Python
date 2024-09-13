import random

print(''' 
888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P" '''                             )

word_list = ["mehedi", "sagnik", "soumyarshi", "apple"]
random_word = ""
stage_6 = '''
    __________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / |
     |
    _|___

'''
stage_5 = '''

    __________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___

'''
stage_4 = ''' 

    __________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___

'''

stage_3 = ''' 

    __________
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___

'''
stage_2 = ''' 

    __________
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___

'''

stage_1 = ''' 

    __________
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___

'''

#print (stage_6)

letter = []
random_word = random.choice(word_list)
for i in random_word:
    letter.append(i)
j = len(letter)
m = '_'
print(letter)
placeholder = " "
for u in letter:
    placeholder += m
print(f"Guess the word : {placeholder}")
#print(f"word to guess : {j*m} ")

game_over = False
correct_letter = []
life = 6
while not game_over:
    guess = input("Guess a letter: ")
    guess = guess.lower()
    display = " "

    for n in random_word:
        if n == guess:
            display += n
            correct_letter.append(guess)
        elif n in correct_letter:
            display += n
        else:
            display += "_"
            
    print(display)
        

    if guess not in random_word:
        life -= 1
        print(f"You guessed: {guess}, it is not in the word. You lose a life")
        print(f"************************** {life}/6 LIVES LEFT *******************************")
        if life == 0:
            game_over = True
            print("*********************** YOU LOSE *****************************")
            print(f" The word was : {random_word}")
    else:
        print(f"You guessed: {guess}, it is in the word. Congrats!")
        print(f"************************** {life}/6 LIVES LEFT *******************************")


    if life == 5:
        print(stage_1)
    elif life == 4:
        print(stage_2)
    elif life == 3:
         print(stage_3)
    elif life == 2:
        print(stage_4)
    elif life == 1:
        print(stage_5)
    elif life == 0:
        print(stage_6)     


    if "_" not in display:
        game_over = True
        print("*********************** YOU WIN *****************************")
