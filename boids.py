from vectors import vector, Vector2,tupl,normalised
import random
import raylibpy as raylib
import math

freedom = 100


class Boid():
    def __init__(self,position,velocity,tag,avoidEdges = True):
        self.tag = tag
        self.radius = 5

        self.avoidEdges = avoidEdges
        
        self.position = vector(position)
        self.velocity = vector(velocity)
        self.acceleration = Vector2(0,0)
        self.perception = 100
        self.maxSpeed = 200

        if tag == 2 :
            self.maxSpeed = 400
        self.maxForce = 50

        self.maxSpeed += random.uniform(-20,20)
        self.maxForce += random.uniform(-4,4)

        self.alignWeight = random.uniform(0.8, 1.6)
        self.cohereWeight = random.uniform(0.6, 1.4)
        self.separateWeight = random.uniform(2.5, 4.0)

        # self.alignWeight = 0
        # self.cohereWeight = 0
        # self.separateWeight = 3

        #self.separateWeight = 2
        avg = (self.alignWeight + self.cohereWeight + self.separateWeight ) / 3
        if self.tag == 1:
            #self.colour = (255,255,255,255)
            self.colour = (100 + avg*65,20,30,255)
        elif self.tag == 2:
            self.colour = (50,50,100 + avg*65,255)
        else:
            self.colour = (0,100 + avg*65,0,255)


    def draw(self):
        angle = self.velocity.angle()
        lx = self.radius * math.cos(angle - math.radians(90))
        ly = self.radius * math.sin(angle - math.radians(90))
        left = Vector2(lx,ly) + self.position
        rx = self.radius * math.cos(angle + math.radians(90))
        ry = self.radius * math.sin(angle + math.radians(90))
        right = Vector2(rx,ry) + self.position
        raylib.draw_triangle((normalised(self.velocity)*15+self.position).tupl(),left.tupl(),right.tupl(),self.colour)
        #raylib.draw_circle_v(tupl(self.position),self.radius,self.colour)

    def update(self,grid,deltaTime):
        drag = 0.002
        self.acceleration = Vector2(0,0)
        boids = getNearbyBoids((self.position / self.perception).floor(),grid)
        alignment = self.align(boids)
        cohesion = self.cohere(boids)
        separation = self.separate(boids)

        if self.avoidEdges:
            avoid = self.avoid()
            self.acceleration += avoid * 10

        self.acceleration += alignment * self.alignWeight
        self.acceleration += cohesion * self.cohereWeight
        self.acceleration += separation * self.separateWeight
        if raylib.is_mouse_button_down(raylib.MOUSE_BUTTON_LEFT) == True:
            mouseX = raylib.get_mouse_x()
            mouseY = raylib.get_mouse_y()
            self.acceleration += self.pointAttract((mouseX,mouseY)) * 2
        self.acceleration += Vector2(random.uniform(-freedom,freedom),random.uniform(-freedom,freedom))

        self.velocity += self.acceleration * deltaTime
        self.velocity += -drag * self.velocity * self.velocity.magnitude() * deltaTime
        self.velocity.limit(self.maxSpeed)
        self.position += self.velocity * deltaTime
        
        
    def align(self,boids):
        force = Vector2(0,0)
        averageVelocity = Vector2(0,0)
        total = 0
        for boid in boids:
            if boid.tag != self.tag:
                continue
            if self is boid: 
                continue
            distance = (self.position - boid.position).lengthSquared()
            if distance < self.perception**2:
                averageVelocity += boid.velocity
                total += 1
        if total > 0:
            averageVelocity /= total
            force = averageVelocity
            force.setMagnitude(self.maxSpeed)
            force -= self.velocity
            force.limit(self.maxForce)

        return force
    
    def cohere(self,boids):
        force = Vector2(0,0)
        averagePosition = Vector2(0,0)
        total = 0
        for boid in boids:
            if boid.tag != self.tag:
                continue
            if self is boid:
                continue
            distance = (self.position - boid.position).lengthSquared()
            if distance < self.perception**2:
                averagePosition += boid.position
                total += 1
        if total > 0:
            averagePosition /= total
            force = averagePosition
            force -= self.position
            force.setMagnitude(self.maxSpeed)
            force -= self.velocity
            force.limit(self.maxForce)

        return force
    
    def separate(self,boids):
        force = Vector2(0,0)
        total = 0

        for boid in boids:
            distance = (self.position - boid.position).lengthSquared()
            if boid.tag == self.tag:
                if self is boid:
                    continue
                if distance < 50**2:
                    toSelf = self.position - boid.position
                    toSelf /= distance**1
                    force += toSelf
                    total += 1
            else:
                if distance < 100**2:
                    toSelf = self.position - boid.position
                    toSelf /= distance
                    force += toSelf *1.5
                    total += 1

        if total > 0:
            force /= total
            force.setMagnitude(self.maxSpeed)
            force -= self.velocity
            force.limit(self.maxForce)
        return force
    
    def pointAttract(self,point):
        point = vector(point)
        force = Vector2(0,0)
        distance = (self.position - point).lengthSquared()
        if distance < 1000**2:
            force = point - self.position
            force.setMagnitude(self.maxSpeed)
            force -= self.velocity
            force.limit(self.maxForce)

        return force
    
    def avoid(self):
        distance = 300
        width = raylib.get_screen_width()
        height = raylib.get_screen_height()
        force = Vector2(0,0)
        try:
            if self.position.y < distance:
                point = Vector2(self.position.x,0)
                diff = self.position - point
                force += diff/diff.magnitude()
            elif self.position.y > height -distance:
                point = Vector2(self.position.x,height)
                diff = self.position - point
                force += diff/diff.magnitude()
            if self.position.x < distance:
                point = Vector2(0,self.position.y)
                diff = self.position - point
                force += diff/diff.magnitude()
            elif self.position.x > width - distance:
                point = Vector2(width,self.position.y)
                diff = self.position - point
                force += diff/diff.magnitude()
        except:
            pass

        return force * 20

            


def getNearbyBoids(gridPos,grid) -> list:
    boids = []
    for x in range(gridPos.x-1,gridPos.x+2):
        for y in range(gridPos.y-1,gridPos.y+2):
            if (x,y) in grid:
                boids.extend(grid[(x,y)])

    return boids
            