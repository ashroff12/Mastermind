import random
code = []
white = 0
black = 0
guess_count= 0
def new_code():
    global code
    while len(code) <4:
        r = random.randint(0,5)
        if r not in code:
            code.append(r)
def score_guess(guess):
    global black
    global white
    global code
    global guess_count
    white=0
    black=0
    #first check for white
    #print (guess)
    #print (code)
    for i in range(4):
        if guess[i] == str(code[i]):
            white += 1
        else:
            for j in range(4):
                if guess[i] == str(code[j]):
                    black += 1
                
    print("whites: " + str(white) + " blacks: " + str(black))
    if white == 4:
        #do some win stuff
        print("You win:(")
    elif guess_count == 10:
        #you ran out pf guesses
        print('You suck at your only job')
    else:
        #no win no lose keep going
        player_guess()
            
    #then check for black

def player_guess():
    print('Make a guess')
    guess = input()
    score_guess(guess)


    
new_code()
print("Welcome to mastermind. You will need to guess a four digit code")
print("The avalible digits are 0 to 5")
print("white = good color and black = bad color")
print("you will get up to 8 turns")
player_guess()



