import pygame  #导入pygame包

#导入包中所有的东西
from pygame.locals import *

from 敌机 import EnemyPlane
from 飞机 import HeroPlane
#键盘控制函数

def keyboardControl(HeroObj):
    eventList = pygame.event.get()
    for event in eventList:
        if event.type ==QUIT:
            print('退出游戏')
            # 退出程序
            exit()
            pass
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('向左移动')
                HeroObj.moveleft()
                pass
            elif event.key == K_d or event.key == K_RIGHT:
                print('向右移动')
                HeroObj.moveright()
                pass
            elif event.key == K_SPACE:
                print('发射子弹')
                HeroObj.shootBullet()
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

    # 初始化音乐模块
    pygame.mixer.init()

    #设置音乐路径
    pygame.mixer.music.load('./feiji/backgroundMusic.mp3')
    #设置音乐循环次数
    pygame.mixer.music.play(-1)
    #设定飞机模型
    hero=HeroPlane(screen)
    #设定敌机模型
    enemyPlane=EnemyPlane(screen)
    while True:

        # 设定窗口背景居中显示
        screen.blit(background,(0,0))

        #设定飞机位置
        hero.display()
        #设定敌机显示
        enemyPlane.display()
        #设定敌机的移动
        enemyPlane.move()
        #设定敌机发射子弹
        enemyPlane.shootEnemyBullet()
        #设定键盘事件
        keyboardControl(hero)
        # 设定刷新窗口，让子弹和飞机动起来
        pygame.display.update()

    pass


if __name__=='__main__':
    main()
    pass