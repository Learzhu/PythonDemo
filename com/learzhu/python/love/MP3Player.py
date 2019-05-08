import pygame
# pip install pygame

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

# playMusic('auido.mp3')
# playMusic('out.wav')
# playMusic("/resources/love_you_three_thousand.mp3")
# playMusic("E:\\PythonProjects\\PythonDemo\\resources\\love_you_three_thousand.mp3")
# //我们常用’/‘来表示相对路径，’\‘来表示绝对路径，上面的路径里\\是转义的意思
# playMusic("love_you_three_thousand.mp3")
# playMusic("http://m8.music.126.net/20190507212130/43d6e9a32e81715c69ab1edb3d763a50/ymusic/d94a/cb8c/5677/e0554d7146e58bf0bdc9cd33983cf3f8.mp3")