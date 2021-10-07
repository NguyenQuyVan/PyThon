import pgzrun
import random
from random import randint
#độ rộng màn hình game
WIDTH=800
HEIGHT=600
score=0
#xuất hiện phi thuyền
ship=Actor('playership1_blue1')
ship.x=370
ship.y=550
game_over=False
gem=Actor('gemblue')
gem.x=200
gem.y=0

meto=Actor('meteorgrey_big1')
meto.x=395
meto.y=0

#di chuyển phi thuyền
def on_mouse_move(pos,rel,buttons):
    ship.x=pos[0]
    ship.y=pos[1]
def update():
    global score , game_over
    gem.y=gem.y+4+score/4 #tốc độ kim cương
    meto.y=meto.y+4+score/4
    if gem.y>600:
        gem.y=0
    if meto.y>600:
        meto.y=0
    if gem.colliderect(ship):
        gem.x=random.randint(20,780)
        gem.y=0
        score=score+1
        sounds.epe.play()
    if meto.colliderect(ship):
        meto.x=random.randint(20,780)
        meto.y=0
        game_over=True
        sounds.bumm.play()
        sounds.gameover.play()

def draw():
    screen.fill((0,0,0))
    if game_over:
        screen.draw.text('game over',(280,250),color=(255,255,255),fontsize=60)
        screen.draw.text('Final score:'+str(score),(200,200),color=(255,0,255),fontsize=80)
    else:
      screen.draw.text('score:'+str(score),(10,15),color=(255,255,255),fontsize=60)
      ship.draw()
      gem.draw()
      meto.draw()
pgzrun.go()
