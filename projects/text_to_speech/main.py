from tkinter import *
from tkinter import ttk
import pyttsx3
from gtts import gTTS
from playsound import playsound


# ------------- Main Function -------------
def set_rate(eventObject):
    pass


def set_voice(eventObject):

    voice = voices.get()
    gender_voices = engine.getProperty("voices")
    if voice == "Female":
        engine.setProperty("voice", gender_voices[1].id)
    else:
        engine.setProperty("voice", gender_voices[0].id)


def speak():
    engine.setProperty("rate", 150)
    engine.say(text_box.get("1.0", "end-1c"))
    engine.runAndWait()


# ------------- Main variables -------------
engine = pyttsx3.init()
main_window = Tk()
main_window.geometry("1000x500+180+50")
main_window.title("Text to speech")
main_window.config(background="#797d7f")

photo = PhotoImage(file=r"images\text-to-speech.png")
main_window.iconbitmap(r"images\text-to-speech-_2_.ico")

button_frame = Frame(main_window, bg="#797d7f", height=400, width=400)
button_frame.place(x=600, y=40)


text_box = Text(
    main_window, width=50, height=17, font=("", 15, "bold"), bd=3, relief="sunken"
)
text_box.place(x=10, y=40)


voices = ttk.Combobox(
    button_frame, state="readonly", values=["Male", "Female"], font=("", 15), width=11
)
voices.place(x=1, y=70)

bt = Button(main_window, text="test", command=voices.insert(1, "aaaa"))
bt.pack()


voices_lb = Label(
    button_frame, text="Voice", font=("", 24, "bold"), bg="#797d7f", fg="white"
)
voices_lb.place(x=20, y=15)
voice = voices.get()


# Combobox event
voices.bind("<<ComboboxSelected>>", set_voice)
# rate.bind("<<ComboboxSelected>>", set_rate)


# ------------- Speak -------------
speak_img = PhotoImage(file=r"images\speaking.png")

speak_bt = Button(
    button_frame,
    image=speak_img,
    text="Speak",
    compound=LEFT,
    font=("", 15, "bold"),
    width=150,
    command=speak,
)
speak_bt.place(x=1, y=200)

# ------------- Save -------------
save_img = PhotoImage(file=r"images\mp3.png")
save_bt = Button(
    button_frame,
    image=save_img,
    text="Save",
    compound=LEFT,
    font=("", 15, "bold"),
    width=150,
)
save_bt.place(x=200, y=200)


main_window.mainloop()
