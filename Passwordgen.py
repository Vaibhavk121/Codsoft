import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x250")
        self.root.configure(bg="#f0f0f0")

        self.label = tk.Label(root, text="Enter length for the password:", bg="#f0f0f0", font=("Arial", 12))
        self.label.pack(pady=10)

        self.length_entry = tk.Entry(root, font=("Arial", 12))
        self.length_entry.pack(pady=10)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.generate_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                messagebox.showwarning("Warning", "Please enter a positive integer.")
                return

            password = self.create_password(length)
            self.result_label.config(text=f"Generated Password: {password}")

        except ValueError:
            messagebox.showwarning("Warning", "Invalid input. Please enter a valid number.")

    def create_password(self, length):
        characters = string.ascii_letters + string.digits + '@#'
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
