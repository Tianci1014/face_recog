import tkinter as tk
import time

def collect_name():
    """
    弹出输入框提示
    :return: 所输入的文本
    """
    name = ''

    root = tk.Tk()

    # 设置标签信息
    label1 = tk.Label(root, text='请输入姓名：')
    label1.grid(row=0, column=0)

    # 创建输入框
    entry1 = tk.Entry(root)
    entry1.grid(row=0, column=1, padx=10, pady=5)

    # 创建按键
    def reutrn_name():
        global name
        name = entry1.get()
        return name

    tk.Button(root, text='获取信息', command=reutrn_name).grid(row=3, column=0, sticky=tk.W, padx=30, pady=5)
    tk.Button(root, text='退出', command=root.quit).grid(row=3, column=1, sticky=tk.E, padx=30, pady=5)

    tk.mainloop()
    name = reutrn_name()
    return name

if __name__ == '__main__':
    name = collect_name()
    print(name)
