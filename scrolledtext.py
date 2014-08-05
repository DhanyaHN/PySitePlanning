
__all__ = ['ScrolledText']

from tkinter import *
from tkinter.constants import RIGHT, LEFT, Y, BOTH

class ScrolledText(Text):
    def __init__(self, master=None, **kw):
        self.frame = Frame(master)
        self.vbar = Scrollbar(self.frame)
        self.vbar.pack(side=RIGHT, fill=Y)

        kw.update({'yscrollcommand': self.vbar.set})
        Text.__init__(self, self.frame, **kw)
        self.pack(side=LEFT, fill=BOTH, expand=True)
        self.vbar['command'] = self.yview
        # Copy geometry methods of self.frame without overriding Text
        # methods -- hack!
        text_meths = vars(Text).keys()
        methods = vars(Pack).keys() | vars(Grid).keys() | vars(Place).keys()
        methods = methods.difference(text_meths)

        for m in methods:
            if m[0] != '_' and m != 'config' and m != 'configure':
                setattr(self, m, getattr(self.frame, m))

    def __str__(self):
        print(str(self.frame))
        return str(self.frame)

def example():
    from tkinter.constants import END
    root = Tk()
    stext = ScrolledText(root ,bg='white', height=10)
    f = open("file1.txt","r")
    f1 = f.read()
    stext.insert(END, f1)
    f.close()
    stext.pack(fill=BOTH, side=LEFT, expand=True)
    stext.focus_set()
    b = Button(text = "hi")
    b.pack()
    print(Text.get(stext,"1.0",'end'))
    stext.mainloop()

if __name__ == "__main__":
    example()
