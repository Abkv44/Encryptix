# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 09:57:51 2024

@author: Abk
"""

import tkinter as tk
from tkinter import messagebox

tasks = []

def list_tasks():
    listbox.delete(0, tk.END)
    if not tasks:
        listbox.insert(tk.END, "No tasks currently!")
    else:
        for index, task in enumerate(tasks, start=1):
            listbox.insert(tk.END, f"{index}. {task}")

def add_task():
    task_to_be_added = task_entry.get()
    if task_to_be_added:
        tasks.append(task_to_be_added)
        task_entry.delete(0, tk.END)
        list_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        tasks.pop(selected_task_index)
        list_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def on_quit():
    # root.quit()
    exit()
    
root = tk.Tk()
root.title("Task Manager")

# Task entry
task_label = tk.Label(root, text="Enter task")
task_label.pack(pady=5)
task_label.config(font=("Helevetica", 16, "bold"))

task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=5)

# Buttons
add_task_button = tk.Button(root, text="Add Task", command=add_task,  width = 14)
add_task_button.pack(pady=5)
add_task_button.configure(bg="yellow")

delete_task_button = tk.Button(root, text="Delete Task", command=delete_task, width=14)
delete_task_button.pack(pady=5)
delete_task_button.configure(bg="yellow")

quit_button = tk.Button(root, text="Quit", command=on_quit, width=14)
quit_button.pack(pady=5)
quit_button.configure(bg="yellow")

# Task list display
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)
listbox.config(font=("Helevetica", 10))

root.mainloop()
