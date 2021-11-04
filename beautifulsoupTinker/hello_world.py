import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_wideget()
        
    def create_wideget(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello Class\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        
        self.quit.pack(side="bottom")
        
    def say_hi(self):
        print("여러분 안녕하세요")
        
root = tk.Tk()
app = Application(master=root)
app.mainloop()


