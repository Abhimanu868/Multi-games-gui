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
#global scopes
pl_music = True
music_length = 0.5
enable_music = True
enable_mode = False
def change_mode():
    global enable_mode
    if enable_mode:
        return {'bg':'#2e2e2e','fg':'white'}
    else:
        return {'bg':'white','fg':'#2e2e2e'}
def apply_to_any_window(win):
    change_colors = change_mode()
    win.configure(bg=change_colors['bg'])
    for widget in win.winfo_children():
        try:
            widget.configure(bg=change_colors['bg'],fg=change_colors['fg'])
        except:
            pass
#music
pygame.mixer.init()
def play_music_win():
    try:
        pygame.mixer.music.load(resource_path('mixkit-achievement-bell-600.wav')) 
        pygame.mixer.music.play(loops=0)
    except:
        print("Error")
def loose_music():
    try:
        pygame.mixer.music.load(resource_path('mixkit-player-losing-or-failing-2042.wav'))
        pygame.mixer.music.play(loops=0)
    except:
        print('Error')
def wrong_input():
    try:
        pygame.mixer.music.load(resource_path('mixkit-wrong-electricity-buzz-955.wav'))
        pygame.mixer.music.play(loops=0)
    except:
        print("Error")
def on_click():
    global enable_music
    if enable_music:
        try:
            click_sound = pygame.mixer.Sound(resource_path("computer-mouse-click-351398.mp3"))
            click_sound.play()
        except Exception as e1:
            print("Error on click music")
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

#rock-paper-scissor
play_list = ['rock','paper','scissor']
class rockpaperscissor:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.rounds = 6
        self.current_round=0
        self.window = tk.Tk()
        self.window.geometry('500x500')
        self.window.title('Welcome to my game')
        self.top_label = tk.Label(self.window,text='Rock,Paper,Scissors',font=('Arial',16,'bold'))
        self.top_label.pack(pady=5)
        self.winner_label = tk.Label(self.window,text='')
        self.winner_label.pack(pady=5)
        self.your_choice = tk.Label(self.window,text='Your choice: ',font=('Arial',16,'bold'))
        self.your_choice.pack(pady=5)
        self.computer_choice = tk.Label(self.window,text='Computer choice: ',font=('Arial',16,'bold'))
        self.computer_choice.pack(pady=5)
        self.score_label = tk.Label(self.window,text=f'Your score: 0/Computer score: 0',font=('Arial',16,'bold'))
        self.score_label.pack(pady=5)
        self.rounds_label = tk.Label(self.window,text=f'Rounds: 0/6',font=('Arial',16,'bold'))
        self.rounds_label.pack(pady=5)
        self.button_frame = tk.Frame(self.window,bg="#e6f7ff")
        self.button_frame.pack(pady=20)
        self.rock_button = tk.Button(self.button_frame, text="Rock",height=2, width=15, command=lambda: [on_click(),self.play_game("rock")])
        self.rock_button.grid(row=0,column=0,pady=5,padx=5)

        self.paper_button = tk.Button(self.button_frame, text="Paper",height=2,  width=15, command=lambda: [on_click(),self.play_game("paper")])
        self.paper_button.grid(row=0,column=1,pady=5,padx=5)

        self.scissor_button = tk.Button(self.button_frame, text="Scissor",height=2,  width=15, command=lambda: [on_click(),self.play_game("scissor")])
        self.scissor_button.grid(row=0,column=2,pady=5,padx=5)
        self.reset_button = tk.Button(self.button_frame, text="Reset",height=2,  width=15, command=lambda: [on_click(),self.reset_game()])
        self.reset_button.grid(row=1,column=0,pady=5,padx=5)
        self.exit_button = tk.Button(self.button_frame,text='Back',height=2, width=15,command=self.on_back)
        self.exit_button.grid(row=1,column=1,pady=5,padx=5)
        apply_to_any_window(self.window)
    def play_game(self,user_input):
        if self.current_round>=self.rounds:
            return
        self.comp_choice = random.choice(play_list)
        self.your_choice.config(text=f'Your choice: {user_input}')
        self.computer_choice.config(text=f'Computer choice: {self.comp_choice}')
        if user_input==self.comp_choice:
            self.winner_label.config(text='Its a tie')
        elif(user_input=='rock' and self.comp_choice=='scissor')or(user_input=='paper' and self.comp_choice=='rock')or(user_input=='scissor' and self.comp_choice=='paper'):
            self.winner_label.config(text='You won this round')
            self.player_score+=1
        else:
            self.winner_label.config(text='computer won this round') 
            self.computer_score+=1
        self.score_label.config(text=f'Your score: {self.player_score}/Computer score: {self.computer_score}')
        self.current_round+=1
        self.rounds_label.config(text=f'Rounds: {self.current_round}/{self.rounds}')
        
        if self.current_round == self.rounds:
            self.decide_winner()
    def decide_winner(self):
        if self.player_score>self.computer_score:
            play_music_win()
            self.winner_label.config(text='You won the game')
        elif(self.player_score==self.computer_score):
            loose_music()
            self.winner_label.config(text='Its tie better luck next time')
        else:
            loose_music()
            self.winner_label.config(text='Computer won the game')
    def reset_game(self):
        self.player_score = 0
        self.computer_score=0
        self.current_round=0
        self.winner_label.config(text='')
        self.score_label.config(text='Your score: 0/Computer score: 0')
        self.rounds_label.config(text='Rounds: 0/6')
    def on_back(self):
        self.click= on_click()
        destroy = self.window.destroy
        self.window.after(300,destroy)
