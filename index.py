from tkinter import *
from tkinter import filedialog
gui = Tk()

def save():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        mess = text.get("1.0",END)
        with open(filepath, "w") as file:
            file.write(mess)

gui.geometry("600x500+300+200")
gui.title("Текстовый редактор")

frame_text = Frame(gui, bg='green', bd=5)
frame_button = Frame(gui, bg='blue', bd=5)

text = Text(frame_text, height=25, font='Arial,14',wrap=WORD)
text.pack()
butt_save = Button(frame_button,text="Сохранить", command=save)
butt_save.configure(width=600)
butt_save.pack()




frame_text.pack()
frame_button.pack()

gui.mainloop() 