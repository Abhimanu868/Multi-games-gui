import random
import tkinter as tk
from tkinter import messagebox
word_list = ['apple', 'grape', 'lemon', 'mango', 'peach',
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
        self.word_guess_label = tk.Label(self.root,text='Your guess: ',font=('Arial',16,'bold'))
        self.word_guess_label.pack(pady=5)
        self.entry = tk.Entry(self.root,font=('Arial', 14), width=5)
        self.entry.pack()
        self.check_button = tk.Button(self.root,text='Submit',font=('Arial',16,'bold'),command=self.check_guess)
        self.check_button.pack(pady=5)
        self.feedback_label = tk.Label(self.root,text='')
        self.feedback_label.pack(pady=5)
        self.tries_label = tk.Label(self.root,text= f'Your tries left: {self.tries}/6',font=('Arial',16,'bold'))
        self.tries_label.pack(pady=5)
        self.update_display()
    def update_display(self):
        displayed_word = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                displayed_word+=letter+' '    
            else:
                displayed_word+='_ '
        self.word_label.config(text=displayed_word.strip())
    def check_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0,tk.END)
        if (not guess.isalpha()) or len(guess)!=1:
            self.feedback_label.config(text='Invalid input!! Please enter a charcter')
            return 
        if guess in self.guessed_letters:
            self.feedback_label.config(text='Already guessed')
            return
        self.guessed_letters+=guess
        if guess in self.word:
            self.feedback_label.config(text='correct')
        else:
            self.tries-=1
            self.feedback_label.config(text='Incorrect guess!! Better luck next time')
            self.tries_label.config(text=f'Your tries left:{self.tries}/6')
        self.update_display()
        if all(letter in self.guessed_letters for letter in self.word):
            messagebox.showinfo(f'Correct you guessed right {self.word}')
            self.root.quit()
        if self.tries == 0:
            messagebox.showinfo('No more tries')
            self.root.quit()
if __name__ =='__main__':
    root = tk.Tk()
    game = Hangman(root)
    root.mainloop()