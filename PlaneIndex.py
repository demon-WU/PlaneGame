import pygame
#导入pygame包
from pygame.locals import *
#导入包中所有的东西

'''
实现飞机的显示，并且可以控制飞机的移动
'''
class HeroPlane(object):
    def __init__(self,screen):
        '''
        初始化函数
        :param screen:主窗口的对象
        '''
        self.x=160
        #飞机初始横坐标
        self.y=461
        #飞机初始纵坐标
        self.screen=screen
        #设置要显示在哪里的窗口
        pass
    def moveleft(self):
        '''
        向左移动
        :return:
        '''
        pass
    def moveright(self):
        '''
        向右移动
        :return:
        '''
        pass
    def display(self):
        '''
        飞机在主窗口的显示
        :return:
        '''
        pass

    pass



def main():
    '''
    创建一个窗口
    :return:
    '''
    # 设定窗口大小
    screen=pygame.display.set_mode((350,500),depth=32)

    # 设定背景图片
    background=pygame.image.load('./feiji/背景.png')

    # 设置窗口标题
    pygame.display.set_caption('双人飞机大战')

    #设置背景音乐
    pygame.mixer.init()
    # 初始化音乐模块
    pygame.mixer.music.load('./feiji/backgroundMusic.mp3')
    #设置音乐路径
    pygame.mixer.music.play(-1)
    #设置音乐循环次数

    #设定飞机模型
    hero=pygame.image.load('./feiji/hero.png')
    #设定飞机模型初始位置
    x,y=160,461
    while True:

        # 设定窗口背景居中显示
        screen.blit(background,(0,0))
        #设定飞机位置
        screen.blit(hero,(x,y))
        #设定键盘事件
        eventList=pygame.event.get()
        for event in eventList:
            if  event.type==QUIT:
                print('退出游戏')
                #退出程序
                exit()
                pass
            elif event.type==KEYDOWN:
                if event.key==K_a or event.key==K_LEFT:
                    print('向左移动')
                    pass
                elif event.key==K_d or event.key==K_RIGHT:
                    print('向右移动')
                    pass
                elif event.key==K_SPACE:
                    print('发射子弹')
                    pass

        # 设定刷新窗口
        pygame.display.update()

    pass


if __name__=='__main__':
    main()