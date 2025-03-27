import pgzrun
import random

HEIGHT=600
WIDTH=800
TITLE="Recycle paper"

centre_x = WIDTH/2
centre_y = HEIGHT/2
final_level = 10
startspeed = 10
ITEMS = ("battery","bottle","chips","bag")

gameover = False
gamecomplete = False
currentlevel = 1
items = []
animations = []

def displaymessage(heading,subtext):
    screen.draw.text(heading,fontsize = 60,center = (centre_x,centre_y),color = "white")
    screen.draw.text(subtext,fontsize = 30,center = (centre_x,centre_y + 60),color = "white")

def get_options_create(extraactors):
    actors_create = ["paper"]
    for i in range(extraactors):
        option = random.choice(ITEMS)
        actors_create.append(option)
    return actors_create

def create_actor(actors_create):
    pass

def layout_actors(new_actors):
    pass

def makeitems(extraactors):
    itemscreate = get_options_create(extraactors)
    new_actors = create_actor(itemscreate)
    layout_actors(new_actors)

def update():
    global items
    if len(items) == 0:
        items = makeitems(currentlevel)

def draw():
    global items, currentlevel, gameover, gamecomplete
    screen.clear()
    screen.blit("bground",(0,0))
    if gameover:
        displaymessage("Game over","You lose")
    elif gamecomplete:
        displaymessage("Game complete","You win")
    else:
        for item in items:
            item.draw()
    
pgzrun.go()