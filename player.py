import pygame
from projectile import Projectile


#creer une classe qui represente le joueur
class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.pv = 100
        self.max_pv= 100
        self.attack= 15
        self.vitesse= 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/dragon.png')
        self.rect = self.image.get_rect()
        self.rect.x= 400
        self.rect.y= 550 

    def damage(self,amount):
        if self.pv - amount > amount:
            #Subir degats
            self.pv -= amount
        else:
            #si le joueur n'a plus de pv
            self.game.game_over()

        #verifier si ses pv <= 0 
        # if  self.pv <= 0:
            #Game over

    def launch_projectile(self):
        #creer instance de class projectile
        self.all_projectiles.add(Projectile(self))
        self.game.sound_manager.play('tir')

    def update_pv_bar(self,surface):
        #dessiner jauge pv
        pygame.draw.rect(surface,(60,63,60),[self.rect.x+30,self.rect.y-20,self.max_pv,3])
        pygame.draw.rect(surface,(231,6,6),[self.rect.x+30,self.rect.y-20,self.pv,3])

    def move_right(self):
        #se deplace que s'il n'entre pas en colision
        if not self.game.check_collision(self,self.game.all_monsters):
            self.rect.x += self.vitesse

    def move_left(self):
        self.rect.x -= self.vitesse

    def move_up(self):
        self.rect.y -= self.vitesse

    def move_down(self):
        self.rect.y += self.vitesse

