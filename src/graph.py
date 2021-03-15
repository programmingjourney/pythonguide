import tkinter as tk

class Example(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack(side="top", fill="both", expand=True)

        # draw some items
        self.canvas.create_rectangle(50, 50, 150, 150, fill="red")
        self.canvas.create_oval(20, 20, 65, 75, outline="green")
        self.canvas.create_text(10, 200, anchor="nw", text="Hello, world")

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()