import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

# Function to animate the GIF
def play_gif():
    global gif_frames, gif_index
    gif_index = (gif_index + 1) % len(gif_frames)
    gif_label.config(image=gif_frames[gif_index])
    root.after(100, play_gif)  # Adjust speed here

# Function to switch GIF and execute a function
def on_image_click():
    print("Clicked! Changing GIF and executing function...")

    # Change GIF dynamically
    load_gif("speaking-gui-unscreen.gif")  # Change to another GIF

    # Execute any function
    execute_function()

# Example function to execute on click
def execute_function():
    print("Executing some function...")

# Function to load a new GIF
def load_gif(gif_path):
    global gif_frames, gif_index, gif_label
    gif = Image.open(gif_path)
    gif_frames = [ImageTk.PhotoImage(frame.copy().resize((300, 300))) for frame in ImageSequence.Iterator(gif)]
    gif_index = 0
    gif_label.config(image=gif_frames[0])  # Set the first frame immediately
    play_gif()

# Initialize Tkinter
root = tk.Tk()
root.title("GIF Switcher UI")
root.geometry("800x600")
root.configure(bg="black")

# GIF Display Label (Initialize Before Using)
gif_label = tk.Label(root, bg="black")
gif_label.place(x=250, y=100)  # Adjust position

# Load initial GIF
gif_frames = []
gif_index = 0
load_gif("basic-gui-unscreen.gif")  # Default GIF

# Load Clickable Image
button_img = Image.open("button.png").resize((80, 80))
button_photo = ImageTk.PhotoImage(button_img)

# Clickable Image (Below GIF)
button_label = tk.Label(root, image=button_photo, bg="black", cursor="hand2")
button_label.place(x=360, y=450)
button_label.bind("<Button-1>", lambda event: on_image_click())

# Run Tkinter main loop
root.mainloop()
