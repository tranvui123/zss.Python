from tkinter import *


class Paint(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.color = "black"
        self.brush_size = 2
        self.setUI()

    def set_color(self, new_color):
        self.color = new_color

    def set_brush_size(self, new_size):
        self.brush_size = new_size

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)

    def setUI(self):

        self.parent.title(".............")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(6, weight=1)
        self.rowconfigure(2, weight=1)

        self.canv = Canvas(self, bg="white")
        self.canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=5, sticky=E+W+S+N)
        self.canv.bind("<B1-Motion>", self.draw)

        color_lab = Label(self, text="Color: ")
        color_lab.grid(row=0, column=0, padx=6)

        red_btn = Button(self, text="Red", width=10,
                         command=lambda: self.set_color("red"))
        red_btn.grid(row=0, column=1)

        yellow_btn = Button(self, text="Yellow", width=10,
                         command=lambda: self.set_color("yellow"))
        yellow_btn.grid(row=0, column=2)

        blue_btn = Button(self, text="Blue", width=10,
                         command=lambda: self.set_color("blue"))
        blue_btn.grid(row=0, column=3)

        purple_btn = Button(self, text="Purple", width=10,
                         command=lambda: self.set_color("purple"))
        purple_btn.grid(row=0, column=4)

        clear_btn = Button(self, text="Clear all", width=10,
                           command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=6, sticky=W)

        size_lab = Label(self, text="Brush size: ")
        size_lab.grid(row=1, column=0, padx=5)
        one_btn = Button(self, text="Two", width=10,
                         command=lambda: self.set_brush_size(2))
        one_btn.grid(row=1, column=1)

        two_btn = Button(self, text="Five", width=10,
                         command=lambda: self.set_brush_size(5))
        two_btn.grid(row=1, column=2)

        three_btn = Button(self, text="Ten", width=10,
                         command=lambda: self.set_brush_size(10))
        three_btn.grid(row=1, column=3)

        four_btn = Button(self, text="Fiveteen", width=10,
                         command=lambda: self.set_brush_size(15))
        four_btn.grid(row=1, column=4)



def main():
    root = Tk()
    root.geometry("850x500+300+300")
    app = Paint(root)
    root.mainloop()
if __name__ == '__main__':
    main()