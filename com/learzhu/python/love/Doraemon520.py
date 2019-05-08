import time
import turtle
# import MP3Player
import pygame
import _thread

def flyTo(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def drawEye():
    turtle.tracer(False)
    a = 2.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
        else:
            a += 0.05
        turtle.left(3)
        turtle.fd(a)
    turtle.tracer(True)

def beard():
    """ 画胡子， 一共六根
    """
    # 左边第一根胡子
    flyTo(-37, 135)
    turtle.seth(165)
    turtle.fd(60)

    # 左边第二根胡子
    flyTo(-37, 125)
    turtle.seth(180)
    turtle.fd(60)

    # 左边第三根胡子
    flyTo(-37, 115)
    turtle.seth(193)
    turtle.fd(60)

    # 右边第一根胡子
    flyTo(37, 135)
    turtle.seth(15)
    turtle.fd(60)

    # 右边第二根胡子
    flyTo(37, 125)
    turtle.seth(0)
    turtle.fd(60)

    # 右边第三根胡子
    flyTo(37, 115)
    turtle.seth(-13)
    turtle.fd(60)

# 貌似只能播放单声道音乐，可能是pygame模块限制
def playMusic(filename, loops=0, start=0.0, value=0.5):
    """
    :param filename: 文件名
    :param loops: 循环次数
    :param start: 从多少秒开始播放
    :param value: 设置播放的音量，音量value的范围为0.0到1.0
    :return:
    """
    flag = False  # 是否播放过
    pygame.mixer.init()  # 音乐模块初始化
    while 1:
        if flag == 0:
            pygame.mixer.music.load(filename)
            # pygame.mixer.music.play(loops=0, start=0.0) loops和start分别代表重复的次数和开始播放的位置。
            pygame.mixer.music.play(loops=loops, start=start)
            pygame.mixer.music.set_volume(value)  # 来设置播放的音量，音量value的范围为0.0到1.0。
        if pygame.mixer.music.get_busy() == True:
            flag = True
        else:
            if flag:
                pygame.mixer.music.stop()  # 停止播放
                break
                
def drawRedScarf():
    """ 画围巾
    """
    turtle.fillcolor("red")  # 填充颜色
    turtle.begin_fill()
    turtle.seth(0)  # 朝向右

    turtle.fd(200)  # 前进10个单位
    turtle.circle(-5, 90)

    turtle.fd(10)
    turtle.circle(-5, 90)

    turtle.fd(207)
    turtle.circle(-5, 90)

    turtle.fd(10)
    turtle.circle(-5, 90)

    turtle.end_fill()


def drawMouse():
    flyTo(5, 148)
    turtle.seth(270)
    turtle.fd(100)
    turtle.seth(0)
    turtle.circle(120, 50)
    turtle.seth(230)
    turtle.circle(-120, 100)


def drawRedNose():
    flyTo(-10, 158)
    turtle.fillcolor("red")  # 填充颜色
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()


def drawBlackdrawEye():
    turtle.seth(0)
    flyTo(-20, 195)
    turtle.fillcolor("#000000")  # 填充颜色
    turtle.begin_fill()
    turtle.circle(13)
    turtle.end_fill()
    turtle.pensize(6)
    flyTo(20, 205)
    turtle.seth(75)
    turtle.circle(-10, 150)
    turtle.pensize(3)
    flyTo(-17, 200)
    turtle.seth(0)
    turtle.fillcolor("#ffffff")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    flyTo(0, 0)


def drawFace():
    """
    """
    turtle.forward(183)  # 前行183个单位
    turtle.fillcolor("white")  # 填充颜色为白色
    turtle.begin_fill()  # 开始填充
    turtle.left(45)  # 左转45度
    turtle.circle(120, 100)  # 右边那半边脸
    turtle.seth(90)  # 朝向向上
    drawEye()  # 画右眼睛
    turtle.seth(180)  # 朝向左
    turtle.penup()  # 抬笔
    turtle.fd(60)  # 前行60
    turtle.pendown()  # 落笔
    turtle.seth(90)  # 朝向上
    drawEye()  # 画左眼睛
    turtle.penup()  # 抬笔
    turtle.seth(180)  # 朝向左
    turtle.fd(64)  # 前进64
    turtle.pendown()  # 落笔
    turtle.seth(215)  # 修改朝向
    turtle.circle(120, 100)  # 左边那半边脸
    turtle.end_fill()  #


def drawHead():
    """ 画了一个被切掉下半部分的圆
    """
    turtle.penup()  # 抬笔
    turtle.circle(150, 40)  # 画圆, 半径150，圆周角40
    turtle.pendown()  # 落笔
    turtle.fillcolor("#00a0de")  # 填充色
    turtle.begin_fill()  # 开始填充
    turtle.circle(150, 280)  # 画圆，半径150, 圆周角280
    turtle.end_fill()

#以下部分为画爱心逻辑
# 画心形圆弧
def hart_arc():
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)

def move_pen_position(x, y):
    turtle.hideturtle()  # 隐藏画笔（先）
    turtle.up()  # 提笔
    turtle.goto(x, y)  # 移动画笔到指定起始坐标（窗口中心为0,0）
    turtle.down()  # 下笔
    turtle.showturtle()  # 显示画笔

