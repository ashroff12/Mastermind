import random
import tkinter

root = tkinter.Tk()
COLORS = ['red', 'yellow', 'blue', 'lime', 'aqua', 'gold']
code = []
white = 0
black = 0
guess_count=0
current_guess = [''] * 4
color_picker = ''
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


def opencolorpicker(pos, btn):
    global color_picker
    color_picker = tkinter.Toplevel(root)
    color1 = tkinter.Button(color_picker, width=4, height=2, bg=COLORS[0], command=lambda:closecolorpicker(pos, btn, COLORS[0]))
    color1.grid(row=0, column=0)
    color2 = tkinter.Button(color_picker, width=4, height=2, bg=COLORS[1], command=lambda:closecolorpicker(pos, btn, COLORS[1]))
    color2.grid(row=0, column=1)
    color3 = tkinter.Button(color_picker, width=4, height=2, bg=COLORS[2], command=lambda:closecolorpicker(pos, btn, COLORS[2]))
    color3.grid(row=0, column=2)
    color4 = tkinter.Button(color_picker, width=4, height=2, bg=COLORS[3], command=lambda:closecolorpicker(pos, btn, COLORS[3]))
    color4.grid(row=0, column=3)
    color5 = tkinter.Button(color_picker, width=4, height=2, bg=COLORS[4], command=lambda:closecolorpicker(pos, btn, COLORS[4]))
    color5.grid(row=0, column=4)
    color6 = tkinter.Button(color_picker, width=4, height=2, bg=COLORS[5], command=lambda:closecolorpicker(pos, btn, COLORS[5]))
    color6.grid(row=0, column=5)
def closecolorpicker(pos, btn, newcolor):
    global color_picker
    color_picker.destroy()
    btn.config(bg=newcolor)
    current_guess[pos] = newcolor

def draw():
    global canvas
    canvas.delete(tkinter.ALL)
    canvas.create_rectangle(0,0,cwidth,cheight, fill='orange')

#buttons for tkinter

b1 = tkinter.Button(root, width=4, height=2, bg="#00ffff", command=lambda:opencolorpicker(0,b1))
b1.grid(row=1, column=0)
b2 = tkinter.Button(root, width=4, height=2, bg="#000fff000", command=lambda:opencolorpicker(0,b2))
b2.grid(row=1, column=1)
b3 = tkinter.Button(root, width=4, height=2, bg="#129034", command=lambda:opencolorpicker(0,b3))
b3.grid(row=1, column=2)
b4 = tkinter.Button(root, width=4, height=2, bg="#519022", command=lambda:opencolorpicker(0,b4))
b4.grid(row=1, column=3)


#submit button
submit = tkinter.Button(root, text="Submit Guess", font="Arial 16 bold", padx=10)
submit.grid(row=1, column=4, padx=20)
#canvas
cwidth=300
cheight=400
canvas=tkinter.Canvas(root, width=cwidth, height=cheight)
canvas.grid(row=2, column=0, columnspan=5)

#runthegame
new_code()
draw()


root.mainloop()
