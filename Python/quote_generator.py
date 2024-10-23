from tkinter import *
from PIL import Image, ImageTk
from requests import get
import io

root = Tk()
root.title("Inspirational Images")
root.geometry("1000x600+50+50")
root.configure(bg="#f0f0f0")

f = ("Calibri", 20, "bold")

def gi():
    try:
        # Using a placeholder image URL
        url = "https://zenquotes.io/api/image/800x400"
        res = get(url)
        
        # Load the image from bytes
        img = Image.open(io.BytesIO(res.content))  # Load image from response content
        imgtk = ImageTk.PhotoImage(image=img)  # Convert to PhotoImage
        lab.configure(image=imgtk)  # Display the image on GUI
        lab.photo = imgtk  # Keep a reference

    except Exception as e:
        print("Issue:", e)

# Create a Frame for better layout
frame = Frame(root, bg="#ffffff", bd=10, relief="ridge")
frame.pack(pady=20, padx=20, fill=BOTH, expand=True)

btn = Button(frame, text="Get Image", font=f, bg="#4CAF50", fg="white", activebackground="#45a049", relief="flat", command=gi)
btn.pack(pady=10)

lab = Label(frame, bg="#ffffff", font=f)
lab.pack(pady=10)

root.mainloop()
