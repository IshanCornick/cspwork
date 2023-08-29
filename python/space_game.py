import pygame, sys

pygame.init()

SCREENWIDTH,SCREENHEIGHT = 500,400
FPS = 60
WIN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("pygame_temp")
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255,0,0)
WHITE = (255,255,255)
#timer = 0

BG = pygame.image.load("student/images/Spaceback.jpg")
BG = pygame.transform.scale(BG, (SCREENWIDTH, SCREENHEIGHT))
GAMEOVER = pygame.image.load("student/images/download.png")
GAMEOVER = pygame.transform.scale(GAMEOVER, (SCREENWIDTH, SCREENHEIGHT))

HITSOUND = pygame.mixer.Sound("student/images/hit-2.ogg")
SHOOTSOUND = pygame.mixer.Sound("student/images/pew.ogg")
REDIMAGE = pygame.image.load("student/images/spaceship_red.png")
REDIMAGE = pygame.transform.scale(REDIMAGE, (55, 40))
REDIMAGE = pygame.transform.rotate(REDIMAGE, -90)
YELLOWIMAGE = pygame.image.load("student/images/spaceship_yellow.png")
YELLOWIMAGE = pygame.transform.scale(YELLOWIMAGE, (55, 40))
YELLOWIMAGE = pygame.transform.rotate(YELLOWIMAGE, 90)
HEALTH_FONT = pygame.font.SysFont("Sans-serif", 40)
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
boarder = pygame.Rect(SCREENWIDTH/2-5,0,10,SCREENHEIGHT)

def yellowmovement(keys_pressed, yellow):
  if keys_pressed[pygame.K_a] and yellow.x > 0:
    yellow.x -= 5
  if keys_pressed[pygame.K_d] and yellow.right <= boarder.left +16:
    yellow.x += 5
  if keys_pressed[pygame.K_w] and yellow.top >= 0:
    yellow.y -= 5
  if keys_pressed[pygame.K_s] and yellow.bottom <= SCREENHEIGHT:
    yellow.y += 5
def redmovement(keys_pressed, red):
  if keys_pressed[pygame.K_LEFT] and red.x >= boarder.right:
    red.x -= 5
  if keys_pressed[pygame.K_RIGHT] and red.right <= SCREENWIDTH:
    red.x += 5
  if keys_pressed[pygame.K_UP] and red.top >= 0:
    red.y -= 5
  if keys_pressed[pygame.K_DOWN] and red.bottom <= SCREENHEIGHT:
    red.y += 5
      
def handle_bullets(yellow_bullet, red_bullet, r, y):
  for i in red_bullet:
    i.x -= 10
    if y.colliderect(i):
      pygame.event.post(pygame.event.Event(YELLOW_HIT))
      red_bullet.remove(i)
    elif i.x < 0:
      red_bullet.remove(i)
      
  for i in yellow_bullet:
    i.x += 10
    if r.colliderect(i):
      pygame.event.post(pygame.event.Event(RED_HIT))
      yellow_bullet.remove(i)
    elif i.x > SCREENWIDTH:
      yellow_bullet.remove(i)


def main():
  global BG
  red_hp = 10
  yellow_hp = 10
  clock = pygame.time.Clock()
  red = pygame.Rect(375,200, 55, 40 )
  yellow = pygame.Rect(125,200, 55, 40)
  red_bullet = []
  yellow_bullet = []
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LSHIFT:
          Bullet = pygame.Rect(yellow.right - 35, yellow.centery +3, 25, 5)
          yellow_bullet.append(Bullet)
          SHOOTSOUND.play()
        if event.key == pygame.K_RSHIFT:
          Bullet2 = pygame.Rect(red.left, red.centery + 3, 25, 5)
          red_bullet.append(Bullet2)
          SHOOTSOUND.play()
      if event.type == RED_HIT:
        red_hp -= 1
        HITSOUND.play()
      if event.type == YELLOW_HIT:
        yellow_hp -= 1
        HITSOUND.play()

    handle_bullets(yellow_bullet, red_bullet, red, yellow)

    keys_pressed = pygame.key.get_pressed()
    yellowmovement(keys_pressed, yellow)
    redmovement(keys_pressed, red)
  
    if red_hp <= 0:
      print ("Yellow wins")
      break
     
    elif yellow_hp <= 0:
      print ("Red wins")
      break
      
    


    WIN.fill(BLACK)
    WIN.blit(BG, (0,0))
    pygame.draw.rect(WIN, BLACK, boarder)
    WIN.blit(REDIMAGE, (red.x,red.y))
    WIN.blit(YELLOWIMAGE, (yellow.x,yellow.y))
    for i in yellow_bullet:
      pygame.draw.rect(WIN, YELLOW, i)
    for i in red_bullet:
      pygame.draw.rect(WIN, RED, i)

    red_text = HEALTH_FONT.render("Hp: " + str(red_hp), 1, WHITE)
    yellow_text = HEALTH_FONT.render("Hp: " + str(yellow_hp), 1, WHITE)
    WIN.blit(red_text, (375,0))
    WIN.blit(yellow_text, (0,0))
    pygame.display.update()
    clock.tick(FPS)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      
    
    WIN.fill(BLACK)
    WIN.blit(GAMEOVER, (0,0))
    pygame.display.update()
    clock.tick(FPS)


main()