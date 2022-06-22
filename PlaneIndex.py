import pygame
#导入pygame包
from pygame.locals import *
#导入包中所有的东西
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

    while True:

        # 设定窗口背景居中显示
        screen.blit(background,(0,0))
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