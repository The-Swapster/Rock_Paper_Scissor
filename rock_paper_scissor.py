import random
from tkinter import *
t = Tk()
t.title('Lets play')
t.configure(bg = 'pink')
user_score = 0
computer_score = 0
user_choice = ''
computer_choice = ''


def choice_to_number(choice):
    rps = {'rock':0, 'paper':1, 'scissor':2}
    return rps[choice]


def number_to_choice(number):
    rps = {0:'rock', 1:'paper', 2:'scissor'}
    return rps[number]


def random_computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])


def result(user_choice, comp_choice):
    global user_score
    global computer_score
    user = choice_to_number(user_choice)
    comp = choice_to_number(comp_choice)
    answer = "\nYour Choice: {uc} \nComputer's Choice: {cc} \nYour Score: {u} \nComputer's Score: {c} \n".format(uc = user_choice, cc = comp_choice, u = user_score , c = computer_score)
    text_area.insert(END, answer)
    if (user == comp):
        a = 'Tie'
    elif ((user - comp) % 3 == 1):
        a = 'User Wins'
        user_score += 1
    else:
        a = 'Computer Wins'
        computer_score += 1
    text_area.insert(END, a)
    
    
def rock():
    global user_choice
    global computer_choice
    user_choice='rock'
    computer_choice=random_computer_choice()
    result(user_choice,computer_choice)
    
    
def paper():
    global user_choice
    global computer_choice
    user_choice='paper'
    computer_choice=random_computer_choice()
    result(user_choice,computer_choice)
    
    
def scissor():
    global user_choice
    global computer_choice
    user_choice='scissor'
    computer_choice=random_computer_choice() 
    result(user_choice,computer_choice)  
    
    
button1 = Button(text="       Rock       ",bg="skyblue",command=rock)
button1.grid(column=0,row=1)
button2 = Button(text="       Paper      ",bg="violet",command=paper)
button2.grid(column=0,row=2)
button3 = Button(text="      Scissor     ",bg="lightgreen",command=scissor)
button3.grid(column=0,row=3)
text_area = Text(t, height = 12, width = 30, bg = "yellow2")
text_area.grid(column = 0, row = 4)
t.mainloop()
    