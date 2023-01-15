from pygame import *

window = display.set_mode((1000,800))
display.set_caption('PingPong')
background = transform.scale(image.load('background.png'),(1000,800))
window.blit(background,(0,0))

clock = time.Clock()
FPS = 80


class Game_sprite(sprite.Sprite):
    def __init__(self, p_image, player_speed, player_x, player_y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    

class Player(Game_sprite):
    def __init__(self, p_image, player_speed, player_x, player_y, size_x, size_y):
        super().__init__(p_image, player_speed, player_x, player_y, size_x, size_y)
    def update_(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 700:
            self.rect.y += self.speed
    def update_second(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 700:
            self.rect.y += self.speed

racket_first_player = Player('racket.png', 5, 10,400, 60,150)
racket_second_player = Player('racket.png', 5, 930,400, 60,150)
ball = Game_sprite('tenis_ball.png', 5, 500,400, 65,65)

speed_x = 8
speed_y = 8

finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish == False:
        window.blit(background,(0,0))
        racket_first_player.update_()
        racket_second_player.update_second()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        if sprite.collide_rect(racket_first_player, ball) or sprite.collide_rect(racket_second_player, ball):
            speed_x *= -1
        if ball.rect.y  < 0 or ball.rect.y > 700:
            speed_y *= -1

        racket_first_player.reset()
        racket_second_player.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
