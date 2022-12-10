from tkinter import *

root = Tk()
root.title("Test2")
root.config(bg="blue")

main_frame = Frame(root, width=800, height=600)
main_frame.grid(row=0, column=0)
main_frame.config(bg="red")
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

left_frame = Frame(main_frame, width=300, height=300)
left_frame.grid(row=0, column=0)
left_frame.config(bg="skyblue")

right_frame = Frame(main_frame, width=300, height=300)
right_frame.grid(row=0, column=1)
right_frame.config(bg="limegreen")

root.mainloop()
