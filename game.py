import pgzrun
from random import randint

TITLE = "Susie Chasing"
WIDTH = 600
HEIGHT = 500

score = 0
game_over = False

susie = Actor("susie")
susie.pos = 100,200

prey = Actor("prey")
prey.pos = 200,200

def draw():
    screen.blit("bg",(0,0))
    susie.draw()
    prey.draw()
    screen.draw.text(f"Score: {score}",color = "black",topleft = (10,10))

    if game_over == True:
        screen.fill("orange")
        screen.draw.text(f"Time is up! Your Final Score is: {score}",fontsize = 35, color = "white",midtop = (300,20))



def time_up():
    global game_over
    game_over = True

def prey_place():
    prey.x = randint(50,550)
    prey.y = randint(50,450)

def update():
   global score
   if keyboard.left:
    susie.x = susie.x - 2
   if keyboard.right:
    susie.x = susie.x + 2
   if keyboard.up:
    susie.y = susie.y - 2
   if keyboard.down:
    susie.y = susie.y + 2

   if susie.colliderect(prey):
    score = score + 10
    prey_place()
time = float(input("How long do you want it to take,seconds?: "))
clock.schedule(time_up,time)
pgzrun.go()

