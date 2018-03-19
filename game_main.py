import pygame
import game_sprite

ID_SHOW_ENEMY_SPRITE = pygame.USEREVENT
ID_SHOW_BULLET_SPRITE = pygame.USEREVENT + 1


class PlaneWar(object):

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(game_sprite.SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.background_sprite = game_sprite.BackgroundSprite("./images/background.png")
        self.background_sprite_alt = game_sprite.BackgroundSprite("./images/background.png", is_alt=True)
        self.plane_sprite = game_sprite.PlaneSprite("./images/me1.png")
        self.bg_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.bg_group.add(self.background_sprite, self.background_sprite_alt)
        self.player_group.add(self.plane_sprite)
        pygame.time.set_timer(ID_SHOW_ENEMY_SPRITE, 1000)
        pygame.time.set_timer(ID_SHOW_BULLET_SPRITE, 200)

    def start_game(self):
        print("开始游戏")
        while self.plane_sprite.is_survive:
            self.handle_key_event()
            self.check_collide()
            self.update_screen()
            self.clock.tick(60)
        print("游戏结束")
        PlaneWar.end_game()

    @staticmethod
    def end_game():
        pygame.quit()
        exit()

    def handle_key_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneWar.end_game()
            elif event.type == ID_SHOW_ENEMY_SPRITE:
                enemy_sprite = game_sprite.EnemySprite("./images/enemy1.png")
                self.enemy_group.add(enemy_sprite)
            elif event.type == ID_SHOW_BULLET_SPRITE:
                bullet_sprite = game_sprite.BulletSprite("./images/bullet1.png", self.plane_sprite)
                self.player_group.add(bullet_sprite)

        pressed_key = pygame.key.get_pressed()
        self.plane_sprite.control_direction(pressed_key)

    def update_screen(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.player_group.update()
        self.player_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        pygame.display.update()

    def check_collide(self):
        pygame.sprite.groupcollide(self.enemy_group, self.player_group, True, True)


if __name__ == "__main__":
    PlaneWar().start_game()
