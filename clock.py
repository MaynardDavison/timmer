import threading
from datetime import datetime
import tkinter

def refresh():

    # 获取用于比较的时间表临时列表
    timelistForCompare = []
    for i in timedict:
        temp = datetime.strptime(i, "%H:%M:%S")
        timelistForCompare.append(temp)
    # 获取当前时间
    timestr = datetime.now().strftime("%H:%M:%S")  # 获取当前的时间并转化为字符串

    #获取用于比较的当前时间
    time_datetype = datetime.strptime(timestr, "%H:%M:%S")

    #插入用于比较的当前时间进行排序获取id号
    timelistForCompare.append(time_datetype)
    timeindex=sorted(timelistForCompare).index(time_datetype)

    #输出时间字符和对应序号，睡觉用None表示
    if timeindex==0 or timeindex== len(timelistForCompare):
        timeindex=None
    else:
        timeindex=timeindex-1#-1是因为列表里面加了临时的

    #显示
    lb.configure(text=timestr)

    if timeindex:#如果存在
        lb2.configure(text=list(timedict.values())[timeindex])#取values的第timeindex个的值,需转成list，dict不行
    else:
        lb2.configure(text="睡觉")

    # 设置5s延时
    root.after(5000, refresh)#不能嵌套多个def

#设置成全局参数，为了after能正常运行
timedict = {'08:00:00': '早餐', '08:30:00': '口语', '09:00:00': '数学', '11:30:00': '午饭', '12:00:00': '单词',
        '12:30:00': '午觉', '13:30:00': '英语', '16:00:00': '力扣', '17:00:00': '公考与国策', '18:00:00': '晚饭',
        '18:30:00': '休息', '19:00:00': '健身', '20:30:00': '洗澡', '21:00:00': '钢琴', '22:00:00': '阅读',
        '22:30:00': '回复消息', '23:00:00': '睡觉'}
# tk 初始化
root = tkinter.Tk()
root.title("时钟")
lb = tkinter.Label(root, text='', fg='black', font=("黑体", 80))
lb2 = tkinter.Label(root, text='', fg='black', font=("黑体", 60))
lb.pack()
lb2.pack()


#生成函数出口供调用
def creat_window():
    #开始循环
    refresh()
    root.mainloop()



# def clock_app():
#     timedict = {'08:00:00': '早餐', '08:30:00': '口语', '09:00:00': '数学', '11:30:00': '午饭', '12:00:00': '单词',
#                 '12:30:00': '午觉', '13:30:00': '英语', '16:00:00': '力扣', '17:00:00': '公考与国策', '18:00:00': '晚饭',
#                 '18:30:00': '休息', '19:00:00': '健身', '20:30:00': '洗澡', '21:00:00': '钢琴', '22:00:00': '阅读',
#                 '22:30:00': '回复消息', '23:00:00': '睡觉'}
#     root = tkinter.Tk()
#     root.title("时钟")
#     # root.iconbitmap('head.ico')
#
#     lb = tkinter.Label(root, text='', fg='black', font=("黑体", 80))
#     lb2 = tkinter.Label(root, text='', fg='black', font=("黑体", 60))
#
#     lb.pack()
#     lb2.pack()
#
#     timestr = datetime.now().strftime("%H:%M:%S")  # 获取当前的时间并转化为字符串
#     lb.configure(text=timestr)
#     time_datetype = datetime.strptime(timestr, "%H:%M:%S")
#     root.after(5000, clock_app)  # 每隔1s调用函数gettime自身获取时间
#     # 设置标识符
#     flag = 0
#     for i in timedict:
#         temp = datetime.strptime(i, "%H:%M:%S")
#         if time_datetype >= temp:  # 这里会赋值多次，但是结果是可以的
#             lb2.configure(text=timedict[i])
#             flag = 1
#     if flag == 1:
#         flag = 0
#     else:
#         lb2.configure(text="睡觉")
