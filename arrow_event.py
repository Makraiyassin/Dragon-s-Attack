import pygame
from arrow import Arrow

#classe pour les fleche
class ArrowEvent:
    #lors du chargement, creer un compteur
    def __init__(self,game):
        self.percent = 0
        self.percent_speed = 10/100
        self.game = game

        # self.fall_mode = False

        #definir un groupe pour les fleches
        self.all_arrows = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed
    
    def is_full_loaded(self):
        return self.percent >= 100

    def reset(self):
        self.percent = 0

    def arrow_fall(self):
        #boucle pour plusier fleche
        for i in range (1,30):
            #apparaitre une premiere fleche
            self.all_arrows.add(Arrow(self))

    def arrow_fall_loaded (self):
        #quand la barre d'event est charger
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.arrow_fall()
            # self.fall_mode = True #activer l'event

    def update_bar(self,surface):
        pygame.draw.rect(surface,(60,63,60),[0,surface.get_height()-15,surface.get_width(),10])
        pygame.draw.rect(surface,(66,100,10),[0,surface.get_height()-15,(surface.get_width()/100)*self.percent,10])
        self.add_percent()



#fall_mode sert a rien ...