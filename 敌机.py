import pygame
import random   #随机产生

from BasePlane import BasePlane
from 敌机子弹 import enemyBullet


class EnemyPlane(BasePlane):
    def __init__(self,screen):
        '''
        敌机构造函数
        :param screen: 传主窗口对象进来
        '''
        super(EnemyPlane, self).__init__(screen,'./feiji/敌机.jpg')
        #默认方向:right
        self.direction='right'
        self.x=0
        self.y=0
        pass
    def shootEnemyBullet(self):
        '''
        敌机随机发射子弹
        :return:
        '''
        num=random.randint(1,2000)
        if num==3:
            newBullet=enemyBullet(self.screen,self.x,self.y)
            self.bulletList.append(newBullet)
        pass
    def move(self):
        '''
        敌机移动
        :return:
        '''
        if self.direction=='right':
            self.x+=0.01
            pass
        elif self.direction=='left':
            self.x-=0.01
            pass
        if self.x>350-30:
            self.direction='left'
            pass
        elif self.x<0:
            self.direction='right'
            pass
        pass
    pass