'''Hangman game'''
word_list = ['apple','grape', 'lemon', 'mango', 'peach',
    'berry', 'plum', 'melon', 'chili', 'onion',
    'carrot', 'bread', 'cheese', 'toast', 'cream',
    'chair', 'table', 'couch', 'glass', 'plate',
    'knife', 'spoon', 'cup', 'fork', 'plant',
    'stone', 'river', 'ocean', 'beach', 'cloud',
    'rain', 'storm', 'light', 'shade', 'flame',
    'brush', 'paint', 'brick', 'steel', 'wheel',
    'train', 'plane', 'truck', 'sheep', 'horse',
    'tiger', 'zebra', 'eagle', 'panda', 'mouse']
class Hangman:
    def __init__(self):
        self.roo = tk.Tk()
        self.roo.geometry('500x500')
        global word_list
        self.word = random.choice(word_list)
        self.guessed_letters = ''
        self.tries = 6
        self.word_label = tk.Label(self.roo,text='_ '*len(self.word),font=('Arial',16,'bold'))
        self.word_label.pack(pady=5)
        self.enter = tk.Entry(self.roo,font=('Arial',16,'bold'))
        self.enter.pack(pady=5)
        self.enter_button = tk.Button(self.roo,text='Enter',width=15,font=('Arial',16,'bold'),command=lambda:[on_click(),self.play_game()])
        self.enter_button.pack(pady=5)
        self.feedback_label = tk.Label(self.roo,text='',font=('Arial',16,'bold'))
        self.feedback_label.pack(pady=5)
        self.tries_label = tk.Label(self.roo,text=f'Your tries left: {self.tries}/6')
        self.tries_label.pack(pady=5)
        self.reset_button = tk.Button(self.roo,text='Reset',width=15,command=lambda:[on_click(),self.reset_game()])
        self.reset_button.pack(pady=5)
        self.back_button = tk.Button(self.roo,text='Back',width=15,command=self.on_back)
        self.back_button.pack(pady=5)
        apply_to_any_window(self.roo)
        self.display_update()
    def display_update(self):
        guessed_word = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                guessed_word+=letter+" "
            else:
                guessed_word+='_ '  
        self.word_label.config(text=guessed_word.strip())  
    def play_game(self):
        guess = self.enter.get().lower()
        self.enter.delete(0,tk.END)
        if (not guess.isalpha()) or len(guess)!=1:
            self.feedback_label.config(text='Invalid choice!')
            wrong_input()
            return
        if guess in self.guessed_letters:
            self.feedback_label.config(text='you already guessed')
            wrong_input()
            return
        self.guessed_letters+=guess
        if guess in self.word:
            self.feedback_label.config(text='correct')
        else:
            self.tries-=1
            self.tries_label.config(text=f"Your tries left: {self.tries}/6")
        self.display_update()
        if all(letter in self.guessed_letters for letter in self.word):
            play_music_win()
            self.feedback_label.config(text='You won')
            self.enter.config(state='disabled')
            self.enter_button.config(state='disabled')
            return
        if self.tries==0:
            loose_music()
            self.feedback_label.config(text=f'You lost. The word was: {self.word}')
            self.enter.config(state='disabled')
            self.enter_button.config(state='disabled')
            return
    def reset_game(self):
        self.word = random.choice(word_list)
        self.guessed_letters=''
        self.tries=6
        self.enter.config(state='normal')
        self.enter_button.config(state='active')
        self.word_label.config(text='_ '*len(self.word))
        self.tries_label.config(text=f'Your tries left: {self.tries}/6')
        self.feedback_label.config(text='')
    def on_back(self):
        self.click= on_click()
        destroy = self.roo.destroy
        self.roo.after(300,destroy)
