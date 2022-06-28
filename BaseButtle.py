import pygame.image


class BaseButtle:
    def __init__(self,screen,imagePath):
        '''
        :param screen: 窗口对象
        :param imagePath: 子弹图片路径
        '''
        self.screen=screen
        self.image=pygame.image.load(imagePath)
        self.buttleList=[]
        pass
    def display(self):
        '''
        子弹显示窗口位置
        :return:
        '''
        self.screen.blit(self.image,(self.x,self.y))
        pass
    def judge(self):
        '''
        判断子弹是否越界
        :return:
        '''
        if self.y<0 or self.y>=500-39:
            return True
        else:
            return False
    pass
