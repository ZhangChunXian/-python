import pygame
import random

# 全局定义游戏界面的长和宽（单位为分辨率）
SCREEN_X = 600                                     # 全局定义游戏界面的长
SCREEN_Y = 600                                     # 全局定义游戏界面的宽

# 蛇类
# 点以25为单位
class Snake:
    # 初始化各种需要的属性 [开始时默认向右/身体块x5]
    def __init__(self):
        self.dirction = pygame.K_RIGHT
        self.body = []
        for x in range(10):
            self.addnode()

# 无论何时 都在前端增加蛇块
    def addnode(self):
        left,top = (0,0)                                         # 设定贪吃蛇从屏幕的右上角开始出现
        if self.body:
            left,top = (self.body[0].left,self.body[0].top)
        node = pygame.Rect(left, top, 25, 25)                    # 定义蛇在游戏开始时出现的位置，以及蛇的每一节身体的长宽 pygame.Rect(left, top, width, height)
        if self.dirction == pygame.K_LEFT:                       # 如果贪吃蛇朝左移动，
            node.left -= 25
        elif self.dirction == pygame.K_RIGHT:
            node.left += 25
        elif self.dirction == pygame.K_UP:
            node.top -= 25
        elif self.dirction == pygame.K_DOWN:
            node.top += 25
        self.body.insert(0,node)


# 创建一个函数main()作为主函数
def main():
    pygame.init()
    screen_size = (SCREEN_X,SCREEN_Y)
    screen = pygame.display.set_mode(screen_size)  #2 设定游戏窗口的大小（单位：分辨率）
    pygame.display.set_caption('Snake') 



main()