def loveLi():
    # love = input("请输入表白话语，默认为‘I Love You’：")
    # signature = input("请签署你的大名，不填写默认不显示：")
    love=""
    signature="大朋友"
    if love == '':
        # love = 'I Love You \n\n Three Thousand'
        love = 'I Love You 3000'
    # 初始化
    # turtle.setup(width=800, height=500)  # 窗口（画布）大小
    turtle.setup(width=1000, height=800)  # 窗口（画布）大小
    turtle.color('red', 'pink')  # 画笔颜色
    turtle.pensize(3)  # 画笔粗细
    turtle.speed(1)  # 描绘速度
    # 初始化画笔起始坐标
    move_pen_position(x=0, y=-180)  # 移动画笔位置
    turtle.left(140)  # 向左旋转140度

    turtle.begin_fill()  # 标记背景填充位置

    # 画心形直线（ 左下方 ）
    turtle.forward(224)  # 向前移动画笔，长度为224
    # 画爱心圆弧
    hart_arc()  # 左侧圆弧
    turtle.left(120)  # 调整画笔角度
    hart_arc()  # 右侧圆弧
    # 画心形直线（ 右下方 ）
    turtle.forward(224)

    turtle.end_fill()  # 标记背景填充结束位置

    # 在心形中写上表白话语
    move_pen_position(0, 0)  # 表白语位置
    turtle.hideturtle()  # 隐藏画笔
    turtle.color('#CD5C5C', 'pink')  # 字体颜色
    # font:设定字体、尺寸（电脑下存在的字体都可设置）  align:中心对齐
    turtle.write(love, font=('Arial', 30, 'bold'), align="center")
    # 签写署名
    if signature != '':
     turtle.color('red', 'pink')
     time.sleep(2)
     move_pen_position(180, -180)
     turtle.hideturtle()  # 隐藏画笔
     turtle.write(signature, font=('Arial', 20), align="center")

def drawAll():
    drawHead()
    drawRedScarf()
    drawFace()
    drawRedNose()
    drawMouse()
    beard()
    flyTo(0, 0)
    turtle.seth(0)
    turtle.penup()
    turtle.circle(150, 50)
    turtle.pendown()
    turtle.seth(30)
    turtle.fd(40)
    turtle.seth(70)
    turtle.circle(-30, 270)
    turtle.fillcolor("#00a0de")
    turtle.begin_fill()
    turtle.seth(230)
    turtle.fd(80)
    turtle.seth(90)
    turtle.circle(1000, 1)
    turtle.seth(-89)
    turtle.circle(-1000, 10)
    turtle.seth(180)
    turtle.fd(70)
    turtle.seth(90)
    turtle.circle(30, 180)
    turtle.seth(180)
    turtle.fd(70)
    turtle.seth(100)
    turtle.circle(-1000, 9)
    turtle.seth(-86)
    turtle.circle(1000, 2)
    turtle.seth(230)
    turtle.fd(40)
    turtle.circle(-30, 230)
    turtle.seth(45)
    turtle.fd(81)
    turtle.seth(0)
    turtle.fd(203)
    turtle.circle(5, 90)
    turtle.fd(10)
    turtle.circle(5, 90)
    turtle.fd(7)
    turtle.seth(40)
    turtle.circle(150, 10)
    turtle.seth(30)
    turtle.fd(40)
    turtle.end_fill()

    # 左手
    turtle.seth(70)
    turtle.fillcolor("#FFFFFF")
    turtle.begin_fill()
    turtle.circle(-30)
    turtle.end_fill()

    # 脚
    flyTo(103.74, -182.59)
    turtle.seth(0)
    turtle.fillcolor("#FFFFFF")
    turtle.begin_fill()
    turtle.fd(15)
    turtle.circle(-15, 180)
    turtle.fd(90)
    turtle.circle(-15, 180)
    turtle.fd(10)
    turtle.end_fill()
    flyTo(-96.26, -182.59)
    turtle.seth(180)
    turtle.fillcolor("#FFFFFF")
    turtle.begin_fill()
    turtle.fd(15)
    turtle.circle(15, 180)
    turtle.fd(90)
    turtle.circle(15, 180)
    turtle.fd(10)
    turtle.end_fill()

    # 右手
    flyTo(-133.97, -91.81)
    turtle.seth(50)
    turtle.fillcolor("#FFFFFF")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

    # 口袋
    flyTo(-103.42, 15.09)
    turtle.seth(0)
    turtle.fd(38)
    turtle.seth(230)
    turtle.begin_fill()
    turtle.circle(90, 260)
    turtle.end_fill()
    flyTo(5, -40)
    turtle.seth(0)
    turtle.fd(70)
    turtle.seth(-90)
    turtle.circle(-70, 180)
    turtle.seth(0)
    turtle.fd(70)

    # 铃铛
    flyTo(-103.42, 15.09)
    turtle.fd(90)
    turtle.seth(70)
    turtle.fillcolor("#ffd200")
    turtle.begin_fill()
    turtle.circle(-20)
    turtle.end_fill()
    turtle.seth(170)
    turtle.fillcolor("#ffd200")
    turtle.begin_fill()
    turtle.circle(-2, 180)
    turtle.seth(10)
    turtle.circle(-100, 22)
    turtle.circle(-2, 180)
    turtle.seth(180 - 10)
    turtle.circle(100, 22)
    turtle.end_fill()
    flyTo(-13.42, 15.09)
    turtle.seth(250)
    turtle.circle(20, 110)
    turtle.seth(90)
    turtle.fd(15)
    turtle.dot(10)
    flyTo(0, -150)
    drawBlackdrawEye()
    loveLi()

def main():
    paintDoraemon()
    # try:
    #     # _thread.start_new_thread(MP3Player.playMusic("love_you_three_thousand.mp3"))
    #     _thread.start_new_thread(playMusic("love_you_three_thousand.mp3"))
    #     # _thread.start_new_thread(paintDoraemon())
    # except:
    #     print("Error: unable to start thread")
    playMusic("love_you_three_thousand.mp3")
def paintDoraemon():
    turtle.screensize(800, 6000, "#F0F0F0")
    turtle.pensize(3)
    turtle.speed(9)
    drawAll()


if __name__ == "__main__":
    main()
    turtle.mainloop()


