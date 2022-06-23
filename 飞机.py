'''
实现飞机的显示，并且可以控制飞机的移动
'''
import pygame.image

from 子弹 import bullet


class HeroPlane(object):
    def __init__(self,screen):
        '''
        初始化函数
        :param screen:主窗口的对象
        '''
        #飞机初始横坐标
        self.x=160
        #飞机初始纵坐标
        self.y=461
        #设置要显示在哪里的窗口
        self.screen=screen
        #导入飞机图片
        self.image =pygame.image.load('./feiji/hero.png')
        #存放子弹轨迹的列表
        self.bulletList=[]
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
    def display(self):
        '''
        飞机在主窗口的显示
        :return:
        '''
        #载入飞机的图片及其位置
        self.screen.blit(self.image,(self.x,self.y))
        #完善子弹的展示逻辑

        #需要删除超出界面的子弹
        needDelitemList=[]
        #循环遍历超出界面的子弹进入needDelitemList[]
        for item in self.bulletList:
            if item.judge():
                needDelitemList.append(item)
                pass
            pass
        #循环遍历删除列表中的子弹
        for i in needDelitemList:
            needDelitemList.remove(i)
            pass
        #对列表中符合条件的子弹进行显示并移动
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()
        pass
    def shootbullet(self):
        '''
        发射子弹
        :return:
        '''
        newBullet=bullet(self.screen,self.x,self.y)
        self.bulletList.append(newBullet)
        pass

    pass