import pygame

pygame.init()

WIDTH = 1280
HEIGHT = 720

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("woodrow's vamp")

running = True
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # self.image = pygame.image.load("images/player.png")
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center= (x, y)
        self.speed = 5
        self.direction = pygame.Vector2()

    def move(self, dx, dy):
        self.direction.x = dx
        self.direction.y = dy

        if self.direction.length() > 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed


player = Player(WIDTH / 2, HEIGHT / 2)


all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# 게임 루프
while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 이벤트리스너
    keys = pygame.key.get_pressed()
    dx = keys[pygame.K_d] - keys[pygame.K_a]
    dy = keys[pygame.K_s] - keys[pygame.K_w]
    # if keys[pygame.K_a]:
    #     print("a 냐")

    player.move(dx, dy)

    screen.fill(GREEN)
    all_sprites.draw(screen)



    pygame.display.flip()

pygame.quit()
