import random
import pygame
from tank import Character
from enemyTank import opponetTank
from pygame import mixer
import math
pygame.init()

# Window information
WIDTH = 799
HEIGHT = 533
FPS = 60
icon = pygame.image.load('world-peace.png')
pygame.display.set_caption("FOR PEACE")
pygame.display.set_icon(icon)
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
mixer.music.load('bensound-epic.mp3')
mixer.music.play(-1)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
# Background image
background = pygame.transform.scale(pygame.image.load('photo_2022-02-17_20-17-00.jpg'),(WIDTH,HEIGHT))

# Tank
tankX = 358
tankY = 400
justTank = Character(tankX, tankY, window, 'tank (3).png')


def tankMovement(key_pressed, tank):
    if key_pressed[pygame.K_d]:
        tank.moveRight()
    elif key_pressed[pygame.K_a]:
        tank.moveLeft()


# Bullet
bullletPicMe = pygame.image.load('bullet (1).png')
bullet_x = 358
bullet_y = 0
by_change = 10
bulletState = 'ready'  # ready ==> you cant see the bullet on the screen. # fire ==> the bullet is currently moving.


def bulletMe(x, y):
    global bulletState
    bulletState = 'fire'
    window.blit(bullletPicMe, (x, y))


# Enemy tank


opponentOneX, opponentTwoX, opponentThreeX, opponentFourX, opponentFiveX, opponentSixX = 110, 210, 310, 410, 510, 610
opponentOneY, opponentTwoY, opponentThreeY, opponentFourY, opponentFiveY, opponentSixY = 50, 50, 50, 50, 50, 50
justOpponent1 = opponetTank(opponentOneX, opponentOneY, window, 100, 'tank (4).png')
justOpponent2 = opponetTank(opponentTwoX, opponentTwoY, window, 100, 'tank (4).png')
justOpponent3 = opponetTank(opponentThreeX, opponentThreeY, window, 100, 'tank (4).png')
justOpponent4 = opponetTank(opponentFourX, opponentFourY, window, 100, 'tank (4).png')
justOpponent5 = opponetTank(opponentFiveX, opponentFiveY, window, 100, 'tank (4).png')
justOpponent6 = opponetTank(opponentSixX, opponentSixY, window, 100, 'tank (4).png')


def enemyTankMovement(tank):
    tank.move()


def collided(bx, by, ex, ey):
    distance = math.sqrt((math.pow(ex - bx, 2)) + (math.pow(ey - by, 2)))
    if distance < 27:
        return True
    else:
        return False


def healthbar(player_health, display, collided):
    if collided:
        player_health -= 5


# Main code to be run
running = True
while running:
    key_pressed = pygame.key.get_pressed()
    clock.tick(FPS)
    for event in pygame.event.get():
        # Quitting the game
        if event.type == pygame.QUIT:
            running = False

        if key_pressed[pygame.K_SPACE]:
            # If the bullet has been reloaded to fire.
            if bulletState == 'ready':
                bulletSound = mixer.Sound('ES_Missile Launch 5 - SFX Producer.mp3')
                bulletSound.play()
                bullet_x = justTank.x
                bulletMe(bullet_x, bullet_y)
    # Displaying window and tank.
    window.blit(background,(0,0))
    justTank.display()
    # If the bullet gets out of the screen
    if bullet_y <= 0:
        bullet_y = justTank.y
        # Reloaded.
        bulletState = 'ready'
    # If bullet is fired
    if bulletState == 'fire':
        bulletMe(bullet_x, bullet_y)
        # Bullet X direction is changing.
        bullet_y -= by_change
    if justOpponent1.health > 0:
        justOpponent1.display()
        enemyTankMovement(justOpponent1)
        coll = collided(bullet_x, bullet_y, justOpponent1.x, justOpponent1.y)
        if coll:
            bullet_x = justTank.x
            bullet_y = 360
            bulletState = 'ready'
            justOpponent1.healthRecuded()

    if justOpponent2.health > 0:
        justOpponent2.display()
        enemyTankMovement(justOpponent2)
        coll = collided(bullet_x, bullet_y, justOpponent2.x, justOpponent2.y)
        if coll:
            bullet_x = justTank.x
            bullet_y = 360
            bulletState = 'ready'
            justOpponent2.healthRecuded()
    if justOpponent3.health > 0:
        justOpponent3.display()
        enemyTankMovement(justOpponent3)
        coll = collided(bullet_x, bullet_y, justOpponent3.x, justOpponent3.y)
        if coll:
            bullet_x = justTank.x
            bullet_y = 360
            bulletState = 'ready'
            justOpponent3.healthRecuded()

    if justOpponent4.health > 0:
        justOpponent4.display()
        enemyTankMovement(justOpponent4)
        coll = collided(bullet_x, bullet_y, justOpponent4.x, justOpponent4.y)
        if coll:
            bullet_x = justTank.x
            bullet_y = 360
            bulletState = 'ready'
            justOpponent4.healthRecuded()
    if justOpponent5.health > 0:
        justOpponent5.display()
        enemyTankMovement(justOpponent5)
        coll = collided(bullet_x, bullet_y, justOpponent5.x, justOpponent5.y)
        if coll:
            bullet_x = justTank.x
            bullet_y = 360
            bulletState = 'ready'
            justOpponent5.healthRecuded()

    if justOpponent6.health > 0:
        justOpponent6.display()
        enemyTankMovement(justOpponent6)
        coll = collided(bullet_x, bullet_y, justOpponent6.x, justOpponent6.y)
        if coll:
            bullet_x = justTank.x
            bullet_y = 360
            bulletState = 'ready'
            justOpponent6.healthRecuded()

    # Movement of the tank
    tankMovement(key_pressed, justTank)
    justOpponent1.healthBar(window, 600, 350)
    justOpponent2.healthBar(window, 600, 380)
    justOpponent3.healthBar(window, 600, 410)
    justOpponent4.healthBar(window, 600, 440)
    justOpponent5.healthBar(window, 600, 470)
    justOpponent6.healthBar(window, 600, 500)
    pygame.display.update()
