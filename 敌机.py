import pygame
import random   #随机产生

from 敌机子弹 import enemyBullet


class EnemyPlane:
    def __init__(self,screen):
        '''
        敌机构造函数
        :param screen: 传主窗口对象进来
        '''
        #默认方向:right
        self.direction='right'
        self.x=0
        self.y=0
        self.bulletList=[]
        self.screen = screen
        self.image = pygame.image.load('./feiji/敌机.jpg')
        pass
    def display(self):
        '''
        敌机以及子弹显示函数
        :return:
        '''
        self.screen.blit(self.image,(self.x,self.y))
        # 需要删除超出界面的子弹
        needDelitemList = []
        # 循环遍历超出界面的子弹进入needDelitemList[]
        for item in self.bulletList:
            if item.judge():
                needDelitemList.append(item)
                pass
            pass
        # 循环遍历删除列表中的子弹
        for i in needDelitemList:
            needDelitemList.remove(i)
            pass
        # 对列表中符合条件的子弹进行显示并移动
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()
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
