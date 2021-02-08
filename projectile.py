import pygame

#classe du projectile
class Projectile(pygame.sprite.Sprite):
    #definir constructeur de la classe
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.vitesse = 5
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 100
        self.rect.y = player.rect.y + 20
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        #tourner le projectile
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image,self.angle,1)
        self.rect = self.image.get_rect(center = self.rect.center)

    def remove(self):
                self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.vitesse
        self.rotate()

        #verifier si le projectile entre en collision avec un monster
        for monster in self.player.game.check_collision(self,self.player.game.all_monsters):
            #le suprimer
            self.remove()

            #infliger des degats
            monster.damage(self.player.attack)

        #verifier si le projectile n'est plus dans l'ecran
        if self.rect.x>1080:
            #le suprimer
            self.remove()
