from tkinter import *
from tkinter import messagebox
from time import sleep


def check():
    username = username_ent.get().strip()
    password = pass_ent.get().strip()
    if username == "admin" and password == "admin":
        # Close login window
        messagebox.showinfo("Success", "You have successfully logged in.")
        window.destroy()

    else:
        messagebox.showerror(
            title="Login Failed", message="Invalid username or password"
        )


window = Tk()
window.geometry("500x300+380+150")
window.config(background="silver")
window.title("Login System")
window.iconbitmap(r"A:\Work-Apps\alhanini\app\images\alhanini.ico")


fr = Frame(window, width=400, height=200, bg="silver")
fr.place(x=50, y=100)
lb = Label(window, text="Login", font=("", 30, "bold"), width=10, height=2, bg="silver")
lb.pack(fill=X)

username_lb = Label(fr, text="Username:", font=("", 22), bg="silver")
username_lb.place(x=1, y=5)
pass_lb = Label(fr, text="Password:", font=("", 22), bg="silver")
pass_lb.place(x=1, y=60)


username_ent = Entry(fr, width=15, font=("", 20))
username_ent.place(x=160, y=10)
pass_ent = Entry(fr, width=15, font=("", 20), show="*")
pass_ent.place(x=160, y=60)

login_bt = Button(
    fr,
    text="Login",
    width=10,
    font=("", 15, "bold"),
    cursor="hand2",
    relief="raised",
    bd=3,
    command=check,
)
login_bt.place(x=200, y=120)
window.bind("<Return>", lambda x: check())

window.mainloop()
