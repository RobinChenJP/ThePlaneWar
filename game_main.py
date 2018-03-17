import pygame
import game_sprite


class PlaneWar(object):

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(game_sprite.SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.background_sprite = game_sprite.BackgroundSprite("./images/background.png")
        self.background_sprite_alt = game_sprite.BackgroundSprite("./images/background.png", is_alt=True)
        self.enemy_sprite = game_sprite.EnemySprite("./images/enemy1.png")
        self.plane_sprite = game_sprite.PlaneSprite("./images/me1.png")
        self.group = pygame.sprite.Group()
        self.group.add(self.background_sprite, self.background_sprite_alt, self.plane_sprite, self.enemy_sprite)

    def start_game(self):
        print("开始游戏")
        while True:
            self.handle_key_event()
            self.update_screen()
            self.clock.tick(60)

    @staticmethod
    def end_game():
        pygame.quit()
        exit()

    def handle_key_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneWar.end_game()
            else:
                print("无效按键，KEY_TYPE：" + str(event.type))

    def update_screen(self):
        self.group.update()
        self.group.draw(self.screen)
        pygame.display.update()


if __name__ == "__main__":
    PlaneWar().start_game()
