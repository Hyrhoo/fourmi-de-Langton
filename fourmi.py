from turtle import screensize
import pygame, sys
from random import randint
pygame.init()
reso = (1000,1000)
screen = pygame.display.set_mode(reso)
screen.fill("#C0C0C0")
clock = pygame.time.Clock()

class Fourmille:
    fourmilles = []

    def __init__(self, pos=[i//2 for i in reso], instruc=[1,-1], taille=1, colors = ["#000000", "#FFFFFF" ,"#FF0000", "#00FFFF", "#0000FF", "#0000A0", "#ADD8E6", "#800080", "#FFFF00", "#00FF00", "#FF00FF", "#808000", "#008000", "#800000", "#A52A2A", "#FFA500", "#C0C0C0"]) -> None:
        self.taille = taille
        self.pos = pos
        self.instruc = instruc
        self.color = [pygame.color.Color(i) for i in colors[:len(self.instruc)]]
        self.color.append(pygame.color.Color(colors[-1]))
        self.direction = 1
        Fourmille.fourmilles.append(self)

    def update(self):
        try:
            coul = screen.get_at(self.pos)
        except IndexError:
            coul = self.color[0]
        try:
            index = self.color.index(coul) + 1
        except ValueError:
            index = len(self.color)
        if index > len(self.instruc) - 1:
            index = 0
        rect = pygame.Rect(self.pos[0], self.pos[1], self.taille, self.taille)
        pygame.draw.rect(screen, self.color[index], rect)
        instru = self.instruc[index]
        self.deplacer(instru)

    def deplacer(self, instru):
        self.direction += instru
        if self.direction < 1:
            self.direction = 4
        elif self.direction > 4:
            self.direction = 1
        self.pos[0] += (((self.direction + 1) % 2) * (3 - self.direction)) * self.taille
        self.pos[1] += ((self.direction % 2) * (2 - self.direction)) * self.taille

def fourmi_random(nbr):
    for _ in range(nbr):
        Fourmille([randint(0, 1000), randint(0, 1000)], [1, -1], 1)

#Fourmille([i//2 for i in reso], instruc=[1,1,-1,-1,1,1,-1,-1], taille=5)
#Fourmille(instruc=[-1,1,-1,1,-1,1,-1,1,-1,1,-1,1], taille=5)
#fourmi_random(1)
Fourmille(taille=5)

while not False:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    
    for f in Fourmille.fourmilles:
        f.update()

    pygame.display.flip()
    clock.tick(60)
