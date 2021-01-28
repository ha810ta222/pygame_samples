# handmade LCD font for pygame
# 5x7ドットマトリクス


import pygame
from pygame.locals import Rect


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

# LCD_font_styles = (LCD_0, LCD_1, LCD_2, LCD_3, LCD_4, LCD_5, LCD_6, LCD_7, LCD_8, LCD_9, LCD_A, LCD_B, LCD_C, LCD_D, LCD_E, LCD_F)

LCD_font_styles = {0x30: LCD_0, 0x31: LCD_1, 0x32: LCD_2, 0x33: LCD_3,
                   0x34: LCD_4, 0x35: LCD_5, 0x36: LCD_6, 0x37: LCD_7,
                   0x38: LCD_8, 0x39: LCD_9, 0x41: LCD_A, 0x42: LCD_B,
                   0x43: LCD_C, 0x44: LCD_D, 0x45: LCD_E, 0x46: LCD_F}

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)


class LCD_font():

    def __init__(self, screen):
        self.screen = screen

    def init_col(self, BLOCK_SIZE=4, BLOCK_INTV=4, COLOR_ON=WHITE, COLOR_OFF=GRAY):
        # ひと桁、コラムの設定
        # ブロックのサイズと配置間隔をピクセル指定（インターバル）
        self.BLOCK_SIZE = BLOCK_SIZE
        self.BLOCK_INTV = BLOCK_INTV
        # on/offのカラー
        self.COLOR_ON = COLOR_ON
        self.COLOR_OFF = COLOR_OFF

    def init_row(self, X_ORG=2, Y_ORG=8, COL_INTV=6):  # 表示行の設定
        # xy空間での7セグ表示、最上位桁の左下座標をブロック数で指定
        self.X_ORG = X_ORG * self.BLOCK_INTV
        self.Y_ORG = Y_ORG * self.BLOCK_INTV
        # 各桁のブロック間隔をブロック数で指定（インターバル）
        self.COL_INTV = COL_INTV * self.BLOCK_INTV

    def update_col(self, col=0, code=2):  # ある桁にある文字を表示する関数
        # codeの文字をcol桁目に表示、桁は最上位桁の左から右へ進む。
        block_size = self.BLOCK_SIZE
        i = 0
        for y in range(7):
            for x in range(5):
                if LCD_font_styles[int(code)][i] == 1:
                    color = self.COLOR_ON
                else:
                    color = self.COLOR_OFF
                # 桁の原点
                x0 = self.X_ORG + self.COL_INTV * col
                y0 = self.Y_ORG
                # ドットの原点座標
                org1 = (x0 + x * self.BLOCK_INTV, y0 + y * self.BLOCK_INTV)
                # ドットを描く
                pygame.draw.rect(self.screen, color, Rect(org1[0], org1[1], block_size, block_size))
                i += 1

    def update_message(self, code=0x30):  # ある桁にある文字を表示する関数
        self.update_col(self, col=0, code=code)
