import tkinter as tk
import sqlite3
from tkinter import ttk # for styling
import os
from tkinter import messagebox # for displaying message boxes
from Crud_components import create_watchlist, read_all_watchlist # imports funcs from crud_components.py

def add_watchlist(): # function to add watchlist
    list_name = entry_list.get() 
    teacher_name = entry_teacher.get()
    
    if list_name and teacher_name: # checks if both fields are filled
        create_watchlist(list_name, teacher_name) # calls the create_watchlist function
        messagebox.showinfo("Success", "Watchlist added successfully.")
    else:
        messagebox.showwarning("Error", "Please fill in all fields.")

root = tk.Tk() # main window
root.title("Netflix Watchlist Manager") # title of the window
root.geometry("400x300") # size of the window

tk.Label(root, text="List Name:").pack(pady=5) # label for list name
entry_list = tk.Entry(root) # entry for list name
entry_list.pack(pady=5) # adds padding

tk.Label(root, text="Teacher Name:").pack(pady=5) # label for teacher name added padding
entry_teacher = tk.Entry(root) # entry for teacher name
entry_teacher.pack(pady=5) # adds padding

tk.Button(root, text="Add Watchlist", command=add_watchlist).pack(pady=20) # button to add watchlist

root.mainloop() # starts the GUI event loop