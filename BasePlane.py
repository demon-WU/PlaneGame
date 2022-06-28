import pygame.image

from 子弹 import bullet


class BasePlane:
    def __init__(self,screen,imagePath):
        '''
        构造父类函数
        :param screen:主窗口对象
        :param imagePath: 图片路径
        '''
        self.screen=screen
        self.imagePath=imagePath
        self.image=pygame.image.load(self.imagePath)
        self.bulletList=[]
        pass
    # def moveLeft(self):
    #     '''
    #     向左移动
    #     :return:
    #     '''
    #     if self.x>0:
    #         self.x-=10
    #         pass
    #     pass
    # def moveRight(self):
    #     '''
    #     向右移动
    #     :return:
    #     '''
    #     if self.x<=310:
    #         self.x+=10
    #         pass
    #     pass
    def display(self):
        '''
        飞机显示位置及子弹显示的位置
        :return:
        '''
        self.screen.blit(self.image,(self.x,self.y))
        needDelItemList=[]
        for item in self.bulletList:
            if item.judge():
                needDelItemList.append(item)
                pass
            pass
        for i in needDelItemList:
            needDelItemList.remove(i)
            pass
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()
            pass
        pass
    def shootBullet(self):
        '''
        发射子弹
        :return:
        '''
        newBullet=bullet(self.screen,self.x,self.y)
        self.bulletList.append(newBullet)
        pass
    pass
