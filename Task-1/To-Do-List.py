import tkinter as tk
from tkinter import messagebox, ttk
import random, time

tasks = []
done_count = 0

# add a new task
def add_task():
    global tasks
    t = task_input.get()
    if t.strip() != "":
        stamp = time.strftime("%H:%M:%S")
        tasks.append(f"{t} (added {stamp}) [❌]")
        refresh_list()
        task_input.delete(0, tk.END)
        messagebox.showinfo("Task Added", f"'{t}' was added.")
        update_bar()
    else:
        messagebox.showwarning("Empty!", "Type something first!")

# mark selected task as done
def mark_done():
    global done_count
    try:
        idx = task_box.curselection()[0]
        if "[❌]" in tasks[idx]:
            tasks[idx] = tasks[idx].replace("[❌]", "[✅]")
            done_count += 1
            refresh_list()
            update_bar()
            confetti()
            messagebox.showinfo("Nice!", random.choice(quotes))
        else:
            messagebox.showinfo("Info", "That one is already done.")
    except:
        messagebox.showerror("Oops", "Pick a task first.")

# delete task
def delete_task():
    global done_count
    try:
        idx = task_box.curselection()[0]
        if "[✅]" in tasks[idx]:
            done_count -= 1
        tasks.pop(idx)
        refresh_list()
        update_bar()
    except:
        messagebox.showerror("Error", "No task selected.")

# redraw list
def refresh_list():
    task_box.delete(0, tk.END)
    for i, t in enumerate(tasks, 1):
        task_box.insert(tk.END, f"{i}. {t}")

# update progress bar
def update_bar():
    if tasks:
        percent = (done_count / len(tasks)) * 100
        bar_val.set(percent)
    else:
        bar_val.set(0)

# quick confetti animation
def confetti():
    colors = ["red", "yellow", "green", "blue", "purple", "orange"]
    for _ in range(15):
        x, y = random.randint(40, 460), random.randint(40, 90)
        sz = random.randint(5, 12)
        c = canvas.create_oval(x, y, x+sz, y+sz, fill=random.choice(colors))
        root.after(600, lambda c=c: canvas.delete(c))

# button hover
def hover_in(e): e.widget["bg"] = "#ffb700"
def hover_out(e): e.widget["bg"] = e.widget._bg

root = tk.Tk()
root.title("My To-Do List")
root.geometry("520x580")
root.configure(bg="#202030")

# heading
lbl = tk.Label(root, text="My To-Do List", font=("Comic Sans MS", 20, "bold"), fg="cyan", bg="#202030")
lbl.pack(pady=8)

# entry
task_input = tk.Entry(root, font=("Arial", 14), width=30, bg="#2a2a40", fg="white", insertbackground="white")
task_input.pack(pady=8)

# buttons
btn_frame = tk.Frame(root, bg="#202030")
btn_frame.pack(pady=8)

def make_btn(txt, clr, cmd, col):
    b = tk.Button(btn_frame, text=txt, font=("Arial", 12, "bold"),
                  bg=clr, fg="white", width=14, command=cmd, relief="flat")
    b.grid(row=0, column=col, padx=4)
    b._bg = clr
    b.bind("<Enter>", hover_in)
    b.bind("<Leave>", hover_out)
    return b

make_btn("Add", "#4CAF50", add_task, 0)
make_btn("Mark Done", "#2196F3", mark_done, 1)
make_btn("Delete", "#f44336", delete_task, 2)

# listbox
frame = tk.Frame(root, bg="#202030")
frame.pack(pady=8)

scroll = ttk.Scrollbar(frame)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

task_box = tk.Listbox(frame, font=("Arial", 14), width=42, height=12,
                      bg="#2a2a40", fg="white", selectbackground="#00bcd4",
                      yscrollcommand=scroll.set)
task_box.pack(side=tk.LEFT, fill=tk.BOTH)
scroll.config(command=task_box.yview)

# progress bar
bar_val = tk.DoubleVar()
bar = ttk.Progressbar(root, variable=bar_val, maximum=100, length=380)
bar.pack(pady=12)

tk.Label(root, text="Progress", font=("Arial", 12, "bold"), fg="white", bg="#202030").pack()

# canvas for confetti
canvas = tk.Canvas(root, width=480, height=90, bg="#202030", highlightthickness=0)
canvas.pack()

quotes = ["Keep going!", "Great job!", "You're on fire!", "Nice work!", "Done & Dusted!"]

root.mainloop()
