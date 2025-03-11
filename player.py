# Player code

from circleshape import *
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, shots_group, drawable_group, updatable_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0

        self.shots_group = shots_group
        self.drawable_group = drawable_group
        self.updatable_group = updatable_group
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.shot_timer <= 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = (pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED)
            self.shot_timer = PLAYER_SHOT_COOLDOWN

            self.shots_group.add(shot)
            self.drawable_group.add(shot)
            self.updatable_group.add(shot)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        self.shot_timer -= dt
    
    