import random
import tkinter as tk
import pygame
root = tk.Tk()
#creating window
root.geometry("400x500")
root.title("Welcome to my game")
root.config(bg="lightblue")
#defining globally
your_score = 0
computer_score = 0
choices = ['rock','paper','scissors']
dark_mode = True
pl_music = True
#creating labels
title_label = tk.Label(root,text="Rock,Paper,Scissors",font=("Arial",16,"bold"),bg="#e6f7ff",fg="red")
title_label.pack(pady=20)
score_label = tk.Label(root,text="Your Score: 0 | Computer Score: 0",font=("Arial",16,'bold'),bg="#e6f7ff")
score_label.pack(pady=10)
result_label = tk.Label(root,text="",font=("Arial",16,'bold'),bg="#e6f7ff")
result_label.pack(pady=10)
user_choice_label = tk.Label(root,text="Your choice: ",font=("Arial",16,"bold"),bg="#e6f7ff")
user_choice_label.pack(pady=5)
comp_choice_label = tk.Label(root,text="Computer choice: ",font=("Arial",16,'bold'),bg="#e6f7ff")
comp_choice_label.pack(pady=5)
rounds_play_label = tk.Label(root,text="Total Rounds: 0/4",font=("Arial",16,'bold'),bg="#e6f7ff")
rounds_play_label.pack(pady=5)
#main functionality
pygame.mixer.init()
def play_music():
    global pl_music
    try:
        if pl_music:
            pygame.mixer.music.load("main-theme-68815.mp3")
            pygame.mixer.music.play(loops=-1)
            pl_music=False
        else:
            pygame.mixer.music.stop()
            pl_music=True
    except Exception as e:
        print("Music error:",e)
rounds=4
current_round=0
def play_game(user_choice):
    global your_score,computer_score,choices,rounds,current_round
    if(current_round>=rounds):
        return
    computer = random.choice(choices)
    user_choice_label.config(text=f"Your choice: {user_choice}")
    comp_choice_label.config(text=f"Computer choice: {computer}")
    if user_choice==computer:
        result = "Its a Tie"
    elif((user_choice=='rock'and computer=='scissors')or(user_choice=='paper'and computer=='rock')or(user_choice=='scissors'and computer=='paper')):
        your_score+=1
        result = 'You Wins'
    else:
        computer_score+=1
        result='Computer Wins'
    result_label.config(text=result)
    score_label.config(text=f"Your Score: {your_score} / Computer Score: {computer_score}")
    current_round+=1
    rounds_play_label.config(text=f"Total Rounds: {current_round}/{rounds}")
    if(current_round==rounds):
        end_game()
def end_game():
    global your_score,computer_score
    if(your_score==computer_score):
        result = 'Its a Tie!!'
    elif(your_score<computer_score):
        result = 'Computer Wins!!'
    else:
        result = 'You Wins!!'
    result_label.config(text=result)
def reset_game():
    global your_score,computer_score,current_round
    your_score=0
    computer_score=0
    current_round=0
    score_label.config(text="Your Score: 0 | Computer Score: 0")
    result_label.config(text="")
    user_choice_label.config(text="Your choice: ")
    comp_choice_label.config(text='Computer choice: ')
    rounds_play_label.config(text='Total Rounds: 0/4')
def change_mode():
    global dark_mode
    if(dark_mode):
        root.config(bg="black")
        dark_mode=False
    else:
        root.config(bg='lightblue')
        dark_mode=True
#buttons for above
button_frame = tk.Frame(root,bg="#e6f7ff")
button_frame.pack(pady=20)
rock_button = tk.Button(button_frame,text='rock',height=2,width=10, command=lambda:play_game('rock'))
rock_button.grid(row=0,column=0,padx=5)
paper_button=tk.Button(button_frame,text='paper',height=2,width=10,command=lambda:play_game('paper'))
paper_button.grid(row=0,column=1,padx=5)
scissor_button = tk.Button(button_frame,text='scissors',height=2,width=10,command=lambda:play_game('scissors'))
scissor_button.grid(row=0,column=2,padx=5)
reset_button = tk.Button(button_frame,text="Reset",height=2,width=10,command=reset_game)
reset_button.grid(row=1,column=0,pady=5)
exit_button=tk.Button(button_frame,text='Exit',height=2,width=10,command=root.destroy)
exit_button.grid(row=1,column=1,pady=5)
change_theme_button = tk.Button(button_frame,text="Mode",height=2,width=10,command=change_mode)
change_theme_button.grid(row=1,column=2,pady=5)
play_music_button = tk.Button(button_frame,text="Music",height=2,width=10,command=play_music)
play_music_button.grid(row=2,column=1,pady=5)
root.mainloop()