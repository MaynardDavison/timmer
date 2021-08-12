from datetime import datetime
import tkinter


'v2'

'v4'
def gettime():
    """
    test


    Returns: None

    """
    timestr = datetime.now().strftime("%H:%M:%S")  # 获取当前的时间并转化为字符串
    lb.configure(text=timestr)
    time_datetype = datetime.strptime(timestr, "%H:%M:%S")
    root.after(5000, gettime)  # 每隔1s调用函数gettime自身获取时间
    # 设置标识符
    flag = 0
    for i in timedict:
        temp = datetime.strptime(i, "%H:%M:%S")
        if time_datetype >= temp:  # 这里会赋值多次，但是结果是可以的
            lb2.configure(text=timedict[i])
            flag = 1
    if flag == 1:
        flag = 0
    else:
        lb2.configure(text="睡觉")

# def speak(text):
#     #语音
#     import pyttsx3
#     speaker=pyttsx3.init()
#     speaker.setProperty('rate',120)
#     speaker.setProperty('volume',1)#音量
#     speaker.say(text)
#     speaker.runAndWait()
#     #音乐


if __name__ == '__main__':
    timedict = {'08:00:00': '早餐', '08:30:00': '口语', '09:00:00': '数学', '11:30:00': '午饭', '12:00:00': '单词',
                '12:30:00': '午觉', '13:30:00': '英语', '16:00:00': '力扣', '17:00:00': '公考与国策', '18:00:00': '晚饭',
                '18:30:00': '休息', '19:00:00': '健身', '20:30:00': '洗澡', '21:00:00': '钢琴', '22:00:00': '阅读',
                '22:30:00': '回复消息', '23:00:00': '睡觉'}
    root = tkinter.Tk()
    root.title("时钟")
    # root.iconbitmap('head.ico')

    lb = tkinter.Label(root, text='', fg='black', font=("黑体", 80))
    lb2 = tkinter.Label(root, text='', fg='black', font=("黑体", 60))

    lb.pack()
    lb2.pack()
    gettime()
    root.mainloop()
