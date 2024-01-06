import tkinter as tk

def calculate():
    try:
      num = ent_field.get()

      if num == "":
         pass
      else:
        if num[0] in ["÷", "x"]:
          ent_field.delete(0, tk.END)
          ent_field.insert(tk.END, "Error: Invalid expression")
          ent_field.config(state=tk.DISABLED)
          btn_c.config(bg="#FF7F7F")
        
        num = num.replace("÷", "/")
        num = num.replace("x", "*")
        result = eval(num)
        ent_field.delete(0, tk.END)
        ent_field.insert(tk.END, result)

    except (TypeError, ZeroDivisionError, SyntaxError):
        ent_field.delete(0, tk.END)
        ent_field.insert(tk.END, "Error")
        ent_field.config(state=tk.DISABLED)
        btn_c.config(bg="#FF7F7F")

def backspace():
   num = ent_field.get()
   back = num[:-1]
   ent_field.delete(0, tk.END)
   ent_field.insert(0, back)

def clear():
  ent_field.config(state=tk.NORMAL)
  ent_field.delete(0, tk.END)
  btn_c.config(bg="white")

#window
win = tk.Tk()
win.title("Calculator")
win.geometry("600x600")
win.configure(bg="#5FBDFF")
win.resizable(False, False)

#Label
tk.Label(win, text="Calculator", font=("Sans Serif", 14)).place(x=250, y=20)

#Entry
ent_field = tk.Entry(win, font=("Sans Serif", 20))
ent_field.place(x=150, y=60, width=300,)

#Buttons
btn_0 = tk.Button(win, text=0, font=("Sans Serif", 20), command=lambda: ent_field.insert(tk.END, "0"), bg="white")
btn_1 = tk.Button(win, text=1, font=("Sans Serif", 20), command=lambda: ent_field.insert(tk.END, "1"), bg="white")
btn_2 = tk.Button(win, text=2, font=("Sans Serif", 20), command=lambda: ent_field.insert(tk.END, "2"), bg="white")
btn_3 = tk.Button(win, text=3, font=("Sans Serif", 20), command=lambda: ent_field.insert(tk.END, "3"), bg="white")
btn_4 = tk.Button(win, text=4, font=("Sans Serif", 20), command=lambda: ent_field.insert(tk.END, "4"), bg="white")
btn_5 = tk.Button(win, text=5, font=("Sans Serif", 20), command=lambda: ent_field.insert(tk.END, "5"), bg="white")
btn_6 = tk.Button(win, text=6, font=("Sans Serif", 20), command=lambda: ent_field.insert(tk.END, "6"), bg="white")
btn_7 = tk.Button(win, text=7, font=("Sans Serif", 20), command=lambda: ent_field.insert(tk.END, "7"), bg="white")
btn_8 = tk.Button(win, text=8, font=("Sans Serif", 20), command=lambda: ent_field.insert(tk.END, "8"), bg="white")
btn_9 = tk.Button(win, text=9, font=("Sans Serif", 20), command=lambda: ent_field.insert(tk.END, "9"), bg="white")
btn_c = tk.Button(win, text="C", font=("Sans Serif", 20), command=clear, bg="white")
btn_plus = tk.Button(win, text="+", font=("Sans Serif", 20), command=lambda: ent_field.insert(tk.END, "+"), bg="white")
btn_minus = tk.Button(win, text="-", font=("Sans Serif", 20), command=lambda: ent_field.insert(tk.END, "-"), bg="white")
btn_divide = tk.Button(win, text="÷", font=("Sans Serif", 20), command=lambda: ent_field.insert(tk.END, "÷"), bg="white")
btn_multiply = tk.Button(win, text="x", font=("Sans Serif", 20), command=lambda: ent_field.insert(tk.END, "x"), bg="white")
btn_enter = tk.Button(win, text="Enter / =", font=("Sans Serif", 20), command=calculate, bg="white")
btn_backspace = tk.Button(win, text="Del", font=("Sans Serif", 14), command=backspace)

#Button Place
btn_0.place(x=110, y=380, width=180)
btn_1.place(x=110, y=300, width=80)
btn_2.place(x=210, y=300, width=80)
btn_3.place(x=310, y=300, width=80)
btn_4.place(x=110, y=220, width=80)
btn_5.place(x=210, y=220, width=80)
btn_6.place(x=310, y=220, width=80)
btn_7.place(x=110, y=140, width=80)
btn_8.place(x=210, y=140, width=80)
btn_9.place(x=310, y=140, width=80)
btn_c.place(x=310, y=380, width=80)
btn_minus.place(x=410, y=140, width=80)
btn_plus.place(x=410, y=220, width=80)
btn_multiply.place(x=410, y=300, width=80)
btn_divide.place(x=410, y=380, width=80)
btn_enter.place(x=140, y=460, width=300)
btn_backspace.place(x=460, y=60, width=80)

#Window Loop
win.mainloop()
