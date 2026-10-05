import raylibpy as raylib
from boids import Boid

import random
from vectors import tupl

width,height = 1900,1000
speed = 1

raylib.set_config_flags(raylib.FLAG_WINDOW_MAXIMIZED|raylib.FLAG_WINDOW_RESIZABLE|raylib.FLAG_MSAA_4X_HINT) 
raylib.init_window(width,height,"boids")

#raylib.set_window_opacity(0.5)

boidNumber = 200

boids:list[Boid] = []
for i in range(boidNumber):
    position = (random.randint(0,width),random.randint(0,height))
    velocity = (random.uniform(-100,100),random.uniform(-100,100))
    num = random.randint(0,100)
    if num <= 60:
        tag = 1
    elif num <= 100:
        
        tag = 2
    else:
        tag = 3
    boids.append(Boid(position,velocity,tag))


def update(boids,deltaTime):
    width = raylib.get_screen_width()
    height = raylib.get_screen_height()
    grid = constructBAH(boids,100)

    for boid in boids:
        boid.update(grid,deltaTime)

    for boid in boids:
        boid.position.x %= width
        boid.position.y %= height

def constructBAH(boids,gridSize):
    grid = {}
    for boid in boids:
        gridPos = tupl((boid.position / gridSize).floor())
        grid.setdefault(gridPos, []).append(boid)
    return grid

def draw(boids):
    raylib.clear_background((2,2,2,255))
    #raylib.draw_rectangle(0,0,width,height,(50,50,50,40))

    for boid in boids:
        boid.draw()

    raylib.draw_fps(10,10)
    raylib.end_drawing()


        



while not raylib.window_should_close():
    deltaTime = raylib.get_frame_time()
    update(boids,deltaTime*speed)
    draw(boids)

    