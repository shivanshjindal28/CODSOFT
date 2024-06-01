import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x400")
        self.root.config(bg="#f7f7f7")

        self.todo_list = []

        self.frame = tk.Frame(self.root, bg="#f7f7f7")
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(
            self.frame, 
            width=50, 
            height=10, 
            bd=0, 
            fg="#333333", 
            selectbackground="#a6a6a6", 
            selectforeground="#ffffff", 
            highlightthickness=0, 
            activestyle="none",
            font=("Helvetica", 12)
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=(10,0))

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(
            self.root, 
            width=50, 
            bd=0, 
            highlightthickness=2, 
            highlightbackground="#cccccc", 
            font=("Helvetica", 12)
        )
        self.entry.pack(pady=10, padx=10)

        self.add_button = tk.Button(
            self.root, 
            text="Add To-Do", 
            command=self.add_todo, 
            bg="#4caf50", 
            fg="#ffffff", 
            bd=0, 
            font=("Helvetica", 12), 
            activebackground="#45a049"
        )
        self.add_button.pack(pady=5, padx=10, fill=tk.X)

        self.remove_button = tk.Button(
            self.root, 
            text="Remove Selected", 
            command=self.remove_todo, 
            bg="#f44336", 
            fg="#ffffff", 
            bd=0, 
            font=("Helvetica", 12), 
            activebackground="#e53935"
        )
        self.remove_button.pack(pady=5, padx=10, fill=tk.X)

        self.clear_button = tk.Button(
            self.root, 
            text="Clear All", 
            command=self.clear_todo, 
            bg="#ff9800", 
            fg="#ffffff", 
            bd=0, 
            font=("Helvetica", 12), 
            activebackground="#fb8c00"
        )
        self.clear_button.pack(pady=5, padx=10, fill=tk.X)

    def add_todo(self):
        item = self.entry.get()
        if item != "":
            self.listbox.insert(tk.END, item)
            self.todo_list.append(item)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a to-do item.")

    def remove_todo(self):
        try:
            selected_item_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_item_index)
            self.todo_list.pop(selected_item_index)
        except IndexError:
            messagebox.showwarning("Warning", "You must select an item to remove.")

    def clear_todo(self):
        self.listbox.delete(0, tk.END)
        self.todo_list = []

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
