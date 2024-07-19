import tkinter as tk
from tkinter import messagebox, ttk

# Initialize contact list
contacts = []

# Function to add a contact
def add_contact(name, phone, email, address):
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    messagebox.showinfo("Success", "Contact added successfully!")

# Function to view all contacts
def view_contacts():
    view_window = tk.Toplevel(root)
    view_window.title("View Contacts")
    view_window.geometry("400x300")
    tk.Label(view_window, text="Contacts List", font=("Helvetica", 16)).pack(pady=10)
    if contacts:
        for contact in contacts:
            contact_info = f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}"
            tk.Label(view_window, text=contact_info, font=("Helvetica", 12)).pack(pady=5)
    else:
        tk.Label(view_window, text="No contacts available.", font=("Helvetica", 12)).pack(pady=10)

# Function to search for a contact
def search_contact(query):
    results = [contact for contact in contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
    return results

# Function to handle searching
def search_contact_gui():
    query = search_query_entry.get()
    results = search_contact(query)
    search_results_window = tk.Toplevel(root)
    search_results_window.title("Search Results")
    search_results_window.geometry("400x300")
    tk.Label(search_results_window, text="Search Results", font=("Helvetica", 16)).pack(pady=10)
    if results:
        for contact in results:
            contact_info = f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}"
            tk.Label(search_results_window, text=contact_info, font=("Helvetica", 12)).pack(pady=5)
    else:
        tk.Label(search_results_window, text="No contacts found.", font=("Helvetica", 12)).pack(pady=10)

# Function to create contact GUI
def add_contact_gui():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    add_contact(name, phone, email, address)

# Create main window
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x400")

# Create a style
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=10)
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TEntry', padding=5)

# Create a frame for form inputs
form_frame = ttk.Frame(root, padding="20")
form_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Add Contact Form
ttk.Label(form_frame, text="Add New Contact", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)

# Label and Entry for Name
ttk.Label(form_frame, text="Name:", anchor='e').grid(row=1, column=0, sticky="e", padx=10, pady=5)
name_entry = ttk.Entry(form_frame, width=30)
name_entry.grid(row=1, column=1, padx=10, pady=5)

# Label and Entry for Phone
ttk.Label(form_frame, text="Phone:", anchor='e').grid(row=2, column=0, sticky="e", padx=10, pady=5)
phone_entry = ttk.Entry(form_frame, width=30)
phone_entry.grid(row=2, column=1, padx=10, pady=5)

# Label and Entry for Email
ttk.Label(form_frame, text="Email:", anchor='e').grid(row=3, column=0, sticky="e", padx=10, pady=5)
email_entry = ttk.Entry(form_frame, width=30)
email_entry.grid(row=3, column=1, padx=10, pady=5)

# Label and Entry for Address
ttk.Label(form_frame, text="Address:", anchor='e').grid(row=4, column=0, sticky="e", padx=10, pady=5)
address_entry = ttk.Entry(form_frame, width=30)
address_entry.grid(row=4, column=1, padx=10, pady=5)

# Add Contact Button
ttk.Button(form_frame, text="Add Contact", command=add_contact_gui).grid(row=5, column=0, columnspan=2, pady=10)

# Create a frame for buttons
button_frame = ttk.Frame(root, padding="20")
button_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

# View Contacts Button
ttk.Button(button_frame, text="View Contacts", command=view_contacts).pack(pady=2)

# Search Contact GUI
ttk.Label(button_frame, text="Search (Name or Phone):").pack(pady=5)
search_query_entry = ttk.Entry(button_frame, width=30)
search_query_entry.pack(pady=5)
ttk.Button(button_frame, text="Search Contact", command=search_contact_gui).pack(pady=10)

# Configure grid weights for responsive design
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Start main event loop
root.mainloop()
