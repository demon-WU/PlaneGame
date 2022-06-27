'''
创建敌机子弹类
'''
import pygame.image
class enemyBullet(object):
    def __init__(self,screen,x,y):
        '''

        :param screen: 窗口对象
        :param x: 飞机横坐标
        :param y: 飞机纵坐标
        '''
        #设置初始横坐标
        self.x=x+13
        # 设置初始纵坐标
        self.y=y+20
        #设置显示在那个窗口对象中
        self.screen=screen
        # 图片读取
        self.image=pygame.image.load('./feiji/子弹.png')
        pass
    def display(self):
        '''
        子弹显示位置
        :return:
        '''
        # 设置子弹位置
        self.screen.blit(self.image,(self.x,self.y))
        pass
    def move(self):
        '''
        子弹位移
        :return:
        '''
        self.y+=0.1
        pass
    def judge(self):
        '''
        判断子弹是否越界
        :return:
        '''
        if self.y>=350:
            return True
        else:
            return False
    pass
