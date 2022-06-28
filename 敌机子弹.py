'''
创建敌机子弹类
'''
import pygame.image

from BaseButtle import BaseButtle


class enemyBullet(BaseButtle):
    def __init__(self,screen,x,y):
        '''

        :param screen: 窗口对象
        :param x: 飞机横坐标
        :param y: 飞机纵坐标
        '''
        super(enemyBullet, self).__init__(screen,'./feiji/子弹1.png')
        #设置初始横坐标
        self.x=x+13
        # 设置初始纵坐标
        self.y=y+20
        pass
    def move(self):
        '''
        子弹位移
        :return:
        '''
        self.y+=0.1
        pass
