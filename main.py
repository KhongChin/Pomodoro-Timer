import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def focus_window(option):
    if option == "on":
        window.deiconify()
        window.focus_force()
        window.attributes('-topmost', 1)
    elif option == "off":
        window.attributes('-topmost', 0)


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    start_button.config(state="normal")
    reset_button.config(state="disabled")
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    tick_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start_button.config(state="disabled")
    reset_button.config(state="normal")
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps in range(1, 8, 2):
        focus_window("off")
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

    elif reps in range(2, 7, 2):
        focus_window("on")
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)

    elif reps == 8:
        focus_window("on")
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = format(count % 60, "02d")
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        ticks = ""
        for _ in range(math.floor(reps/2)):
            ticks += "✔"
        tick_label.config(text=ticks)


# ---------------------------- UI SETUP -------------------------------
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=image)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"),)
canvas.grid(row=1, column=1)

timer_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(row=0, column=1)
start_button = tkinter.Button(text="Start", command=start_timer, highlightthickness=0, state="normal")
start_button.grid(row=2, column=0)
reset_button = tkinter.Button(text="Reset", command=timer_reset, highlightthickness=0, state="disabled")
reset_button.grid(row=2, column=2)
tick_label = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
tick_label.grid(row=3, column=1)

window.mainloop()
