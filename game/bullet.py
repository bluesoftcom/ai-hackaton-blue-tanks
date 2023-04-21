import math
import pygame

class Bullet:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 10
        self.gravity = 0.5
        self.radius = 5
        self.time = 1

    def update(self, terrain):
        # Calculate position based on angle, speed and time
        x_offset = math.cos(math.radians(self.angle)) * self.speed
        y_offset = -math.sin(math.radians(self.angle)) * self.speed + 0.5 * self.gravity * self.time
        self.x += x_offset
        self.y += y_offset
        self.time += 1

        # Check for collision with terrain
        terrain_bottom = terrain.get_y(self.x)
        if self.y >= terrain_bottom:
            self.y = terrain_bottom
            return True  # Bullet hit the ground
        return False  # Bullet still in the air


    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2))

def fire(tank, angle):
    bullet = Bullet(tank.x + tank.width/2, tank.y + tank.height/2, angle)
    bullets = []
    bullets.append(bullet)