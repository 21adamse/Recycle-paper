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

is_game_over = False
is_game_complete = False
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
    new_actors=[]
    for item in actors_create:
        actor=Actor(item+"img")
        new_actors.append(actor)
    return new_actors

def layout_actors(new_actors):
    number_gaps = len(new_actors)+1
    gap_size = WIDTH // number_gaps
    random.shuffle(new_actors)
    for index,item in enumerate(new_actors):
        new_xpos = (index+1)*gap_size
        item.x = new_xpos

def animate_actors(new_actors):
    global animations
    for actor in new_actors:
        duration = startspeed-currentlevel
        actor.anchor = ("center","bottom")
        animations.append(animate(actor,duration = duration,on_finished = game_over,y = HEIGHT))

def stop_animation(animations):
    for animation in animations:
        if animation.running:
            animation.stop()

def makeitems(extraactors):
    itemscreate = get_options_create(extraactors)
    new_actors = create_actor(itemscreate)
    layout_actors(new_actors)
    animate_actors(new_actors)
    return new_actors

def game_complete():
    global items,currentlevel,animations,is_game_complete
    stop_animation(animations)
    if currentlevel == final_level:
        is_game_complete = True
    else:
        currentlevel += 1
        items=[]
        animations=[]

def game_over():
    global is_game_over
    is_game_over = True

def update():
    global items
    if len(items) == 0:
        items = makeitems(currentlevel)

def on_mouse_down(pos):
    global items, currentlevel
    for item in items:
        if item.collidepoint(pos):
            if "paper" in item.image:
                game_complete()
            else:
                game_over()

def draw():
    global items, currentlevel, gameover, gamecomplete
    screen.clear()
    screen.blit("bground",(0,0))
    if is_game_over:
        displaymessage("Game over","You lose")
    elif is_game_complete:
        displaymessage("Game complete","You win")
    else:
        for item in items:
            item.draw()
    
pgzrun.go()