import pygame
#导入pygame包
from pygame.locals import *
#导入包中所有的东西
def main():
    '''
    创建一个窗口
    :return:
    '''
    screen=pygame.display.set_mode((350,500))
    #设定窗口大小
    background=pygame.image.load('./feiji/背景.png')
    #设定背景图片
    pygame.display.set_caption('双人飞机大战')
    #设置窗口标题
    while True:
        screen.blit(background,(0,0))
        #设定图片居中显示
        pygame.display.update()
        #设定刷新窗口
    pass
main()