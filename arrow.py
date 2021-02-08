import pygame
import random
from monster import Monster,Warrior,Knight


#creer une classe pour generer des fleche
class Arrow(pygame.sprite.Sprite):
    def __init__(self,arrow_event):
        super().__init__()
        #definir l'image arrow
        self.image = pygame.image.load('assets/arrow.png')
        self.rect = self.image.get_rect()
        self.vitesse = random.randint(2,6)
        self.rect.x=random.randint(20,1030)
        self.rect.y= - random.randint(0,800)
        self.arrow_event = arrow_event

    def remove(self):
        self.arrow_event.all_arrows.remove(self)

        #verifier si le nombre de fleche est 0
        if len(self.arrow_event.all_arrows) == 0:
            self.arrow_event.reset()
            #apparaitre les monstre
            self.arrow_event.game.start()

            # for i in range(1,4):
            #     self.arrow_event.game.spawn_monster(Warrior)
            # self.arrow_event.game.spawn_monster(Knight)

    def fall(self):
        self.rect.y += self.vitesse

        if self.rect.y >= 565:
            # retirer la fleche quand elle touche le sole
            self.remove()
            self.arrow_event.game.sound_manager.play('arrow')
            #s'il n'y a plus de fleches => (deja fait ligne 21 à 25)
            # if len(self.arrow_event.all_arrows) == 0 :
                #remettre la jauge au depart
                # self.arrow_event.reset()
                # self.arrow_event.fall_mode = False
            
        #verifier si la fleche touche le dragon
        if self.arrow_event.game.check_collision(self,self.arrow_event.game.all_players):
            self.arrow_event.game.player.damage(10)
            self.remove()





#fall_mode sert a rien ...