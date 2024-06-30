import tkinter as tk
from tkinter import messagebox
import json

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x500")  # Set window size to 400x500 pixels

        self.contacts = self.load_contacts()

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky='w')

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5, sticky='w')

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.search_label = tk.Label(root, text="Search:")
        self.search_label.grid(row=5, column=0, padx=10, pady=5, sticky='e')
        self.search_entry = tk.Entry(root)
        self.search_entry.grid(row=5, column=1, padx=10, pady=5, sticky='w')
        self.search_button = tk.Button(root, text="Search", command=self.search_contact)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.listbox = tk.Listbox(root, width=50, height=15)
        self.listbox.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        self.load_listbox()

    def load_contacts(self):
        try:
            with open('contacts.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open('contacts.json', 'w') as file:
            json.dump(self.contacts, file)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        if name and phone and email:
            self.contacts.append({'name': name, 'phone': phone, 'email': email})
            self.save_contacts()
            self.load_listbox()
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "All fields are required")

    def delete_contact(self):
        selected = self.listbox.curselection()
        if selected:
            del self.contacts[selected[0]]
            self.save_contacts()
            self.load_listbox()
        else:
            messagebox.showwarning("Selection Error", "Select a contact to delete")

    def search_contact(self):
        search_term = self.search_entry.get().lower()
        results = [c for c in self.contacts if search_term in c['name'].lower() or search_term in c['phone'] or search_term in c['email']]
        self.listbox.delete(0, tk.END)
        for contact in results:
            self.listbox.insert(tk.END, f"{contact['name']} - {contact['phone']} - {contact['email']}")

    def load_listbox(self):
        self.listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.listbox.insert(tk.END, f"{contact['name']} - {contact['phone']} - {contact['email']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
