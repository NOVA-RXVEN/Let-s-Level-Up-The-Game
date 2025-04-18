import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 70
MID_FONT_SIZE = 35
SMALL_FONT_SIZE = 30

pygame.init()
background_image = pygame.transform.scale( pygame.image.load("bg1.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont("Times New Roman", FONT_SIZE)
small_font = pygame.font.SysFont("Times New Roman", SMALL_FONT_SIZE)
mid_font = pygame.font.SysFont("Times New Roman", MID_FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, color, height, width):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color("dodgerblue"))
        
        pygame.draw.rect(self.image, color, (0,0, width, height))
        self.rect = self.image.get_rect()
        
    def move(self,x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)
        
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("COLLISIONN")

all_sprites = pygame.sprite.Group()

sprite1 = Sprite(pygame.Color('cyan'), 30, 30)
sprite1.rect.x = random.randint(0, SCREEN_WIDTH - sprite1.rect.width)
sprite1.rect.y = random.randint(0, SCREEN_HEIGHT - sprite1.rect.width)
all_sprites.add(sprite1)

sprite2 = Sprite(pygame.Color('darkgreen'), 30,30)
sprite2.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
sprite2.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.width)
all_sprites.add(sprite2)

running, won = True, False
clock = pygame.time.Clock()
score = 0

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.type == pygame.K_x):
            pygame.quit()
            running = False
            
    if not won:
        keys = pygame.key.get_pressed()
        
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
        
        sprite1.move(x_change, y_change)
        
        if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            sprite2.rect.x = random.randint(0, SCREEN_WIDTH - sprite2.rect.width)
            sprite2.rect.y = random.randint(0, SCREEN_HEIGHT - sprite2.rect.width)
            all_sprites.add(sprite2)
            
            score = score + 1
            
            if score >= 10:
                won = True
    
    screen.blit(background_image, (0,0))
    all_sprites.draw(screen)
    
    headline_text = mid_font.render(f"Score 10 to Win the Game!", True, pygame.Color("navy blue"))
    screen.blit(headline_text, (55,5))
    
    score_text = small_font.render(f"Score: {score}", True, pygame.Color("navy blue"))
    screen.blit(score_text, (190,40))
    
    if won:
        win_text = font.render("You win!", True, pygame.Color('yellow'))
        screen.blit(win_text, ((SCREEN_WIDTH - win_text.get_width()) // 2,(SCREEN_HEIGHT - win_text.get_height()) // 2.5))
        
    pygame.display.flip()
    clock.tick(90)