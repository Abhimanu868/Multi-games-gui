import random
import tkinter as tk
import pygame
import os
import sys
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS  # PyInstaller's temp folder
    except AttributeError:
        base_path = os.path.abspath(".")  # Normal Python execution

    return os.path.join(base_path, relative_path)
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
enable_music = True
music_level = 0.5
#creating labels
title_label = tk.Label(root,text="Rock,Paper,Scissors",font=("Arial",16,"bold"),bg="#e6f7ff",fg="red")
title_label.pack(pady=20)
score_label = tk.Label(root,text="Your Score: 0 / Computer Score: 0",font=("Arial",16,'bold'),bg="#e6f7ff")
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
pygame.mixer.init() # intializing the pygame mixer
#adding on click sound feature
def on_click():
    if enable_music:
        try:
            click_sound = pygame.mixer.Sound(resource_path("computer-mouse-click-351398.mp3"))
            click_sound.play()
        except Exception as e1:
            print("Error on click music")
#adding play music feature on clicking
def play_music():
    global pl_music
    try:
        music_path = resource_path("main-theme-68815.mp3")
        if pl_music:
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play(loops=-1)
            pl_music=False
        else:
            pygame.mixer.music.stop()
            pl_music=True
    except Exception as e:
        print("Music error:",e)
rounds=4
current_round=0
#main game 
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
        result = 'You won this round'
    else:
        computer_score+=1
        result='Computer won this round'
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
        result = 'Win for Computer!!'
    else:
        result = 'Congratulations You won the game!!'
    result_label.config(text=result)
#for reseting
def reset_game():
    global your_score,computer_score,current_round
    your_score=0
    computer_score=0
    current_round=0
    score_label.config(text="Your Score: 0 / Computer Score: 0")
    result_label.config(text="")
    user_choice_label.config(text="Your choice: ")
    comp_choice_label.config(text='Computer choice: ')
    rounds_play_label.config(text='Total Rounds: 0/4')
#adding features on exit button
def on_exit():
    on_click()
    destroy = root.destroy
    root.after(300,destroy)
#settings menu
def open_settings():
    #change volume
    def change_volume(value):
        global music_level
        user_value = float(value)
        pygame.mixer.music.set_volume(user_value)
        music_level=user_value
    #for changing the mode to dark on clicking and then agin to lightblue on another click
    def change_mode():
        global dark_mode
        if(dark_mode):
            after_settings = settings_pop.config(bg='black')
            after_feature = root.config(bg="black")
            root.after(100,after_feature,after_settings)
            dark_mode=False
        else:
            after_black = settings_pop.config(bg="lightblue")
            change_light = root.config(bg='lightblue')
            root.after(100,change_light,after_black)
            dark_mode=True
    #for back functionality
    def back_game():
        on_click()
        destroy = settings_pop.destroy
        settings_pop.after(300,destroy)
    settings_pop = tk.Toplevel(root)
    settings_pop.title("Settings")
    settings_pop.geometry("300x300")
    settings_pop.config(bg="lightblue")
    vol_label = tk.Label(settings_pop,text="Change the Volume: ")
    vol_label.pack(pady=10)
    vol_change_slider = tk.Scale(settings_pop,from_=0,to=1,resolution=0.1,orient=tk.HORIZONTAL,command=change_volume)
    vol_change_slider.set(music_level)
    vol_change_slider.pack(padx=5)
    play_music_button = tk.Button(settings_pop,text="Music",height=2,width=10,command=lambda:[on_click(),play_music()])
    play_music_button.pack(pady=5)
    change_theme_button = tk.Button(settings_pop,text="Mode",height=2,width=10,command=lambda:[on_click(),change_mode()])
    change_theme_button.pack(pady=5)
    back_button = tk.Button(settings_pop,text='Back',height=2,width=10,command=back_game)
    back_button.pack(pady=5)
    log_out_button = tk.Button(settings_pop,text='Log Out',height=2,width=10,command=on_exit)
    log_out_button.pack(pady=5)
#buttons for above
button_frame = tk.Frame(root,bg="#e6f7ff")
button_frame.pack(pady=20)
rock_button = tk.Button(button_frame,text='rock',height=2,width=10, command=lambda:[on_click(),play_game('rock')])
rock_button.grid(row=0,column=0,padx=5)
paper_button=tk.Button(button_frame,text='paper',height=2,width=10,command=lambda:[on_click(),play_game('paper')])
paper_button.grid(row=0,column=1,padx=5)
scissor_button = tk.Button(button_frame,text='scissors',height=2,width=10,command=lambda:[on_click(),play_game('scissors')])
scissor_button.grid(row=0,column=2,padx=5)
reset_button = tk.Button(button_frame,text="Reset",height=2,width=10,command=lambda:[on_click(),reset_game()])
reset_button.grid(row=1,column=0,pady=5)
settings_menu_button = tk.Button(button_frame,text="Settings",height=2,width=10,command=lambda:[on_click(),open_settings()])
settings_menu_button.grid(row=1,column=1,pady=5)
root.mainloop()