import tkinter as tk

window = tk.Tk()
window.geometry("300x150")
window.title("Tic Tac Toe")


def action(button):

    if btns[button].cget('text') == '-':
        btns[button].configure(text='X')

    else:
        btns[button].configure(text='-')


btn_nr = -1
btns = []

for x in range(1, 4):

    for y in range(1, 4):

        btn_nr += 1
        print(btn_nr)

        btns.append(tk.Button(text='-', command=lambda x=btn_nr: action(x)))
        btns[btn_nr].grid(row=x, column=y)

exit_button = tk.Button(text='Exit Game', command=window.destroy)
exit_button.grid(row=4, column=1, columnspan=15)

window.mainloop()