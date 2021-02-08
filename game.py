import pygame
from player import Player
from monster import Monster,Warrior,Knight
from arrow_event import ArrowEvent
from sound import SoundManager

#creer une classe qui represente le jeu
class Game:
    def __init__(self):
        #definir si jeu a commencé
        self.is_playing = False
        #generer joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        #créer le score
        self.font = pygame.font.Font("assets/BlackOpsOne-Regular.ttf",25)
        self.score = 0
        self.pressed = {}
        
        #groupe de monstre
        self.all_monsters = pygame.sprite.Group()

        #gerer le son
        self.sound_manager = SoundManager()

        #generer l'event
        self.arrow_event = ArrowEvent(self)

    def start(self):
        self.is_playing = True
        for i in range(1,4):
            self.spawn_monster(Warrior)
        self.spawn_monster(Knight)

    def add_score(self,points=10):
        self.score+= points

    def game_over(self):
        #remettre le jeux au debut (retirer les monstres, remetre les pv à 100, et ecran d'acceuil)
        self.all_monsters = pygame.sprite.Group()
        self.arrow_event.all_arrows=pygame.sprite.Group()
        self.player.pv = self.player.max_pv
        self.arrow_event.reset()
        self.is_playing = False
        self.score = 0
        self.sound_manager.play('game_over')
    
    def update(self,screen):
        #afficher le score sur l'ecran
        score_text = self.font.render(f"Score : {self.score}",1,(0,0,0))
        screen.blit(score_text, (20,20))

        #appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        #actualiser jauge pv joueur
        self.player.update_pv_bar(screen)

        #actualiser la barre d'event du jeu
        self.arrow_event.update_bar(screen)

        #appliquer l'image des projectiles
        self.player.all_projectiles.draw(screen)
        
        #appliquer les images de monstres
        self.all_monsters.draw(screen)

        #appliquer les images de fleches
        self.arrow_event.all_arrows.draw(screen)

        #recupperer les projectile du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        #recupperer les monstre du jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_pv_bar(screen)

        #recupperer les fleches du jeu
        for arrow in self.arrow_event.all_arrows:
            arrow.fall()

        #Deplacement gauche droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width< screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x>0:
            self.player.move_left()
        #deplacement haut bas
        # elif self.pressed.get(pygame.K_UP) and self.player.rect.y>0:
        #     self.player.move_up()
        # elif self.pressed.get(pygame.K_DOWN)and self.player.rect.y + self.player.rect.height< screen.get_height():
        #     self.player.move_down()


    def spawn_monster(self,monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))

    def check_collision(self, sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False, pygame.sprite.collide_mask)