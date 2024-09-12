# demo for 7-segment simulation
# using the class 'Seven_seg' in seven_seg_pg.py

import pygame
import datetime
from seven_seg_pg import Seven_seg
from lcd_font_pg import LCD_font
from mcje.minecraft import Minecraft
import param_MCJE as param

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
