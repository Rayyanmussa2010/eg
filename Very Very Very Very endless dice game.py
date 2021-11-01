# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 16:08:51 2021

@author: DELL
"""

from tkinter import *
import random
root=Tk()

root.title("dice")

root.geometry("400x400")
player1=Label(root, text="Player 1", bg="blue", fg="white")
player1.place(relx=0.1, rely=0.5, anchor=CENTER)
player2=Label(root, text="Player 2", bg="blue", fg="white")
player2.place(relx=0.9, rely=0.5, anchor=CENTER)
player1_score_label=Label(root, bg="blue", fg="white")
player1_score_label.place(relx=0.1, rely=0.4, anchor=CENTER)
player2_score_label=Label(root, bg="blue", fg="white")
player2_score_label.place(relx=0.9, rely=0.4, anchor=CENTER)
random_dice=Label(root, bg="brown", fg="white")
random_dice.place(relx=0.5, rely=0.5, anchor=CENTER)
player1














root.mainloop()