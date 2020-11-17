
import tkinter as tk
from Projects.screenOCR.view.view import App


if __name__ == '__main__':

    # --创建实例
    root = tk.Tk()

    app = App()
    app.pack()

    root.title("文字识别")
    root.geometry('500x300')
    root.mainloop()
