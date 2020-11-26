import tkinter as tk
root = tk.Tk()
msg = "Welcome to Biocrux Cigarette bud Recycling Zone.\nPlease extinguish and drop your Cigarette bud here"
root.title("Cigarette Bud Crusher: BioCrux")

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

frame.columnconfigure(1, weight=1)
frame.rowconfigure(1, weight=1)

row0 = tk.Label(frame, text=" ")
welcomeScreen = tk.Label(frame, text=msg)
row2 = tk.Label(frame, text=" ")

row0.grid(row=0, column=1, padx=5, pady=5)
welcomeScreen.grid(row=1, column=1, padx=5, pady=5)
row2.grid(row=2, column=2, padx=5, pady=5)


root.mainloop()
