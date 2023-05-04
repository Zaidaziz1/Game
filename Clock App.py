import tkinter as tk
import time

class DigitalClock(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.update_clock()

    def create_widgets(self):
        self.clock_label = tk.Label(self.master, font=('Arial', 80), bg='black', fg='white')
        self.clock_label.pack(fill='both', expand=True)

    def update_clock(self):
        current_time = time.strftime('%H:%M:%S')
        self.clock_label.config(text=current_time)
        self.master.after(1000, self.update_clock)

root = tk.Tk()
root.title('Digital Clock')
root.geometry('600x200')
root.config(bg='black')

digital_clock = DigitalClock(root)
digital_clock.pack(fill='both', expand=True)

root.mainloop()
