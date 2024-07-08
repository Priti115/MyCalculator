from tkinter import Tk, Entry, Button, StringVar

# Convert RGB to hexadecimal color
unique_rgb = "#a1a6a5"  # (123, 104, 238) in hexadecimal

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry('400x450')
        master.config(bg='pink')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(master, width=30, bg=unique_rgb, font=('Arial', 20), textvariable=self.equation).place(x=0, y=0)
        
        # Adding Buttons for demonstration
        Button(master, text='1',width=6,height=2,command=lambda: self.show(1)).place(x=10, y=50)
        Button(master, text='2',width=6,height=2, command=lambda: self.show(2)).place(x=90, y=50)
        Button(master, text='3',width=6,height=2, command=lambda: self.show(3)).place(x=170, y=50)
        Button(master, text='4',width=6,height=2, command=lambda: self.show(4)).place(x=250, y=50)
        Button(master, text='C',width=6,height=2,bg='red', command=self.clear).place(x=330, y=50)

        Button(master, text='5',width=6,height=2, command=lambda: self.show(4)).place(x=10, y=100)
        Button(master, text='6',width=6,height=2, command=lambda: self.show(6)).place(x=90, y=100)
        Button(master, text='7',width=6,height=2, command=lambda: self.show(7)).place(x=170, y=100)
        Button(master, text='8',width=6,height=2, command=lambda: self.show(8)).place(x=250, y=100)
        Button(master, text='+',width=6,height=2, command=lambda: self.show('+')).place(x=330, y=100)

        Button(master, text='9',width=6,height=2, command=lambda: self.show(9)).place(x=10, y=150)
        Button(master, text='0',width=6,height=2, command=lambda: self.show(0)).place(x=90, y=150)
        Button(master, text='00',width=6,height=2, command=lambda: self.show(00)).place(x=170, y=150)
        Button(master, text='.',width=6,height=2, command=lambda: self.show('.')).place(x=250, y=150)
        Button(master, text='-',width=6,height=2, command=lambda: self.show('-')).place(x=330, y=150)

        Button(master, text='%',width=6,height=2, command=lambda: self.show('%')).place(x=10, y=200)
        Button(master, text='^',width=6,height=2, command=lambda: self.show('^')).place(x=90, y=200)
        Button(master, text='(',width=6,height=2, command=lambda: self.show('(')).place(x=170, y=200)
        Button(master, text=')',width=6,height=2, command=lambda: self.show(')')).place(x=250, y=200)
        Button(master, text='*',width=6,height=2, command=lambda: self.show('*')).place(x=330, y=200)
        
        Button(master, text='[',width=6,height=2, command=lambda: self.show('[')).place(x=10, y=250)
        Button(master, text=']',width=6,height=2, command=lambda: self.show(']')).place(x=90, y=250)
        Button(master, text='{',width=6,height=2, command=lambda: self.show('{')).place(x=170, y=250)
        Button(master, text='}',width=6,height=2, command=lambda: self.show('}')).place(x=250, y=250)
        Button(master, text='/',width=6,height=2, command=lambda: self.show('/')).place(x=330, y=250)
        
        Button(master, text='!',width=6,height=2, command=lambda: self.show('!')).place(x=10, y=300)
        Button(master, text='x',width=6,height=2, command=lambda: self.show('x')).place(x=90, y=300)
        Button(master, text='y',width=6,height=2, command=lambda: self.show('y')).place(x=170, y=300)
        Button(master, text='sin',width=6,height=2, command=lambda: self.show('sin')).place(x=250, y=300)
        Button(master, text='=',width=6,height=2,bg='green', command=self.solve).place(x=330, y=300)
        
        
    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)
    
    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception as e:
            self.equation.set("Error")

root = Tk()
calculator = Calculator(root)
root.mainloop()
