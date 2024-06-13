from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT = ('Arial', 10, 'normal')
BG = 'white'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letters = [choice(letters) for char in range(randint(8,10))]
    pw_symbols = [choice(symbols) for symbol in range(randint(2,4))]
    pw_numbers = [choice(numbers) for num in range(randint(2,4))]

    password_list = pw_letters + pw_symbols + pw_numbers
    shuffle(password_list)
    password = "".join(password_list)
    input_pw.insert(0, password)
    pyperclip.copy(password) # add new password to clipboard
    messagebox.showinfo(title= 'Your password is ready!', message= 'Your new randomly generated password is ready and has been added to the clipboard! You can now paste it.')

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_website = input_website.get()
    new_username = input_username.get()
    new_pw = input_pw.get()
    new_data = {
        new_website: {
            'email': new_username,
            'password': new_pw,
        }
    }
    # alert user if they left something blank, ends function if they did so nothing is saved
    if len(new_website) ==0 or len(new_username)==0 or len(new_pw) == 0:
        messagebox.showinfo(title= 'Forgetting something?', message = 'Whoops looks like you forgot to add some info\nMake sure all fields are filled!')
    else:
        try:
            # open json file in read mode
            with open("data.json", 'r') as data_file:
                # read/load the old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # update the old data with new data
            data.update(new_data)

            with open("data.json", 'w') as data_file:
                # write data to json file; indents are for readability
                json.dump(data, data_file, indent=4)
        finally:
            input_website.delete(0, END)
            #input_username.delete(0, END)
            input_pw.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_pw():
    search_web = input_website.get()
    try:
        with open("data.json", 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title= 'Error', message= 'No data file found.')
    else:
        if search_web in data:
            email = data[search_web]['email']
            password = data[search_web]['password']
            messagebox.showinfo(title= search_web, message= f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title= 'Error', message= f"No account for {search_web} has been saved.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg = BG)

# canvas w/ logo
canvas = Canvas(width = 200 , height = 200,  bg = BG, highlightthickness=0)
pwm_lock = PhotoImage(file = 'logo.png')
canvas.create_image(100, 95, image= pwm_lock)
# timer_text = canvas.create_text(100, 135, text = "00:00", fill = "white", font=(FONT_NAME, 30, 'bold'))
canvas.grid(column = 1, row = 0)

#labels
website = Label(text='Website:', font = FONT, bg = BG)
website.grid(column = 0, row =1)
username = Label(text='Email/Username:', font = FONT, bg = BG)
username.grid(column = 0, row =2)
password = Label(text='Password:', font = FONT, bg = BG)
password.grid(column = 0, row =3)

#buttons
generate = Button(text = 'Generate Password', command=generate_pw)
generate.grid(column = 2, row = 3)
add = Button(text = 'Add', width = 43, command=save)
add.grid(column = 1, row =4, columnspan = 2 )
search = Button(text = 'Search', width = 13, command = find_pw)
search.grid(column = 2, row = 1)

#entries
input_website = Entry(width = 32)
input_website.grid(column = 1, row = 1)
input_website.focus() # method calls the cursor to automatically begin here
input_username = Entry(width= 50)
input_username.grid(column = 1, row = 2, columnspan =2)
input_pw = Entry(width=32)
input_pw.grid(column = 1, row = 3)

window.mainloop()
