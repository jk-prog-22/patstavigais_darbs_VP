from tkinter import *
import string
import random


#Paroļu ģenerators
password_chars = string.ascii_letters + string.digits

def password_generator():
    password_field.delete(0, END) #Pēc ievadīšanas izdzēst saitli
    length = int(char_input.get()) #lietotajs ievada cik garu paroli grib
    password = "".join([random.choice(password_chars) for _ in range(length)]) #random skaitļu ģenerēšana
    password_field.insert(0, password)
    


#Lietoāja interfeiss
window = Tk()
window.title("Paroļu Ģenerators")
window.config(padx=50, pady=50, bg="#1BD7A6") #Loga konfigurācija/krāsa/izmers

label_title = Label(text="Paroļu ģenerators", #Virsraksts
                    bg="#1BD7A6",
                    fg="#000000",
                    font=("Arial", 35, "bold"))
label_title.grid(row=0, column=0, columnspan=3, pady=30)

label_before_input = Label(text="Ievadi Simbolu skaitu", #Nepieciešamo simbolu skaits
                           bg="#FFFFFF",
                           fg="#000000",
                           font=("Arial", 15, "bold"))
label_before_input.grid(row=1, column=0)

char_input = Entry(bg="#FFFFFF")
char_input.grid(row=1, column=1)
char_input.insert(0, "")
char_input.focus()


generate_password_button = Button(text="Ģenerēt paroli",
                                  bg="#FFFFFF",
                                  height=4,
                                  width=55,
                                  command=password_generator)
generate_password_button.grid(row=2, column=0, columnspan=3, padx=50, pady=50)

password_field = Entry(bg="#1BD7A6", #Paroles lauks
                       font=("Arial", 15, "bold"), width=40)
password_field.grid(row=3, column=0, columnspan=3)


window.mainloop()