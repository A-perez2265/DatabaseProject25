import tkinter as tk
import sqlite3
from tkinter import ttk # for styling
import os
from tkinter import messagebox # for displaying message boxes
from Crud_components import create_watchlist, read_all_watchlist, delete_watchlist, update_watchlist # imports funcs from crud_components.py

def add_watchlist(): # function to add watchlist
    # gets values from entry fields
    list_name = entry_list.get()
    teacher_name = entry_teacher.get() 
    
    if list_name and teacher_name: # checks if both fields are filled
        create_watchlist(list_name, teacher_name) # calls the create_watchlist function
        # clears the entry fields
        entry_list.delete(0, tk.END)
        entry_teacher.delete(0, tk.END) 
        print_watchlists() # refreshes the watchlist display
        messagebox.showinfo("Success", f"Watchlist '{list_name}' added.") # shows success message
    else:
        messagebox.showwarning("Error", "Please fill in all fields.")

def print_watchlists(): # function to print watchlists
    for item in tree.get_children(): # clears the treeview
        tree.delete(item) # deletes each item in the treeview

    watchlists = read_all_watchlist()  # calls the read_all_watchlist function
    for wlValues in watchlists: # iterates through the watchlists
        tree.insert('', 'end', values=(wlValues[0],wlValues[1], wlValues[2], wlValues[3])) # inserts watchlist data into the treeview

def delete_selected(): # function to delete selected watchlist
    selected_item = tree.selection() # gets the selected item in the treeview
    if not selected_item:
        messagebox.showwarning("Error", "Please select a watchlist to delete.")
        return

    item = tree.item(selected_item) # gets the item data
    watchlist_id = item["values"][0] # gets the watchlist ID from the selected item
    list_name = item["values"][1] # gets the list name from the selected item

    confirm = messagebox.askyesno("Confirm Delete", f"Delete '{list_name}'?") # asks for confirmation
    if not confirm:
        return

    success, deleted_name = delete_watchlist(watchlist_id) # calls the delete_watchlist function
    if success: # if a watchlist was deleted
        print_watchlists() # refreshes the watchlist display   
        messagebox.showinfo("Deleted", f"Watchlist '{list_name}' deleted.")      
    else:
        messagebox.showwarning("Error", "Watchlist not found or already deleted.")

def update_watchlist_gui(): # function to update watchlist
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Error", "Please select a watchlist to update.")
        return

    old_item = tree.item(selected_item)
    old_list_name = old_item["values"][0]

    new_list_name = entry_list.get()
    new_teacher_name = entry_teacher.get()

    if not new_list_name or not new_teacher_name:
        messagebox.showwarning("Error", "Please fill in all fields.")
        return

    updated = update_watchlist(old_list_name, new_list_name, new_teacher_name)
    if updated > 0:
        messagebox.showinfo("Updated", f"Watchlist '{old_list_name}' updated.")
        print_watchlists()  # refresh table
    else:
        messagebox.showwarning("Error", "No watchlist found to update.")

def on_row_select(event): # function to handle row selection in treeview
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        values = item["values"]
        
        entry_list.delete(0, tk.END)
        entry_list.insert(0, values[1])  # list_name
        entry_teacher.delete(0, tk.END)
        entry_teacher.insert(0, values[2])  # teacher_name


# actual GUI code

root = tk.Tk() # main window
root.title("Netflix Watchlist Manager") # title of the window

tree = ttk.Treeview(root, columns=("ID", "List Name", "Teacher Name", "Created Date"), show="headings")
tree.heading("ID", text="ID") 
tree.column("ID", width=50, anchor="center") # sets column width and alignment of ID to be short n small
tree.heading("List Name", text="List Name")
tree.heading("Teacher Name", text="Teacher Name")
tree.heading("Created Date", text="Created Date")
tree.pack(pady=10) # packs the treeview with padding
tree.bind("<<TreeviewSelect>>", on_row_select) # binds the row selection event


tk.Label(root, text="List Name:").pack(pady=5) # label for list name
entry_list = tk.Entry(root) # entry for list name
entry_list.pack(pady=5) # adds padding

tk.Label(root, text="Teacher Name:").pack(pady=5) # label for teacher name added padding
entry_teacher = tk.Entry(root) # entry for teacher name
entry_teacher.pack(pady=5) # adds padding

tk.Button(root, text="Add Watchlist", command=add_watchlist).pack(pady=20) # button to add watchlist
tk.Button(root, text="Delete Selected", command=delete_selected).pack(pady=5) # button to delete selected watchlist
tk.Button(root, text="Update Selected", command=update_watchlist_gui).pack(pady=5) # button to update selected watchlist


# auto-display watchlists on startup
print_watchlists()

root.mainloop() # starts the GUI event loop