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
pygame.display.set_caption("AVC")
pygame.display.set_icon(icon)
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
mixer.music.load('bensound-epic.mp3')
mixer.music.play(-1)

# COlOURS
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
font = pygame.font.Font('robosapien.ttf', 25)
# Background image
background = pygame.transform.scale(pygame.image.load('photo_2022-02-17_20-17-00.jpg'), (WIDTH, HEIGHT))
# Tank
tankX = 358
tankY = 480
justTank = Character(tankX, tankY, window, 'tank (3).png')


def tankMovement(key_pressed, tank):
    if key_pressed[pygame.K_d]:
        if tank.x < 749:
            tank.moveRight()
    elif key_pressed[pygame.K_a]:
        if tank.x > 50:
            tank.moveLeft()


# Bullet
bullletPicMe = pygame.image.load('bullet (1).png')
bullet_x = 0
bullet_y = 0
by_change = 10
numberOfBullets = 8
bulletState = 'ready'  # ready ==> you cant see the bullet on the screen. # fire ==> the bullet is currently moving.


def bulletMe(x, y):
    global bulletState
    bulletState = 'fire'
    window.blit(bullletPicMe, (x, y))


# Enemy tank
opponentOneX, opponentTwoX, opponentThreeX, opponentFourX, opponentFiveX, opponentSixX = 110, 210, 310, 410, 510, 610
opponentOneY, opponentTwoY, opponentThreeY, opponentFourY, opponentFiveY, opponentSixY = random.randint(15,
                                                                                                        25), random.randint(
    25, 30), random.randint(30, 35), random.randint(25, 30), random.randint(15, 25), random.randint(20, 40)
justOpponent1 = opponetTank(opponentOneX, opponentOneY, window, 70, 'tank (5).png', random.uniform(0.1, 0.5))
justOpponent2 = opponetTank(opponentTwoX, opponentTwoY, window, 70, 'tank (5).png', random.uniform(0.1, 0.5))
justOpponent3 = opponetTank(opponentThreeX, opponentThreeY, window, 100, 'tank (4).png', 0.11)
justOpponent4 = opponetTank(opponentFourX, opponentFourY, window, 100, 'tank (4).png', 0.11)
justOpponent5 = opponetTank(opponentFiveX, opponentFiveY, window, 70, 'tank (5).png', random.uniform(0.1, 0.3))
justOpponent6 = opponetTank(opponentSixX, opponentSixY, window, 70, 'tank (5).png', random.uniform(0.1, 0.3))


def enemyTankMovement(tank):
    tank.move()


# Collision calculation
def collided(bx, by, ex, ey):
    distance = math.sqrt((math.pow(ex - bx, 2)) + (math.pow(ey - by, 2)))
    if distance < 27:
        return True
    else:
        return False


# Main code to be executed
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
    window.blit(background, (0, 0))
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
    # Shot on opponent tank 1
    if justOpponent1.health > 0:
        justOpponent1.display()
        enemyTankMovement(justOpponent1)
        coll = collided(bullet_x, bullet_y, justOpponent1.x, justOpponent1.y)
        if coll:
            justOpponent1.horizontalMovement()
            bullet_x = justTank.x
            bullet_y = justTank.y
            bulletState = 'ready'
            justOpponent1.healthRecuded()
    # Shot on opponent tank 1
    if justOpponent2.health > 0:
        justOpponent2.display()

        enemyTankMovement(justOpponent2)
        coll = collided(bullet_x, bullet_y, justOpponent2.x, justOpponent2.y)
        if coll:
            justOpponent2.horizontalMovement()
            bullet_x = justTank.x
            bullet_y = justTank.y
            bulletState = 'ready'
            justOpponent2.healthRecuded()
    # Shot on opponent tank 3
    if justOpponent3.health > 0:
        justOpponent3.display()

        enemyTankMovement(justOpponent3)
        coll = collided(bullet_x, bullet_y, justOpponent3.x, justOpponent3.y)
        if coll:
            justOpponent3.horizontalMovement()
            bullet_x = justTank.x
            bullet_y = justTank.y
            bulletState = 'ready'
            justOpponent3.healthRecuded()
    # Shot on opponent tank 4
    if justOpponent4.health > 0:
        justOpponent4.display()

        enemyTankMovement(justOpponent4)
        coll = collided(bullet_x, bullet_y, justOpponent4.x, justOpponent4.y)
        if coll:
            justOpponent4.horizontalMovement()
            bullet_x = justTank.x
            bullet_y = justTank.y
            bulletState = 'ready'
            justOpponent4.healthRecuded()
    # Shot on opponent tank 5
    if justOpponent5.health > 0:
        justOpponent5.display()
        enemyTankMovement(justOpponent5)
        coll = collided(bullet_x, bullet_y, justOpponent5.x, justOpponent5.y)
        if coll:
            justOpponent5.horizontalMovement()
            bullet_x = justTank.x
            bullet_y = justTank.y
            bulletState = 'ready'
            justOpponent5.healthRecuded()
    # Shot on opponent tank 6
    if justOpponent6.health > 0:
        justOpponent6.display()

        enemyTankMovement(justOpponent6)
        coll = collided(bullet_x, bullet_y, justOpponent6.x, justOpponent6.y)
        if coll:
            justOpponent6.horizontalMovement()
            bullet_x = justTank.x
            bullet_y = justTank.y
            bulletState = 'ready'
            justOpponent6.healthRecuded()
    if (
            justOpponent1.health == 0 and justOpponent2.health == 0 and justOpponent3.health == 0 and justOpponent4.health == 0 and justOpponent5.health == 0 and justOpponent6.health == 0) or (
            justOpponent1.y >= 450 or justOpponent2.y >= 450 or justOpponent3.y >= 450 or justOpponent4.y >= 450 or justOpponent5.y >= 450 or justOpponent6.y >= 450):

        if justOpponent1.health == 0 and justOpponent2.health == 0 and justOpponent3.health == 0 and justOpponent4.health == 0 and justOpponent5.health == 0 and justOpponent6.health == 0:
            over_test = font.render('SAFE FROM INVASION', True, (255, 255, 255))
            window.blit(over_test, (280, 250))
        else:
            over_test = font.render('INVADED', True, (255, 255, 255))
            window.blit(over_test, (350, 250))
        justOpponent1.x += 1000
        justOpponent2.x += 1000
        justOpponent3.x += 1000
        justOpponent4.x += 1000
        justOpponent5.x += 1000
        justOpponent6.x += 1000
        justTank.x += 1000
    # Movement of our tank.
    tankMovement(key_pressed, justTank)
    # Health count of the opponent tanks.
    justOpponent1.healthBar(window, 660, 350)
    justOpponent2.healthBar(window, 660, 380)
    justOpponent3.healthBar(window, 660, 410)
    justOpponent4.healthBar(window, 660, 440)
    justOpponent5.healthBar(window, 660, 470)
    justOpponent6.healthBar(window, 660, 500)
    pygame.display.update()