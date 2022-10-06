import types

import numpy
import random
from tkinter import ttk
from tkinter import Frame, Tk, BOTH, Text, Button, END
from tkinter import filedialog
from sort import InsertionSort, BubbleSort
from datetime import datetime


def Check(s):
    a = [int(x) for x in s.split()]
    for i in a:
        if isinstance(i, int):
            return True
    return False


def DelLit(s):
    line = s.replace('[', '')
    line = line.replace(']', '')
    line = line.replace(',', '')
    return line


class Main_Window(Frame):
    def __init__(self):
        super().__init__()
        self.Box = None
        self.initUI()

    def initUI(self):
        self.master.title("Сортировка массивов")
        self.pack(fill=BOTH, expand=1)

        self.Browser = Button(text='Загрузить файл', command=self.BrowseFile)
        self.Browser.place(x=70, y=335, width=120, height=50)

        self.Bubblebtn = Button(text='Пузырьковая сортировка', command=self.BubbleSort)
        self.Bubblebtn.place(x=520, y=335, width=150, height=50)

        self.Insertbtn = Button(text='Сортировка вставкой', command=self.InsertSort)
        self.Insertbtn.place(x=720, y=335, width=130, height=50)

        self.CreateArr = Button(text='Сгенерировать массив', command=self.Generate)
        self.CreateArr.place(x=250, y=335, width=135, height=50)

        self.CreatFile = Button(text='Выгрузить в файл', command=self.CreateFile)
        self.CreatFile.place(x=860, y=150, width=120, height=50)

        self.input = Text(
            width=50,
            height=20
        )
        self.input.place(x=20, y=5)

        self.output = Text(
            width=50,
            height=20
        )
        self.output.place(x=450, y=5)

        self.log = Text(
            width=104,
            height=10
        )
        self.log.place(x=20, y=400)

        number = (10, 50, 100, 500, 1000, 5000)
        self.Box = ttk.Combobox(values=number)
        # self.Box.grid(column=0,row=1)
        self.Box.current(0)
        self.Box.place(x=430, y=350, width=50)

    def Generate(self):
        self.input.delete(1.0, END)
        i = 0
        a = []
        curr = self.Box.get()
        while i < int(curr):
            x = random.randint(-500, 500)
            a.append(x)
            i += 1
        self.input.insert(1.0, str(a))

    def BrowseFile(self):
        self.input.delete(1.0, END)
        ftypes = (('text files', '*.txt'),
                  ('All files', '*.*'))
        f = filedialog.askopenfile(
            title='Open a file',
            initialdir=r'C:\Users\guy20\Desktop\Python_Labs\pythonProject\lab3',
            filetypes=ftypes
        )
        if f != None:
            s = f.read()
            if Check(s):
                self.input.insert(1.0, s)
            else:
                res = 'Ошибка! Найдена буква!'
                self.log.insert(1.0, res)
            f.close()

    def CreateFile(self):
        ftypes = (('text files', '*.txt'),
                  ('All files', '*.*'))
        file_name = filedialog.asksaveasfilename(
            title='Open a file',
            initialdir=r'C:\Users\guy20\Desktop\Python_Labs\pythonProject\lab3',
            filetypes=ftypes
        )
        if file_name != '':
            f = open(file_name, 'w')
            text = self.output.get(1.0, END)
            f.write(text)
            f.close()

    def BubbleSort(self):
        self.output.delete(1.0, END)
        self.log.delete(1.0, END)
        start = datetime.now()
        text = self.input.get(1.0, END)
        text = DelLit(text)
        a = [int(x) for x in text.split()]
        res = BubbleSort(a)
        self.output.insert(1.0, res)
        end = datetime.now()
        s = 'Duration: {}'.format(end - start)
        self.log.insert(1.0, s)

    def InsertSort(self):
        self.log.delete(1.0, END)
        self.output.delete(1.0, END)
        start = datetime.now()
        text = self.input.get(1.0, END)
        text = DelLit(text)
        a = [int(x) for x in text.split()]
        res = InsertionSort(a)
        self.output.insert(1.0, res)
        end = datetime.now()
        s = 'Duration: {}'.format(end - start)
        self.log.insert(1.0, s)


def main():
    root = Tk()
    win = Main_Window()
    root.geometry('1000x600')
    root.resizable('false', 'false')
    root.mainloop()


if __name__ == '__main__':
    main()
