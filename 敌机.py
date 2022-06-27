import pygame


class EnemyPlane:
    def __init__(self,screen):
        '''
        敌机构造函数
        :param screen: 传主窗口对象进来
        '''
        self.x=0
        self.y=0
        self.screen = screen
        self.image = pygame.image.load('./feiji/敌机.jpg')
        pass
    def display(self):
        '''
        敌机显示函数
        :return:
        '''
        self.screen.blit(self.image,(self.x,self.y))
    def shootEnemyBullet(self):
