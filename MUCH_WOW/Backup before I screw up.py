#This incredible, rarted game was programmed by the one and only, Boyd Kirkman.
#Feel free to update/add to the game!


import sys
import random
import math
import pygame
import pygame.locals
from time import sleep


width = 1280
height = 720

pygame.init()

#~~~~~~~~~~~~~~~~~~~~~~~~~~Loading in Sounds/Music~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

global triple
global damnson
global gotcha
global boomheadshot
global screech
global sounds
global MKMLG
triple = pygame.mixer.Sound("triple.wav")
damnson = pygame.mixer.Sound("damnson.wav")
gotcha = pygame.mixer.Sound("gotcha.wav")
boomheadshot = pygame.mixer.Sound("boomheadshot.wav")
screech = pygame.mixer.Sound("screech.wav")
sounds = [triple, damnson, boomheadshot]
MKMLG = pygame.mixer.music.load("MKMLG.mp3")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~NO LEAVING MECHANIC~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def No_Leaving():

    otherdoge = pygame.image.load('No.png')
    R = otherdoge.get_rect()
    X = width/2 - R.center[0] + 20
    if pygame.QUIT in [e.type for e in pygame.event.get()]:
            screen = pygame.display.set_mode((width,height))
            font = pygame.font.SysFont("freeserif", 72, bold = 1)
            textSurface = font.render("Don't Leave!", 1,
                                      pygame.Color(255,4,4))
            screen.blit(textSurface,(width/2-R.center[0], height/2-R.center[1]))
            while True:
                #Angry Doge:
                screen.blit(otherdoge, (X, height/2 - R.center[1]))
                pygame.display.update()
                if pygame.QUIT in [e.type for e in pygame.event.get()]:
                    break

