from tkinter import *

import tkinter.font as tkFont

from app import recognizeWords
from obj.Admin import Admin
from obj.Screen import Screen
import pyperclip


class App(Frame):
    alert_button = None
    info_text = None

    # --初始化
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    # --创建界面组件
    def createWidgets(self):
        self.alert_button = Button(self, text='框选识别', command=self.onclick)
        self.alert_button.pack(padx=50, pady=10)
        self.info_text = Text(self, font=tkFont.Font(family='微软雅黑', size=10, weight=tkFont.NORMAL))
        self.info_text.insert('insert', '操作指引：\n\n点击按钮后，使用鼠标左键框选需要识别的区域即可。\n\n识别成功后会自动添加到剪贴板。')
        self.info_text.pack(padx=20, pady=10)

    # --按钮响应事件
    def onclick(self):
        # 获取图片
        img_str = Screen().captureImage(need_save=False)
        self.info_text.delete(0.0, END)

        # 鉴权（获取token)
        token = Admin().accessToken()

        display_info = '\n'.join(recognizeWords(token, img_str))
        pyperclip.copy(display_info)

        self.info_text.insert('end', display_info)
        # messagebox.showinfo('OCR识别成功！', '内容已自动复制到了剪贴板。' or '识别失败！')




