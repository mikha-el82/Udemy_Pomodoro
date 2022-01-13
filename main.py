from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#519259"
YELLOW = "#fffda2"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = ""
timer_running = False


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    global timer_running
    timer_running = False
    window.after_cancel(timer)
    timer_txt.config(text="Timer", fg=GREEN)
    checkmarks_txt.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def timer_check():
    global timer_running
    if not timer_running:
        timer_running = True
        start_timer()


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_sec)
        timer_txt.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_sec)
        timer_txt.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        timer_txt.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    mins = count // 60
    secs = count % 60
    if secs < 10:
        secs = f"0{secs}"
    time_left = f"{mins}:{secs}"
    canvas.itemconfig(timer_text, text=time_left)
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        work_cycles = reps // 2
        ticks = work_cycles * "✔"
        checkmarks_txt.config(text=ticks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Counter")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_txt = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_txt.grid(column=1, row=0)

start_btn = Button(text="Start", font=(FONT_NAME, 20, "bold"), highlightthickness=0, command=timer_check)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", font=(FONT_NAME, 20, "bold"), highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

checkmarks_txt = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
checkmarks_txt.grid(column=1, row=3)

window.mainloop()
