import pygame
import random

# 全局定义
SCREEN_X = 600                 #全局定义屏幕的宽
SCREEN_Y = 600                 #全局定义屏幕的长

    
# 蛇类
# 点以25为单位
class Snake:
    # 初始化各种需要的属性 [开始时默认向右/身体块x5]
    def __init__(self):
        self.dirction = pygame.K_RIGHT
        self.body = []
        for x in range(5):
            self.addnode()
        
    # 无论何时 都在前端增加蛇块
    def addnode(self):
        left,top = (0,0)                     # 设定贪吃蛇从屏幕的右上角开始出现
        if self.body:
            left,top = (self.body[0].left,self.body[0].top)
        node = pygame.Rect(left, top, 25, 25)                    # 定义蛇在游戏开始时出现的位置，以及蛇的每一节身体的长宽 pygame.Rect(left, top, width, height)
        if self.dirction == pygame.K_LEFT:                       # 如果贪吃蛇朝左移动，则就在左边增加一个蛇块
            node.left -= 25
        elif self.dirction == pygame.K_RIGHT:
            node.left += 25
        elif self.dirction == pygame.K_UP:
            node.top -= 25
        elif self.dirction == pygame.K_DOWN:
            node.top += 25
        self.body.insert(0,node)
        
    # 删除最后一个块
    def delnode(self):
        self.body.pop()                         # 在前进过程中删除最后一个蛇块
        
    # 死亡判断
    def isdead(self):
        # 撞墙
        if self.body[0].x  not in range(SCREEN_X):          # 若蛇块不在屏幕范围内，判定死亡为真
            return True
        if self.body[0].y  not in range(SCREEN_Y):
            return True
        # 撞自己
        if self.body[0] in self.body[1:]:                   # 如果撞到自己，判定为死亡
            return True
        return False
        
    # 移动！
    def move(self):
        self.addnode()                                      # 往运动方向增加一个蛇块
        self.delnode()                                      # 在前进过程中删除最后一个蛇块
        
    # 改变方向 但是左右、上下不能被逆向改变
    def changedirection(self, curkey):
        LR = [pygame.K_LEFT, pygame.K_RIGHT]
        UD = [pygame.K_UP, pygame.K_DOWN]
        if curkey in LR+UD:                                  # 如果按键在四个方向键之内
            if (curkey in LR) and (self.dirction in LR):
                return                                       # 
            if (curkey in UD) and (self.dirction in UD):
                return
            self.dirction = curkey                           # 返回当前的运动方向
       
       
# 食物类
# 方法： 放置/移除
# 点以25为单位
class Food:
    def __init__(self):                                       
        self.rect = pygame.Rect(0,0,25,25)                    # rect对象是用来存储矩形对象的
        
    def remove(self):
        self.rect.left = 0
    
    def set(self):
        if self.rect.left == 0:
            allpos = []
            # 不靠墙太近 25 ~ SCREEN_X-25 之间
            for pos in range(25,SCREEN_X-25,25):                # 将屏幕减小外围25分辨率后的所有位置（以25*25像素块为单位）都添加到allpos列表中
                allpos.append(pos)
            self.rect.left = random.choice(allpos)
            self.rect.top  = random.choice(allpos)
            print(self.rect)
            

def show_text(screen, pos, text, color, font_bold = False, font_size = 60, font_italic = False):   
    #获取系统字体，并设置文字大小                                             # pygame.font.SysFont() 从系统字体库创建一个 Font 对象。SysFont(name, size, bold=False, italic=False) -> Font
    cur_font = pygame.font.SysFont("宋体", font_size)  
    #设置是否加粗属性  
    cur_font.set_bold(font_bold)                                            # pygame.font.Font.set_bold()  ——  启动粗体字渲染
    #设置是否斜体属性                                                        # pygame.font.Font.set_italic()  ——  启动斜体字渲染
    cur_font.set_italic(font_italic)  
    #设置文字内容  
    text_fmt = cur_font.render(text, 1, color)                              # pygame.font.Font.render()  ——  在一个新 Surface 对象上绘制文本
    #绘制文字  
    screen.blit(text_fmt, pos)                                              # surface.blit(image, position) 
     
def main():
    pygame.init()                                    #初始化pygame模块，确保pygame模块完整可用
    screen_size = (SCREEN_X,SCREEN_Y)
    screen = pygame.display.set_mode(screen_size)    #设定游戏窗口的大小（分辨率吧）
    pygame.display.set_caption('Snake')              #设定游戏窗口的标题
    clock = pygame.time.Clock()                      #创建一个名字为clock的对象来记录时间
    scores = 0                                       #初始化分数为0
    isdead = False                                   #创建死亡判定参数isdead,初始为False
    
    # 蛇/食物
    snake = Snake()                                  #创建一个Snake类的实例，名字为snack
    food = Food()                                    #创建一个Food类的实例，名字为food
    
    while True:
        for event in pygame.event.get():             # 设定游戏开始
            if event.type == pygame.QUIT:            # 判定玩家是否退出（点击窗口的X关闭游戏）
                pygame.quit()
            if event.type == pygame.KEYDOWN:         # 检查玩家是否按下关键键位，未真则执行if后语句
                snake.changedirection(event.key)     # 玩家按下方向键以后执行改变方向
                # 死后按space重新开始
                if event.key == pygame.K_SPACE and isdead:  # 如果贪吃蛇死亡判定为真，且玩家按了space键则重新开始游戏
                    return main()
                
            
        screen.fill((25,25,25))                      # 定义屏幕颜色（RGB颜色）
        

        # 画蛇身 / 每一步+1分
        if not isdead:                               # 如果蛇没有死，那么每走一步加一分
            scores+=1
            snake.move()
        for rect in snake.body:
            pygame.draw.rect(screen,(20,220,39), rect)  # 设置贪吃蛇的颜色（RGB颜色）

        # 显示死亡文字
        isdead = snake.isdead()
        if isdead:                                    # 判断贪吃蛇是否死亡
            show_text(screen,(100,200),'YOU DEAD!',(227,29,18),False,100)
            show_text(screen,(150,260),'press space to try again...',(0,0,22),False,30)

        # 食物处理 / 吃到+50分
        # 当食物rect与蛇头重合,吃掉 -> Snake增加一个Node
        if food.rect == snake.body[0]:
            scores+=50
            food.remove()
            snake.addnode()
        
        # 食物投递
        food.set()
        pygame.draw.rect(screen,(136,0,21),food.rect)            # 绘制矩形对象 pygame.draw.rect(surface, self.innerColor， self.rect)
        
        # 显示分数文字
        show_text(screen,(50,500),'Scores: '+str(scores),(223,223,223))
        
        pygame.display.update()                              # The Pygame.display.update() method redraws the screen.
        clock.tick(10)                                        # The clock.tick() method 一秒内刷新的次数
    
    
if __name__ == '__main__':
    main() 
  
