
import pygame, sys, random
pygame.init()

class Slotmachine:
  def __init__ (self,wallet):
    self.slots = []
    self.wallet = wallet 
    self.symbols = ["🍒","🍇","🫐","🍑", "🍌", "🥝", "🍓", "🍋","🍒","🍇","🫐","🍑", "🍌", "🥝", "🍓", "🍋","🍒","🍇","🫐","🍑", "🍌", "🥝", "🍓", "🍋","🍒", "🍌", "🥝", "🍓", "🍋", "💎","💎"]
  def Pull(self):
    s1 = random.choice(self.symbols)
    s2 = random.choice(self.symbols)
    s3 = random.choice(self.symbols)
    self.slots.clear()
    self.slots.append(s1)
    self.slots.append(s2)
    self.slots.append(s3)

  def Checkmoney(self):
    if self.slots [0] == "💎" and self.slots[0] == self.slots[1] == self.slots[2]:
      return ("four")
    elif self.slots[0] == self.slots[1] == "💎" or self.slots[1] == self.slots[2] == "💎" or self.slots[0] == self.slots[2] == "💎":
      return ("three")
    elif self.slots[0] == "💎" or self.slots[1] == "💎" or self.slots[2] == "💎":
      return("two")
    elif self.slots[0] == self.slots[1] == self.slots[2]:
      return("three")
    elif self.slots[0] == self.slots[1] or self.slots[1] == self.slots[2] or self.slots[0] == self.slots[2]:
      return("two")
    else:
      return("none")
      
  def Make_bet(self,bet):
    if bet <= 0:
      return ("To low")
    if bet > self.wallet:
      return ("To high brokey")
  
    self.Pull()
    
    if self.Checkmoney() == "none":
      self.wallet -= bet
    if self.Checkmoney() == "two":
      self.wallet += 2.25*bet
    if self.Checkmoney() == "three":
      self.wallet += 3.25*bet
    if self.Checkmoney() == "four":
      self.wallet += 4*bet

    


WIN = pygame.display.set_mode((400, 300))
FPS = 60
pygame.display.set_caption("Slot")

BLACK = (0, 0, 0)
WHITE = (255,255,255)
FONT = pygame.font.SysFont('Sans-serif', 40)

banana = pygame.image.load("student/images/banana.png")
blueberry = pygame.image.load("student/images/blueberries.png")
cherry = pygame.image.load("student/images/cherry.png")
grape = pygame.image.load("student/images/grape.png")
kiwi = pygame.image.load("student/images/kiwi.png")
lemon = pygame.image.load("student/images/lemon.png")
peach = pygame.image.load("student/images/peach.png")
strawberry = pygame.image.load("student/images/strawberry.png")
diamond = pygame.image.load("student/images/diamond.png")
sound = pygame.mixer.Sound("student/images/slotmachine.ogg")

Fruit_dict = {"🍒" : cherry,"🍇" : grape,"🫐" : blueberry,"🍑" : peach, "🍌" : banana, "🥝" : kiwi, "🍓" : strawberry , "🍋" : lemon, "💎" : diamond}

def main():
  clock = pygame.time.Clock()
  s = Slotmachine(100)
  answer = ""
  isasking = True

  
  
  while True:
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if isasking == True:
            if event.key == pygame.K_BACKSPACE:
              answer = answer[0:-1] 
            elif event.key == pygame.K_RETURN and answer != "":
              isasking = False
              sound.play()
              s.Make_bet(int(answer))
              answer = ""
              isasking = True
            elif pygame.key.name(event.key).isdigit():
              answer += event.unicode
        # for i in answer:
        #   if i not in ['1',2,3,4,5,6,7,8,9,0]
        #     print
          
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()


      
      
      WIN.fill(BLACK)
      if s.slots:
        left_image = Fruit_dict[s.slots[0]]
        middle_image = Fruit_dict[s.slots[1]]
        right_image = Fruit_dict[s.slots[2]]
        WIN.blit(left_image,(0,100))
        WIN.blit(middle_image,(125,100))
        WIN.blit(right_image,(250,100))
        
      # WIN.blit(left,(25,40))
      # WIN.blit(middle,(50,40))
      # WIN.blit(right,(75,40))
        
      inputtext = FONT.render(answer,1,WHITE)
      WIN.blit(inputtext,(0,50))
      money_text = FONT.render(str(s.wallet),1,WHITE)
      WIN.blit(money_text,(0,0))
      pygame.display.update()
      clock.tick(FPS)

main()