import tkinter as tk
import tkinter.filedialog
from tkinter import messagebox
def get_text_any_file(link):
    if (".txt" in link):

        f = open(link,"r", encoding="utf-8")
        print(1)
        text = ""
        add = f.readline()
        while(add):
            text+=add
            add = f.readline()

        return text
    raise Exception("Ошибка ошибки")

class MainWindowClass():
    def __init__(self,calc):
        self.root = tk.Tk()
        self.root.resizable(width=False, height=False)
        self.root.geometry("450x500")
        self.root.title("Анализатор текста")
        self.path = tk.StringVar()
        self.path_txt = ""
        self.text_label = [tk.StringVar() for i in range(7)]
        l = "абвгдеж"
        for i in range(len(self.text_label)):
            self.text_label[i].set(f"{l[i]}:")
        self.is_file = False
        self.calc = calc
        self.init__adds()

    def start(self):
        self.root.mainloop()

    def init__adds(self):
        self.draw_radio()
        self.draw_buttons()
        self.draw_categories()

    def draw_categories(self):
        tk.Label(text="Максимальные совпадения в каждой подтеме:").place(y=150, x=40)
        for i in range(7):
             tk.Label(textvariable = self.text_label[i]).place(y=170+20*i,x = 40)

        tk.Label(text="Результат:").place(y=150 + 20 * 9, x=10)
        self.res = tk.Text()
        self.res.place(y=150 + 20 * 10, x=0,height=100,width=450)

    def draw_radio(self):
        self.radio_var = tk.IntVar()
        def check():
            if self.radio_var.get()==1:
                self.is_file = True
                self.text.pack_forget()
                self.button__filedialog.pack()
                self.label__filedialog.pack()
            else:
                self.is_file = False
                self.label__filedialog.pack_forget()
                self.button__filedialog.pack_forget()
                self.text.pack()
        def get_path():

            self.path_txt = tkinter.filedialog.askopenfilenames()
            if self.path_txt:
                self.path_txt = self.path_txt[0]
                try:
                    print(self.path_txt)
                    text = get_text_any_file(self.path_txt)
                    self.text.delete(1.0, "end")
                    self.text.insert(1.0, text)
                    self.path.set(f"file:{self.path_txt.split('/')[-1]}")
                except:
                        messagebox.showerror('Python Error', 'Ошибка извлечения текста из файла')


        self.radio_var.set(1)
        self.radio__file = tk.Radiobutton(text="file",variable=self.radio_var, value=1,command=check)
        self.radio__text = tk.Radiobutton(text="text",variable=self.radio_var, value=2,command=check)
        self.text = tk.Text(height=5)
        self.label__filedialog = tk.Label(textvariable  = self.path)
        self.button__filedialog = tk.Button(text="Загрузить",command=get_path)
        self.radio__file.pack()
        self.radio__text.pack()
        check()

    def draw_buttons(self):
        self.submit__button = tk.Button(text = 'Классифицировать',command=lambda :self.calc(self.text_label,self.text.get("1.0",tk.END),self.res))
        self.submit__button.place(y = 465,x = 320)
