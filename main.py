from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50,bg=PINK)

canvas = Canvas(width=200, height=224,bg=PINK,highlightthickness=0)
t_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=t_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2,row=1)


my_label=Label(text="Timer",fg=GREEN,font=(FONT_NAME,35),bg=PINK)
my_label.grid(column=2,row=0)


button = Button(text="Start",highlightthickness=0)
button.grid(column=0,row=3)

restart_button=Button(text="restart",highlightthickness=0)
restart_button.grid(column=3,row=3)

tick=Label(text=" ✔",fg=GREEN,bg=PINK)
tick.grid(column=2, row=4)

window.mainloop()
