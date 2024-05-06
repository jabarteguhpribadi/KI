from cryptography.fernet import Fernet
import tkinter as tk
import customtkinter

customtkinter.set_appearance_mode("light")

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def enkripsi():
    pesan = entry_enkripsi.get()
    pesan = fer.encrypt(pesan.encode()).decode()
    
    hasil.insert(tk.END,"- " + pesan + "\n \n")
    entry_enkripsi.delete(0, "end")
    
def dekripsi():
    pesan = entry_dekripsi.get()
    pesan = fer.decrypt(pesan.encode()).decode()
    
    hasil.insert(tk.END,"- " + pesan + "\n \n")
    entry_dekripsi.delete(0, "end")

def clear():
    hasil.delete(0.1,"end")

### GUI ###
root = customtkinter.CTk()
root.title("Enkripsi")
root.geometry("720x720")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

### Side Frame ###
frame = customtkinter.CTkFrame(root, width=300, corner_radius=5)
frame.grid(row=0, column=0, sticky="nsw")

label1 = customtkinter.CTkLabel(frame, width=250, text="Aplikasi Enkripsi", font=customtkinter.CTkFont(size=15, weight="bold"))
label1.grid(row=0, column=0, sticky="nw", padx=(0,0))

### Entry Frame ###
entryframe = customtkinter.CTkFrame(frame, width= 200, corner_radius= 0.5)
entryframe.grid(row = 1, column = 0, pady = 5, padx = 5)

label2 = customtkinter.CTkLabel(entryframe, width=150, text="Plaintext", font=customtkinter.CTkFont(size=12))
label2.grid(row=0, column=0, padx=(0,0), pady=(2,0))
entry_enkripsi = customtkinter.CTkEntry(entryframe, height=30, width=200, corner_radius=5, placeholder_text="Pesan yang akan dienkripsi")
entry_enkripsi.grid(row=1, column=0, padx=10, pady=1)

label3 = customtkinter.CTkLabel(entryframe, width=150, text="Chipertext", font=customtkinter.CTkFont(size=12))
label3.grid(row=2, column=0, padx=(0,0), pady=(15,0))
entry_dekripsi = customtkinter.CTkEntry(entryframe, height=30, width=200, corner_radius=5, placeholder_text="Pesan yang akan didekripsi")
entry_dekripsi.grid(row=3, column=0, padx=10, pady=(1,10))

btnframe = customtkinter.CTkFrame(frame, width=250)
btnframe.grid(row=2, column=0)
btn1 = customtkinter.CTkButton(btnframe, width=70, text="Enkripsi", command=enkripsi)
btn1.grid(row=0, column=0, padx=5, pady=5)
btn2 = customtkinter.CTkButton(btnframe, width=70, text="Dekripsi", command=dekripsi)
btn2.grid(row=0, column=1, padx=5, pady=5)
btn3 = customtkinter.CTkButton(btnframe, width=70, text="Clear", command=clear)
btn3.grid(row=0, column=2, padx=5, pady=5)
### Entry Frame ###
### Side Frame ###

frameHasil = customtkinter.CTkFrame(root, width=450, corner_radius=5)
frameHasil.grid(row=0, column=1, padx=5, pady=5, sticky="nswe")
hasil = customtkinter.CTkTextbox(frameHasil, height=700, width=440, corner_radius=5)
hasil.grid(row=0, column=0, padx=10, pady=5, sticky="ns")


root.mainloop()