import tkinter as tk

root = tk.Tk()

# 设置标签信息
label1 = tk.Label(root, text='战队名称：')
label1.grid(row=0, column=0)
label2 = tk.Label(root, text='选手名字：')
label2.grid(row=1, column=0)

# 创建输入框
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)


# 创建按键
def show():
    print('战队名称：%s' % entry1.get())
    print('选手名称：%s' % entry2.get())


button1 = tk.Button(root, text='获取信息', command=show).grid(row=3, column=0,
                                                              sticky=tk.W, padx=30, pady=5)
button2 = tk.Button(root, text='退出', command=root.quit).grid(row=3, column=1,
                                                               sticky=tk.E, padx=30, pady=5)

tk.mainloop()
