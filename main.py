import pygame
import core
import random

tete= []
corps= []
pomme = []
score = []

vitesse = 5

def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [750, 750]

    global tete,corps,pomme
    tete= [375, 375, 20, 20, 58, 137, 35 ]
    corps= [377, 393, 20, 20, 75, 242, 75 ]

    x = random.randint(0,742)
    y = random.randint(0,742)

    pomme = pomme + [ x ,y ]




    print("Setup END-----------")


def longueur():
    if (pomme[1] - tete[1]) < 9 + 20 and (pomme[0] - tete[0]) < 9 + 20:
        pygame.draw.rect(core.screen, (corps[4], corps[5], corps[6]), (corps[0], corps[1], corps[2], corps[4]))




def run():
    print("running")
    pygame.draw.rect(core.screen, (tete[4], tete[5], tete[6]), (tete[0], tete[1], tete[2], tete[3]))
    pygame.draw.rect(core.screen, (corps[4], corps[5], corps[6]), (corps[0], corps[1], corps[2], corps[3]))
    score = []
    pygame.event.pump()
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_DOWN]):
        tete[1] = tete[1] + vitesse
        corps[0] = tete[0]
        corps[1] = tete[1] - 20

    if (keys[pygame.K_UP]):
        tete[1] = tete[1] - vitesse
        corps[0] = tete[0]
        corps[1] = tete[1] + 20

    if (keys[pygame.K_RIGHT]):
        tete[0] = tete[0] + vitesse
        corps[1] = tete[1]
        corps[0] = tete[0] - 20

    if (keys[pygame.K_LEFT]):
        tete[0] = tete[0] - vitesse
        corps[1] = tete[1]
        corps[0] = tete[0] + 20


    pygame.draw.circle(core.screen, (255, 0, 0), (pomme[0], pomme[1]), 9)

    if (pomme[1]-tete[1]) < 9 + 20 and (pomme[0]-tete[0]) < 9 + 20:
        pomme[1] = random.randint (0,742)
        pomme[0]= random.randint (0,742)
        score = score + [1]

    if (tete[1]==0 or tete[1]==750 or tete[0]==0  or tete[0]==750):
        print(score)
        print("GAMEOVER")


core.main(setup, run)