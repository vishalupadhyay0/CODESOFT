#A To-Do List application is a useful project that helps users manage
#and organize their tasks efficiently. This project aims to create a
#command-line or GUI-based application using Python, allowing
#users to create, update, and track their to-do lists

import tkinter as tk
from tkinter import messagebox, ttk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("600x400")
        self.root.configure(bg='#f0f0f0')

        self.task_list = []

        # Styling
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 12), padding=10)
        self.style.configure('TEntry', font=('Arial', 12), padding=10)
        self.style.configure('TLabel', font=('Arial', 12), padding=10)
        
        # Title
        self.title_label = tk.Label(root, text="To-Do List", font=('Arial', 24, 'bold'), bg='#f0f0f0')
        self.title_label.pack(pady=20)

        # Task Listbox
        self.task_frame = tk.Frame(root, bg='#f0f0f0')
        self.task_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        self.task_listbox = tk.Listbox(self.task_frame, width=60, height=10, selectmode=tk.SINGLE, font=('Arial', 12))
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.scrollbar = tk.Scrollbar(self.task_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)
        
        # Entry Frame
        self.entry_frame = tk.Frame(root, bg='#f0f0f0')
        self.entry_frame.pack(pady=10, padx=20, fill=tk.BOTH)
        
        self.task_entry = ttk.Entry(self.entry_frame, width=50)
        self.task_entry.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.add_button = ttk.Button(self.entry_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.update_button = ttk.Button(self.entry_frame, text="Update Task", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.delete_button = ttk.Button(self.entry_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=10, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            new_task = self.task_entry.get()
            if new_task:
                self.task_list[task_index] = new_task
                self.task_listbox.delete(task_index)
                self.task_listbox.insert(task_index, new_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a new task.")
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            del self.task_list[task_index]
            self.task_listbox.delete(task_index)
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

