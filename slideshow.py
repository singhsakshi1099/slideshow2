from itertools import cycle
from PIL import Image, ImageTk
import time 
import tkinter as tk

root = tk. Tk()
root.title("Image Slideshow Viewer")

#list of the Image path 
image_paths = [
    "/home/sakshi/Downloads/2022 photos/WhatsApp Image 2024-07-24 at 10.29.09 AM (1).jpeg",
    "/home/sakshi/Downloads/2022 photos/WhatsApp Image 2024-07-24 at 10.22.07 AM (1).jpeg",
    "/home/sakshi/Downloads/WhatsApp Image 2025-01-29 at 12.09.58 PM (1).jpeg",
    "/home/sakshi/Downloads/2022 photos/WhatsApp Image 2024-07-24 at 10.29.12 AM.jpeg",
]


#Resize the image to 1080*1080
image_size=(1080,1080)
images=[Image.open(path).resize(image_size)for path in image_paths]
photo_images=[ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_Button = tk.Button(root, text='Play Slidesshow',command=start_slideshow)
play_Button.pack()

root.mainloop()