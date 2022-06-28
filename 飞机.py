'''
实现飞机的显示，并且可以控制飞机的移动
'''
import pygame.image

from BasePlane import BasePlane
from 子弹 import bullet


class HeroPlane(BasePlane):
    def __init__(self,screen):
        '''
        初始化函数
        :param screen:主窗口的对象
        '''
        super(HeroPlane, self).__init__(screen,'./feiji/hero.png')
        #飞机初始横坐标
        self.x=160
        #飞机初始纵坐标
        self.y=461
        pass
    def moveleft(self):
        '''
        向左移动
        :return:
        '''
        if self.x>0:
            self.x-=10
            pass
        pass
    def moveright(self):
        '''
        向右移动
        :return:
        '''
        if self.x<=310:
            self.x+=10
        pass