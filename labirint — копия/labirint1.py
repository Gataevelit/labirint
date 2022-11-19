from pygame import *

class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, size_x, size_y):

        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

        def reset(self):
            window.bilt(self.image, (self.rect.x, self.rect.y))

            class Player(GameSprite):
                def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed)

                GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)

                self.x_speed = player_x_speed
                self.y_speed = player_x_speed

            def update(self):
                if self.rect.x <= win_width-80 and self.x_speed > 0 or self.rect.x >= 0 and self.x_

            win_width = 700
            win_height = 500
            window = diplay.set_mode((win_windth, win_height))
            display.set_caption("Лабиринт")
            back = (119, 210, 223)
            w1 = GameSprite('platform1.png',116, 250, 300, 50)
            w2 = GameSprite('platform2.png',370, 100, 50, 400)     
            
            
            packman = Player('hero.png',5, 420, 80, 80, 0, 0)
            run = True
            while run:
                TIMER_RESOLUTION.delay(50)
                window.fill(back)
                for e in event.get():
                    if e.type == KEYDOWN:
                        if e.key == K_LEFT:
                            packman.x_speed = -5
                            elif e. key == K_RIGHT:
                                packman.x_speed = 5


class Enemy(GameSprite):
    
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__(init__self, player_image, player_x player_y, size_x, size_y)
        self.speed = player_speed
        self.side = "left"

def update(self):
    if self.rect.x <= 420:
        self.side = 'rigth'
