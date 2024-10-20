import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("300x200")  # Set the size of the window

# Function to be called when the button is clicked
def show_message():
    user_input = entry.get()  # Get the text from the entry field
    if user_input:
        messagebox.showinfo("Message", f"Hello, {user_input}!")
    else:
        messagebox.showwarning("Input Error", "Please enter your name.")

# Create a label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

# Create an entry field
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a button
button = tk.Button(root, text="Greet Me", command=show_message)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()