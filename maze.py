# создай игру "Лабиринт"!
import pygame 

pygame.init()
pygame.mixer.init()
pygame.font.init()

font = pygame.font.Font(None, 70)
win = font.render("YOU WIN!?", True, (0, 0, 0))
lose = font.render("YOU LOSE!!!", True, (0, 0, 0))

Width = 700
Height = 500
WIDTH = 70
HEIGHT = 50
FPS = 60

window = pygame.display.set_mode((Width, Height)) #установка размера окна, (WIDTH, HEIGHT) - тапл
clock = pygame.time.Clock() 
pygame.mixer.music.load('jungles.ogg')
pygame.mixer.music.play()
kick = pygame.mixer.Sound('kick.ogg')

treasure = pygame.transform.scale(pygame.image.load("treasure.png"), (WIDTH, HEIGHT))
background = pygame.transform.scale(pygame.image.load("background.jpg"), (Width, Height)) #!
sprite1 = pygame.transform.scale(pygame.image.load("hero.png"), (WIDTH, HEIGHT))
sprite2 = pygame.transform.scale(pygame.image.load("cyborg.png"), (WIDTH, HEIGHT))

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_X, player_Y, player_Speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (65, 65))
        self.speed = player_Speed
        self.rect = self.image.get_rect()
        self.rect.x = player_X
        self.rect.y = player_Y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x < Width - 80:
            self.rect.x += self.speed
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < Height - 80:
            self.rect.y += self.speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(GameSprite):
    def update(self):
        # print("pug")
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= Width - 85:
            self.direction = "left"
        # print("cat")
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Wall():
    def __init__(self,
        color: tuple[int, int, int],
        wall_x: int,
        wall_y: int,
        wall_width: int,
        wall_height: int,
        window: pygame.Surface,
        ):
        super().__init__()
        self.color = color
        self.width = wall_width
        self.height = wall_height
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        self.window = window
    def draw_wall(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))

player = Player("hero.png", 50, 50, 5)
enemy = Enemy("cyborg.png", 470, 300, 3)
treasure = Player("treasure.png", 570, 50, 0)

wall_ceiling = Wall((255, 0, 0), 0, 0, 700, 10, window)
wall_left = Wall((255, 0, 0), 0, 10, 10, 700, window)
wall_right = Wall((255, 0, 0), 690, 0, 700, 700, window)


wall_maze_1 = Wall((255, 0, 0), 150, 0, 10, 300, window)
wall_maze_2 = Wall((255, 0, 0), 250, 100, 10, 700, window)
wall_maze_3 = Wall((255, 0, 0), 450, 0, 10, 400, window)


# final = GameSprite("treasure.png", Width - 120, Height - 80, 0)

#задай фон сцены
loop = True
finish = False

kick.play()
while loop:
    clock.tick(FPS)
    window.blit(background, (0, 0))

    #работа с событиями
    for event in pygame.event.get():
        #проверить закрытие окна
        if event.type == pygame.QUIT:
            loop = False
    
    if (
        pygame.sprite.collide_rect(player, enemy)
        or pygame.sprite.collide_rect(player, wall_ceiling)
        or pygame.sprite.collide_rect(player, wall_left)
        or pygame.sprite.collide_rect(player, wall_right)
        or pygame.sprite.collide_rect(player, wall_maze_1)
        or pygame.sprite.collide_rect(player, wall_maze_2)
        or pygame.sprite.collide_rect(player, wall_maze_3)
    ):
        finish = True
        window.blit(lose, (200, 200))
        print("ХАХАХАХАХАХ")

    if (pygame.sprite.collide_rect(player, treasure)):

        finish = True
        window.blit(win, (200, 200))
        print("победа")
        
    if finish != True:

        player.update()
        enemy.update()


        player.reset()
        enemy.reset()
        treasure.reset()

        wall_ceiling.draw_wall()
        wall_left.draw_wall()
        wall_right.draw_wall()

        wall_maze_1.draw_wall()
        wall_maze_2.draw_wall()
        wall_maze_3.draw_wall()

    pygame.display.update()
































# 1
# def c_to_f(temp):
#     G = temp * 9/5 + 32
#     return G
# print(c_to_f(100))

# 2
# def even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# print(even(4))

# 4
# def multiplication_table(numm):
#     G = 0
#     while G <= 10:
#         print(G * numm)
#         G += 1
# print(multiplication_table(5))

# 3
# l_int = [10, 5, 3, 2, 1]
# def my_max(l_int):
#     G = l_int[0]
#     for i in l_int:
#         if G < i:
#             G = i
#     return G
# print(my_max(l_int))

# 5
# def sum_integers(n):
#     samm = 0
#     J = 0
#     G = []
#     while n:
#         samm += 1
#         G.append(samm)
#     for i in len(G):
#         J += i
#         print(G)
# print(sum_integers(3))



