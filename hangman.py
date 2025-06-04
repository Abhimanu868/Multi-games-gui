import random 
import pygame
import tkinter as tk
from tkinter import messagebox
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
    def __init__(self,root):
        self.root = root
        self.root.geometry('400x400')
        global word_list
        self.word = random.choice(word_list)
        self.guessed_letters = ''
        self.tries = 6
        self.word_label = tk.Label(self.root,text='_ '*len(self.word),font=('Arial',16,'bold'))
        self.word_label.pack(pady=5)
        self.enter = tk.Entry(self.root,font=('Arial',16,'bold'))
        self.enter.pack(pady=5)
        self.enter_button = tk.Button(self.root,text='Enter',font=('Arial',16,'bold'),command=self.play_game)
        self.enter_button.pack(pady=5)
        self.feedback_label = tk.Label(self.root,text='')
        self.feedback_label.pack(pady=5)
        self.tries_label = tk.Label(self.root,text=f'Your tries left: {self.tries}/6')
        self.tries_label.pack(pady=5)
        self.reset_button = tk.Button(self.root,text='Reset',command=self.reset_game)
        self.reset_button.pack(pady=5)
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
            return
        if guess in self.guessed_letters:
            self.feedback_label.config(text='you already guessed')
            return
        self.guessed_letters+=guess
        if guess in self.word:
            self.feedback_label.config(text='correct')
        else:
            self.tries-=1
            self.tries_label.config(text=f"Your tries left: {self.tries}/6")
        self.display_update()
        if all(letter in self.guessed_letters for letter in self.word):
            messagebox.showinfo('You won the game. The word is:',self.word)
            self.enter.config(state='disabled')
            self.enter_button.config(state='disabled')
            return
        if self.tries==0:
            messagebox.showinfo('OOPS! You Lost this game. Better luck next time. The word was: ',self.word)
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
if __name__ == '__main__':
    root = tk.Tk()
    game = Hangman(root)
    root.mainloop()