from datetime import datetime
import tkinter

def creat_window(timedict):
    """
    test

    Returns: None

    """

    # 获取用于比较的时间表临时列表
    timelistForCompare = []
    for i in timedict:
        temp = datetime.strptime(i, "%H:%M:%S")
        timelistForCompare.append(temp)

    #获取时间戳 与事件索引
    timestr, timeindex = get_data(timelistForCompare)

    #tk 初始化
    root = tkinter.Tk()
    root.title("时钟")
    lb = tkinter.Label(root, text='', fg='black', font=("黑体", 80))
    lb2 = tkinter.Label(root, text='', fg='black', font=("黑体", 60))
    lb.pack()
    lb2.pack()

    def show():
        #显示
        lb.configure(text=timestr)

        if timeindex:#如果存在
            lb2.configure(text=list(timedict.values())[timeindex])#取values的第timeindex个的值,需转成list，dict不行
        else:
            lb2.configure(text="睡觉")


    #设置5s延时
    root.after(5000, show())  # 每隔5获取值

    #开始循环
    root.mainloop()


def get_data(timelistForCompare):
    # 获取当前时间
    timestr = datetime.now().strftime("%H:%M:%S")  # 获取当前的时间并转化为字符串

    #获取用于比较的当前时间
    time_datetype = datetime.strptime(timestr, "%H:%M:%S")

    #插入用于比较的当前时间进行排序获取id号
    timelistForCompare.append(time_datetype)
    timeindex=sorted(timelistForCompare).index(time_datetype)

    #输出时间字符和对应序号，睡觉用None表示
    if timeindex==0 & timeindex== len(timelistForCompare):
        return timestr, None
    return timestr, timeindex-1#-1是因为列表里面加了临时的



