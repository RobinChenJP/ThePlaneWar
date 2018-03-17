import pygame
import random

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SECOND = 60


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, img_path, speed=1):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.speed = speed


class PlaneSprite(GameSprite):
    def __init__(self, img_path, speed=1):
        super().__init__(img_path, speed)
        self.rect.x = (SCREEN_RECT.width - self.rect.width) / 2
        self.rect.y = SCREEN_RECT.height - self.rect.height

    def update(self, *args):
        self.rect.y -= self.speed
        if self.rect.y < -self.rect.height:
            self.rect.y = SCREEN_RECT.height


class EnemySprite(GameSprite):
    def __init__(self, img_path, speed=1):
        super().__init__(img_path, speed)
        self.max_x = SCREEN_RECT.width - self.rect.width
        self.random_show()

    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_RECT.height:
            self.rect.y = -self.rect.height
            self.random_show()

    def random_show(self):
        self.rect.x = random.randint(0, self.max_x)
        self.speed = random.randint(1, 3)


class BulletSprite(GameSprite):
    def __init__(self, img_path, speed=1):
        super().__init__(img_path, speed)

    def update(self, *args):
        super().update()
        self.rect.y -= self.speed


class BackgroundSprite(GameSprite):
    def __init__(self, img_path, speed=1, is_alt=False):
        super().__init__(img_path, speed)
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.y > self.rect.height:
            self.rect.y = -self.rect.height
