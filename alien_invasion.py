import sys
import pygame
from setting import Setting
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from button import Button
from alien import Alien


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建一个用于储存游戏统计信息的实例
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于储存子弹的编组
    bullets = Group()
    # 创建一个外星人
    # alien = Alien(ai_settings, screen)
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        '''# 监视键盘和鼠标 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()'''
        if stats.game_active:
            ship.update()

            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            '''bullets.update()
            # 删除已消失的子弹
            for bullet in bullets.copy():
                if bullet.rect.bottom<=0:
                    bullets.remove(bullet)
            # print(len(bullets))'''
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        '''# 每次循环时重新绘制屏幕
        screen.fill(ai_setting.bg_color)
        ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()'''


run_game()
