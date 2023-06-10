from pygame import *
back=(255,200,100)
width=700
height=500
class GameSprite(sprite.Sprite):
    #конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #разом 55,55 - параметри
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height - 80:
            self.rect.y += self.speed
window=display.set_mode((width,height))
window.fill(back)


clock=time.Clock()
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

game_over=False

speed_x=3
speed_y=3

while not game_over:
    for e in event.get():
        if e.type==QUIT:
            game_over=True
            
    if game_over!=True:
        ball.rect.x+=speed_x
        ball.rect.y+=speed_y
    
    if ball.rect.y>width-50 or ball.rect.y<0:
        speed_y*-=1
    
    

    ball.reset()
    display.update()
    clock.tick(40)
