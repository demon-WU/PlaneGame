class BasePlane:
    def __init__(self,screen,imagePath,x,y):
        '''
        构造父类函数
        :param screen:主窗口对象
        :param imagePath: 图片路径
        :param x:初始横坐标位置
        :param y:初始纵坐标位置
        '''
        self.screen=screen
        self.imagePath=imagePath
        self.x=x
        self.y=y
        pass