#~~~~~~~~~~~~~~~~~~~~~~~~~Setting up the Doge Sprite~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Doge(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("run1.png").convert_alpha()
        self.rect = self.image.get_rect()
        #Orientation
        global Orient
        Orient = 0
        #Trying to animate a gif
        global blip
        blip = 0
        global image_changing_score
        image_changing_score = 0

    def update(self):
        #trying to animate a gif
        global blip
        blip += 1
        global image_changing_score
        if blip == 50:
            image_changing_score += 1
            blip = 0
        if image_changing_score % 2 == 0:
            self.image =

        global Orient
        #Exiting via a mouse click on the doge
        x,y = pygame.mouse.get_pos()
        if x >= self.rect.x and x <= self.rect.x + 139:
            Mouse_Location_X = True
        if x < self.rect.x or x > self.rect.x + 139:
            Mouse_Location_X = False
        if y >= self.rect.y and y <= self.rect.y + 92:
            Mouse_Location_Y = True
        if y < self.rect.y or y > self.rect.y + 92:
            Mouse_Location_Y = False
        if pygame.mouse.get_pressed()[0] and Mouse_Location_X == True and Mouse_Location_Y == True:
            pygame.quit()
        #No flying
        if self.rect.y < 340:
            self.rect.y += 20
        #Orientation
        if Orient == 0:
            self.image = pygame.image.load("run1.png").convert_alpha()
        if Orient == 1:
            self.image = pygame.image.load("run1.png").convert_alpha()
            self.image = pygame.transform.flip(self.image, True, False)
        #Moving
        if pygame.key.get_pressed()[pygame.K_RIGHT] and self.rect.x < 1170:
            if score == 0:
                self.rect.x += 10
            if score != 0 and score <= 4:
                self.rect.x += score*10
            if score > 4:
                self.rect.x += 60
            self.image = pygame.image.load("moving?.png").convert_alpha()
            Orient = 0
        if pygame.key.get_pressed()[pygame.K_LEFT] and self.rect.x > 0:
            if score == 0:
                self.rect.x -= 10
            if score != 0 and score <= 4:
                self.rect.x -= score*10
            if score > 4:
                self.rect.x -= 60
            self.image = pygame.image.load("moving?.png").convert_alpha()
            self.image = pygame.transform.flip(self.image, True, False)
            Orient = 1
        if pygame.key.get_pressed()[pygame.K_UP] and self.rect.y > 340:
            if score == 0:
                self.rect.y -= 10
            if score != 0 and score <= 4:
                self.rect.y -= score*10
            if score > 4:
                self.rect.y -= 60
        if pygame.key.get_pressed()[pygame.K_DOWN] and self.rect.y < 640:
            if score == 0:
                self.rect.y += 10
            if score != 0 and score <= 4:
                self.rect.y += score*10
            if score > 4:
                self.rect.y += 60

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Doritos~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Doritos(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("Doritos.png").convert_alpha()
        self.rect = self.image.get_rect()

    def it_be_spawning(self):
        self.rect.x = random.randrange(1,1170)
        self.rect.y = random.randrange(340,640)

    def oh_no_it_be_eaten(self):
        global score
        if pygame.sprite.collide_mask(doge, doritos):
            pygame.mixer.Sound.play(random.choice(sounds))
            self.rect.x = random.randrange(1,1170)
            self.rect.y = random.randrange(340,640)
            score += 1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MLG Elmo~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class MLG_Elmo(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("Elmo_a_coma_for_ya.png").convert_alpha()
        self.rect = self.image.get_rect()

    def did_elmo_get_ya(self):
        if self.rect.x > doge.rect.x:
            self.rect.x += -1*score
        if self.rect.x < doge.rect.x:
            self.rect.x += 1*score
        if self.rect.y > doge.rect.y:
            self.rect.y += -1*score
        if self.rect.y < doge.rect.y:
            self.rect.y += 1*score
        if pygame.sprite.collide_mask(self, doge):
            game_over()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~The Sun~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class sun(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("sun.png").convert_alpha()
        self.rect = self.image.get_rect()

    def the_sun_turns(self):
        if self.rect.x > doge.rect.x:
            self.rect.x += -3
        if self.rect.x < doge.rect.x:
            self.rect.x += 3
        if self.rect.y > doge.rect.y:
            self.rect.y += -3
        if self.rect.y < doge.rect.y:
            self.rect.y += 3
        if pygame.sprite.collide_mask(self, doge):
            game_over()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Restart Button~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class revive_button(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("revive_button_untouched.png").convert_alpha()
        self.rect = self.image.get_rect()
    def sensing_click(self):
        x,y = pygame.mouse.get_pos()
        if x >= width/2-50 and x <= width/2+50:
            Mouse_Location_X = True
        if x < width/2-50 or x > width/2+50:
            Mouse_Location_X = False
        if y >= 570 and y <= 620:
            Mouse_Location_Y = True
        if y < 570 or y > 620:
            Mouse_Location_Y = False
        #button functions
        if pygame.mouse.get_pressed()[0] and Mouse_Location_X == True and Mouse_Location_Y == True:
            Level_1()
        if Mouse_Location_X == True and Mouse_Location_Y == True:
            self.image = pygame.image.load("revive_button_touched.png").convert_alpha()
        else:
            self.image = pygame.image.load("revive_button_untouched.png").convert_alpha()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Title Screen~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def GameIntro():
    pygame.mixer.music.play(-1)
    intro_doge = pygame.image.load('doge.jpg')
    r = intro_doge.get_rect()
    direction = 2
    X = width/2 - r.center[0]

    window = pygame.display.set_mode((width,height))
    pygame.display.set_caption("MUCH WOW")

    intro_happening = True
    while intro_happening:
        window.blit(pygame.image.load('background.jpg'),(0,0))

        #DOGE
        window.blit(intro_doge, (X, -100))
        #Moving Doge
        X += direction
        if X >= width - r.width or X <= 0:
            direction *= -1

        #Title
        ffont = pygame.font.SysFont("freeserif", 190, bold = 1)
        ttextSurface = ffont.render("MUCH WOW", 1, pygame.Color(255,255,255))
        tt = ttextSurface.get_rect()
        window.blit(ttextSurface, (width/2 - tt.width/2 + 10, height/15))
        pygame.display.update()

        #Buttons
        def W_button():
            Font = pygame.font.SysFont("freesansbold", 100, bold = 1)
            TextSurface = Font.render("PLAY", 1, pygame.Color(255,255,255))
            T = TextSurface.get_rect()
            window.blit(TextSurface, (width/2 - T.width/2, height/2 - T.height/2))
            pygame.display.update()
        def B_button():
            Font = pygame.font.SysFont("freesansbold", 100, bold = 1)
            TextSurface = Font.render("PLAY", 1, pygame.Color(0,0,0))
            T = TextSurface.get_rect()
            window.blit(TextSurface, (width/2 - T.width/2, height/2 - T.height/2))
            pygame.display.update()
        #Mouse Location
        x,y = pygame.mouse.get_pos()
        if x >= width/2-50 and x <= width/2+50:
            Mouse_Location_X = True
        if x < width/2-50 or x > width/2+50:
            Mouse_Location_X = False
        if y >= height/2-30 and y <= height/2+30:
            Mouse_Location_Y = True
        if y < height/2-30 or y > height/2+30:
            Mouse_Location_Y = False
        #button functions
        if pygame.mouse.get_pressed()[0] and Mouse_Location_X == True and Mouse_Location_Y == True:
            Level_1()

        elif Mouse_Location_X == True and Mouse_Location_Y == True:
            B_button()

        else:
            W_button()

        No_Leaving()
        pygame.display.update()

#~~~~~~~~~~~~~~~~~~Level 1 (I'll add more later, hopefully...)~~~~~~~~~~~~~~~~~~


def Level_1():
    intro_happening = False
    global score
    score = 0
    Level1 = pygame.display.set_mode((width,height))
    #Set Doge location
    global doge
    doge = Doge()
    doge.rect.x = width/2-doge.rect.center[0]
    doge.rect.y = height/2-doge.rect.center[1]
    #Spawn Doritos
    global doritos
    doritos = Doritos()
    doritos.it_be_spawning()
    #Spawning in the Sun
    global sun_lol
    sun_lol = sun()
    sun_lol.rect.x = 1080
    sun_lol.rect.y = 100
    #Elmo's on his way!
    global elmo
    elmo = MLG_Elmo()
    elmo.rect.x = 50
    elmo.rect.y = 50
    #this is jsut a variable so that elmo screeches on entry!
    random_var = 0


    global game_in_play
    game_in_play = True
    while game_in_play:

        #Background
        Level1.blit(pygame.image.load('Background_lol.jpg').convert(),(0,0))
        #keeping score
        font = pygame.font.SysFont("freeserif", 72, bold = 1)
        textSurface = font.render(str(score), 1,
                                  pygame.Color(0,0,0))
        Level1.blit(textSurface,(50, 50))
        #Create Doge Sprite
        doge.update()
        Level1.blit(doge.image, doge.rect)
        #Spawn the Doritos
        doritos.oh_no_it_be_eaten()
        Level1.blit(doritos.image, doritos.rect)
        #The Sun
        if score >= 10:
            sun_lol.the_sun_turns()
        Level1.blit(sun_lol.image, sun_lol.rect)
        #The Triggering of MLG Elmo
        elmo.did_elmo_get_ya()
        if score >= 1:
            if random_var == 0:
                pygame.mixer.Sound.play(screech)
                random_var = 1
            Level1.blit(elmo.image, elmo.rect)
        #No leaving Mechanic
        No_Leaving()

        #Update screen
        pygame.display.update()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Game Over~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def game_over():
    pygame.mixer.Sound.stop(triple)
    pygame.mixer.Sound.stop(boomheadshot)
    pygame.mixer.Sound.stop(screech)
    pygame.mixer.Sound.stop(damnson)
    pygame.mixer.Sound.play(gotcha)
    global game_in_play
    game_in_play = False
    #The Revive Button
    button = revive_button()
    button.rect.x = width/2-50
    button.rect.y = 570
    while True:
        No_Leaving()
        window2 = pygame.display.set_mode((width,height))
        #picture of dead doge
        dd = pygame.image.load("dead_doge.png").convert_alpha()
        dd_dimensions = dd.get_rect()
        window2.blit(dd, (width/2 - dd_dimensions.height/2, height/2 - dd_dimensions.height/2))
        #The game over message
        Font = pygame.font.SysFont("freesansbold", 100, bold = 1)
        TextSurface = Font.render("You stole "+str(score)+" doritos!", 1, pygame.Color(255,255,255))
        T = TextSurface.get_rect()
        window2.blit(TextSurface, (width/2 - T.width/2, 50))
        #The game over message cont.
        lelFont = pygame.font.SysFont("freesansbold", 50, bold = 1)
        lelTextSurface = lelFont.render("But died...", 1, pygame.Color(255,25,25))
        lelT = lelTextSurface.get_rect()
        window2.blit(lelTextSurface, (width/2 - lelT.width/2, 150))
        #The revive Button
        button.sensing_click()
        window2.blit(button.image, button.rect)
        #updating the window
        pygame.display.update()




while __name__ == '__main__':
    GameIntro()
