import pygame
import random

#créer la class monster
class Monster(pygame.sprite.Sprite):
    def __init__(self,game,name,size = (200,200),offset = 0):
        super().__init__()
        self.game=game
        self.pv = 100
        self.max_pv= 100
        self.attack = 0.5
        self.size = size
        self.image = pygame.image.load(f'assets/{name}.png')
        self.image = pygame.transform.scale(self.image,size)
        self.rect= self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,600)
        self.rect.y = 560 - offset

        self.points = 15

    def set_peed(self,speed):
        self.default_speed = speed
        self.vitesse = random.randint(1,3)

    def damage(self,amount):
        #Infliger degats
        self.pv -= amount

        #verifier si ses pv <= 0 
        if  self.pv <= 0:
            #le faire reaparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0,600)
            self.pv = self.max_pv
            self.vitesse = random.randint(1,self.default_speed)

            self.game.add_score(self.points)

            #verifier si la barre d'event est a 100%
            if self.game.arrow_event.is_full_loaded():
                #le retirer du jeu
                self.game.all_monsters.remove(self)
                self.game.arrow_event.arrow_fall_loaded()


    def update_pv_bar(self,surface):
        #definir couleur jauge pv
        bar_color = (231,6,6)

        #definir la position de notre jauge pv
        bar_position = [self.rect.x+10,self.rect.y-10,self.pv,3]

        #definir couleur bg jauge pv
        bg_bar_color = (60,63,60)

        #definir position bg jauge pv
        bg_bar_position = [self.rect.x+10,self.rect.y-10,self.max_pv,3]

        #dessiner jauge pv
        pygame.draw.rect(surface,bg_bar_color,bg_bar_position)
        pygame.draw.rect(surface,bar_color,bar_position)

    def forward(self):
        #se deplace que s'il n'entre pas en colision
        if not self.game.check_collision(self,self.game.all_players):
            self.rect.x -= self.vitesse
        else:
            #Infliger degats
            self.game.player.damage(self.attack)
            #verifier s'il sort de l'ecran
            # if self.rect.x <= 0 :
                #le faire reaparaitre comme un nouveau monstre
                # self.rect.x = 1000 + random.randint(0,600)
                # self.pv = self.max_pv
                # self.vitesse = random.randint(1,2)

class Knight(Monster):
    def __init__(self,game):
        super().__init__(game,"knight",(160,160),30)
        self.pv = 150
        self.max_pv = 150
        self.attack = 0.8
        self.set_peed(3)

        self.points = 25


class Warrior(Monster):
    def __init__(self,game):
        super().__init__(game,"warrior",(130,130))
        self.set_peed(2)

