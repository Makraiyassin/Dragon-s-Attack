import pygame
import math
from game import Game

pygame.init()
#definir une clock
clock = pygame.time.Clock()
FPS = 60

#generer la fenetre du jeu
pygame.display.set_caption("comet fall Game")
screen = pygame.display.set_mode((1080,720))

#importer bg du jeux
background = pygame.image.load('assets/castle.png')

#importer banniere
banner = pygame.image.load('assets/banner4.png')
# banner = pygame.transform.scale(banner,(500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/3.3) 
banner_rect.y = math.ceil(screen.get_height()/23) 

#bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button,(350,100))
play_button_rect = banner.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/2.4) 
play_button_rect.y = math.ceil(screen.get_height()/1.95) 

#charger jeu
game = Game()

running = True

#boucle du jeu (tant que runnig == true)

while running:

    #appliquer bg du jeu
    screen.blit(background,(0,-200))

    #verifier si jeux a commencé
    if game.is_playing :
        #declancher les instructions de la partie 
        game.update(screen)
    #verifier si le jeu n'a pas commencé
    else:
        #ajouté l'ecran de bienvenu
        screen.blit(play_button,play_button_rect)
        screen.blit(banner,banner_rect)

    #mettre à jour l'ecran
    pygame.display.flip()
    
    #si le joueur ferme la fenetre
    for event in pygame.event.get():

        #verifier que l'event est "fermer fenetre"
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")

        #detecter si un joueur appuie sur une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key]=True
            #detecter si le joueur appuie sur espace
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    game.start()


        #detecter si un joueur appuie sur une touche du clavier
        elif event.type == pygame.KEYUP:
            game.pressed[event.key]=False

        #detecter si un joueur appuie sur la souris
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verification pour savoir si la souris est en collision avec les boutton
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode "lancé"
                game.start()
                
                # jouer le son
                game.sound_manager.play("click")

    #fixer le nombre de FPS
    clock.tick(FPS)

