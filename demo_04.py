# demo for 7-segment simulation
# using the class 'Seven_seg' in seven_seg_pg.py

import pygame
import datetime
from seven_seg_pg import Seven_seg
from lcd_font_pg import LCD_font
from mcje.minecraft import Minecraft
import param_MCJE as param

LCD_0 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 1, 1,
         1, 0, 1, 0, 1,
         1, 1, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0)

LCD_1 = (0, 0, 1, 0, 0,
         0, 1, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 1, 1, 1, 0)

LCD_2 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         0, 0, 0, 0, 1,
         0, 0, 0, 1, 0,
         0, 0, 1, 0, 0,
         0, 1, 0, 0, 0,
         1, 1, 1, 1, 1)

LCD_3 = (1, 1, 1, 1, 1,
         0, 0, 0, 1, 0,
         0, 0, 1, 0, 0,
         0, 0, 0, 1, 0,
         0, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0)

LCD_4 = (0, 0, 0, 1, 0,
         0, 0, 1, 1, 0,
         0, 1, 0, 1, 0,
         1, 0, 0, 1, 0,
         1, 1, 1, 1, 1,
         0, 0, 0, 1, 0,
         0, 0, 0, 1, 0)

LCD_5 = (1, 1, 1, 1, 1,
         1, 0, 0, 0, 0,
         1, 1, 1, 1, 0,
         0, 0, 0, 0, 1,
         0, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0)

LCD_6 = (0, 0, 1, 1, 0,
         0, 1, 0, 0, 0,
         1, 0, 0, 0, 0,
         1, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0)

LCD_7 = (1, 1, 1, 1, 1,
         0, 0, 0, 0, 1,
         0, 0, 0, 1, 0,
         0, 0, 1, 0, 0,
         0, 1, 0, 0, 0,
         0, 1, 0, 0, 0,
         0, 1, 0, 0, 0)

LCD_8 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0)

LCD_9 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 1,
         0, 0, 0, 0, 1,
         0, 0, 0, 1, 0,
         0, 1, 1, 0, 0)

LCD_A = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         1, 1, 1, 1, 1,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1)

LCD_B = (1, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         1, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         1, 1, 1, 1, 0)

LCD_C = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 0,
         1, 0, 0, 0, 0,
         1, 0, 0, 0, 0,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0)

LCD_D = (1, 1, 1, 0, 0,
         1, 0, 0, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         1, 0, 0, 1, 0,
         1, 1, 1, 0, 0)

LCD_E = (1, 1, 1, 1, 1,
         1, 0, 0, 0, 0,
         1, 0, 0, 0, 0,
         1, 1, 1, 1, 1,
         1, 0, 0, 0, 0,
         1, 0, 0, 0, 0,
         1, 1, 1, 1, 1)

LCD_F = (1, 1, 1, 1, 1,
         1, 0, 0, 0, 0,
         1, 0, 0, 0, 0,
         1, 1, 1, 1, 1,
         1, 0, 0, 0, 0,
         1, 0, 0, 0, 0,
         1, 0, 0, 0, 0)

LCD_COL = (0, 0, 0, 0, 0,
           0, 1, 1, 0, 0,
           0, 1, 1, 0, 0,
           0, 0, 0, 0, 0,
           0, 1, 1, 0, 0,
           0, 1, 1, 0, 0,
           0, 0, 0, 0, 0,)

LCD_HYF = (0, 0, 0, 0, 0,
           0, 0, 0, 0, 0,
           0, 0, 0, 0, 0,
           0, 1, 1, 1, 0,
           0, 0, 0, 0, 0,
           0, 0, 0, 0, 0,
           0, 0, 0, 0, 0,)

# LCD_font_styles = (LCD_0, LCD_1, LCD_2, LCD_3, LCD_4, LCD_5, LCD_6, LCD_7, LCD_8, LCD_9, LCD_A, LCD_B, LCD_C, LCD_D, LCD_E, LCD_F)

LCD_font_styles = {0x30: LCD_0, 0x31: LCD_1, 0x32: LCD_2, 0x33: LCD_3,
                   0x34: LCD_4, 0x35: LCD_5, 0x36: LCD_6, 0x37: LCD_7,
                   0x38: LCD_8, 0x39: LCD_9, 0x41: LCD_A, 0x42: LCD_B,
                   0x43: LCD_C, 0x44: LCD_D, 0x45: LCD_E, 0x46: LCD_F,
                   0x47: LCD_COL, 0x48: LCD_HYF}

mc = Minecraft.create(port=param.PORT_MC)

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([600, 320])
pygame.display.set_caption("pygame 7-segment display simulation")
screen.fill(DARK_GRAY)

display1 = Seven_seg(screen)
display1.init_col(BLOCK_SIZE=6, BLOCK_INTV=8, COLOR_ON=GREEN, COLOR_OFF=GRAY)
display1.init_row(X_ORG=8, Y_ORG=8, COL_INTV=6)

lcd1 = LCD_font(screen)
lcd1.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=CYAN, COLOR_OFF=GRAY)
lcd1.init_row(X_ORG=8, Y_ORG=10, COL_INTV=6)

lcd2 = LCD_font(screen)
lcd2.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=RED, COLOR_OFF=GRAY)
lcd2.init_row(X_ORG=8, Y_ORG=18, COL_INTV=6)

running = True
# infinite loop top ----
while running:
    for count in range(16 ** 4):  # 0から65535まで
        # press ctrl-c or close the window to stop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not running:
            break
        # 「for count」のループから抜ける。whileループも抜ける。

        display1.update_col(col=0, num=count // (16 ** 3))  # 4096の位
        display1.update_col(col=1, num=count // (16 ** 2))  # 256の位
        display1.update_col(col=2, num=count // 16)  # 16の位
        display1.update_col(col=3, num=count)   # 1の位

        dt_now = datetime.datetime.now()
        
        #mc.setBlock(5, 70, 5,  param.GOLD_BLOCK)
        for i in range (7):
            for j in range (5):                #if :
                if LCD_0 == 1 :
                    mc.setBlock(5+j,71+i,5, param.GOLD_BLOCK)

        
        lcd1.update_col(col=0, code=ord('0')+dt_now.year//1000)
        lcd1.update_col(col=1, code=ord('0')+((dt_now.year//100)%10))
        lcd1.update_col(col=2, code=ord('0')+((dt_now.year//10)%10))
        lcd1.update_col(col=3, code=ord('0')+dt_now.year%10)
        lcd1.update_col(col=4, code=0x48)
        lcd1.update_col(col=5, code=ord('0')+dt_now.month//10)
        lcd1.update_col(col=6, code=ord('0')+dt_now.month%10)
        lcd1.update_col(col=7, code=0x48)
        lcd1.update_col(col=8, code=ord('0')+dt_now.day//10)
        lcd1.update_col(col=9, code=ord('0')+dt_now.day%10)


        lcd2.update_col(col=0, code=ord('0')+dt_now.hour//10)
        lcd2.update_col(col=1, code=ord('0')+dt_now.hour%10)
        lcd2.update_col(col=2, code=0x47)
        lcd2.update_col(col=3, code=ord('0')+dt_now.minute//10)
        lcd2.update_col(col=4, code=ord('0')+dt_now.minute%10)
        lcd2.update_col(col=5, code=0x47)
        lcd2.update_col(col=6, code=ord('0')+dt_now.second//10)
        lcd2.update_col(col=7, code=ord('0')+dt_now.second%10)

        pygame.display.flip()  # update_col
        clock.tick(20)  # FPS, Frame Per Second
    screen.fill(DARK_GRAY)
# infinit loop bottom ----

pygame.quit()
