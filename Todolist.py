import tkinter as tk
from tkinter import messagebox
import json
import os

# Constants for file storage
TODO_FILE = 'todo_list.json'

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({'task': task, 'completed': False})
        save_tasks(tasks)
        task_entry.delete(0, tk.END)
        refresh_tasks()
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty.")

def refresh_tasks():
    for widget in task_frame.winfo_children():
        widget.destroy()
    for i, task in enumerate(tasks):
        task_text = task['task']
        status = "Completed" if task['completed'] else "Pending"
        lbl = tk.Label(task_frame, text=f"{i + 1}. {task_text} [{status}]")
        lbl.pack(anchor='w', pady=2)

def update_task():
    try:
        task_num = int(task_entry.get()) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]['completed'] = not tasks[task_num]['completed']
            save_tasks(tasks)
            refresh_tasks()
        else:
            messagebox.showwarning("Input Error", "Invalid task number.")
    except ValueError:
        messagebox.showwarning("Input Error", "Enter a valid task number.")

def delete_task():
    try:
        task_num = int(task_entry.get()) - 1
        if 0 <= task_num < len(tasks):
            tasks.pop(task_num)
            save_tasks(tasks)
            refresh_tasks()
        else:
            messagebox.showwarning("Input Error", "Invalid task number.")
    except ValueError:
        messagebox.showwarning("Input Error", "Enter a valid task number.")

app = tk.Tk()
app.title("To-Do List")
app.geometry("400x400")
app.configure(bg='#f7f7f7')

header = tk.Label(app, text="To-Do List", font=('Helvetica', 18, 'bold'), bg='#f7f7f7', pady=10)
header.pack()
header = tk.Label(app, text="Your Personal manager", font=('Helvetica', 12, ), bg='#f7f7f7', pady=10)
header.pack()
task_frame = tk.Frame(app, bg='#f7f7f7')
task_frame.pack(pady=10)

task_entry_frame = tk.Frame(app, bg='#f7f7f7')
task_entry_frame.pack(pady=10)

task_entry = tk.Entry(task_entry_frame, width=30)
task_entry.grid(row=0, column=0, padx=5)

button_frame = tk.Frame(app, bg='#f7f7f7')
button_frame.pack(pady=10)

button_width = 15  # Set the same width for all buttons


add_button = tk.Button(button_frame, text="Add Task", command=add_task, bg='#5cb85c', fg='white', width=button_width)
add_button.grid(row=0, column=0, padx=5, pady=5)

update_button = tk.Button(button_frame, text="Update Task", command=update_task, bg='#0275d8', fg='white', width=button_width)
update_button.grid(row=0, column=1, padx=5, pady=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, bg='#d9534f', fg='white', width=button_width)
delete_button.grid(row=0, column=2, padx=5, pady=5)

tasks = load_tasks()
refresh_tasks()

app.mainloop()