"Number Guessing"
class NumberGuessing:
    def __init__(self):
        self.number = random.randint(1,100)
        self.guesses=0
        self.total_guess = 10
        self.guess_game = tk.Tk()
        self.guess_game.title("Number guess game")
        self.guess_game.geometry("500x500")
        self.input_label = tk.Label(self.guess_game,text="Enter Number: ",font=('Arial',16,'bold'))
        self.input_label.pack(pady=5)
        self.enter_input = tk.Entry(self.guess_game,font=('Arial',16,'bold'))
        self.enter_input.pack(pady=5)
        self.guess_button = tk.Button(self.guess_game,text='Enter',width=15,command=lambda:[on_click(),self.enter_number()])
        self.guess_button.pack(pady=5)
        self.feedback_label = tk.Label(self.guess_game,text='',font=('Arial',16,'bold'))
        self.feedback_label.pack(pady=5)
        self.reset_button = tk.Button(self.guess_game,text='Reset',width=15,command=lambda:[on_click(),self.reset()])
        self.reset_button.pack(pady=5)
        self.back_button = tk.Button(self.guess_game,text='Back',width=15,command=self.on_back)
        self.back_button.pack(pady=5)
        apply_to_any_window(self.guess_game)
    def enter_number(self):
        guess_number = self.enter_input.get()
        self.enter_input.delete(0,tk.END)
        if not guess_number.isdigit():
            wrong_input()
            self.feedback_label.config(text="Invalid input. Enter a number from 1 to 100.")
            return
        guess_number = int(guess_number)
        if not (1 <= guess_number <= 100):
            wrong_input()
            self.feedback_label.config(text="Number must be between 1 and 100.")
            return
        self.guesses+=1
        if guess_number == self.number:
            play_music_win()
            self.feedback_label.config(text="Congratulations! You guessed the number!")
            self.enter_input.config(state='disabled')
            self.guess_button.config(state='disabled')
        elif guess_number > self.number:
            self.feedback_label.config(text="You guessed too high!")
        else:
            self.feedback_label.config(text="You guessed too low!")
        if self.guesses >= self.total_guess:
            loose_music()
            self.feedback_label.config(text=f"Game Over! The number was {self.number}")
            self.enter_input.config(state='disabled')
            self.guess_button.config(state='disabled')
    def reset(self):
        self.guesses=0
        self.number = random.randint(1,100)
        self.enter_input.config(state='normal')
        self.guess_button.config(state='normal')
        self.feedback_label.config(text='')
    def on_back(self):
        on_click()
        self.guess_game.after(300, self.guess_game.destroy)
root = tk.Tk()
root.title('menu')
root.geometry('500x500')
rock_game_button = tk.Button(root,text='Rock Paper Scissors',width=15,command=lambda:[rockpaperscissor(),on_click()])
rock_game_button.pack(pady=5)
hangman_game_button = tk.Button(root,text='Hangman',width=15,command=lambda:[on_click(),Hangman()])
hangman_game_button.pack(pady=5)
guessnumber_game_button = tk.Button(root,text="Number guess",width=15,command=lambda:[on_click(),NumberGuessing()])
guessnumber_game_button.pack(pady=5)
def open_settings():
    def change_volume(value):
        global music_length
        user_value = float(value)
        pygame.mixer.music.set_volume(user_value)
        music_length=user_value
    def toggle_color():
        global enable_mode
        enable_mode=not enable_mode
        apply_to_any_window(root)
        apply_to_any_window(settings_window)
    def on_back():
        click= on_click()
        destroy = settings_window.destroy
        settings_window.after(300,destroy)
    def on_exit():
        click = on_click()
        destroy = root.destroy
        root.after(300,destroy)
    settings_window = tk.Toplevel(root)
    settings_window.geometry('500x500')
    volume_label = tk.Label(settings_window,text='Change Volume: ')
    volume_label.pack(pady=5)
    volume_change_slider = tk.Scale(settings_window,from_=0,to=1,resolution=0.1,orient=tk.HORIZONTAL,command=lambda value:change_volume(value))
    volume_change_slider.set(music_length)
    volume_change_slider.pack(pady=5)
    change_mode_button = tk.Button(settings_window,text='Toggle',width=15,command=lambda:[on_click(),toggle_color()])
    change_mode_button.pack(pady=5)
    play_music_button = tk.Button(settings_window,text='Music',width=15,command=lambda:[on_click(),play_music()])
    play_music_button.pack(pady=5)
    back_button = tk.Button(settings_window,text='Back',width=15,command=on_back)
    back_button.pack(pady=5)
    exit_button = tk.Button(settings_window,text='Exit',width=15,command=on_exit)
    exit_button.pack(pady=5)
    apply_to_any_window(settings_window)
settings_button = tk.Button(root,text='Settings',width=15,command=lambda:[on_click(),open_settings()])
settings_button.pack(pady=5)
apply_to_any_window(root)
root.mainloop()