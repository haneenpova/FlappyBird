import pygame as pg
import random  
import math

class Bird:
    def __init__(self, window, x, y ,color, radius):
    
        # if random.randint(0, 1):
        #     self.direction = 1
        # else:
        #     self.direction = -1

        self.window = window
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        # self.bird = pg.draw.circle(self.window, self.color, (self.x, self.y), 50)
    
    def render(self):
        pg.draw.circle(self.window, self.color, (self.x,self.y), self.radius)
        

#collision funcs
def collideCircle(raven, raven_x_pos, raven_y_pos, raven_radius):

    if math.sqrt(pow(raven.x - raven_x_pos, 2) + pow(raven.y - raven_y_pos, 2)) < (raven.radius + raven_radius):
        return True
    else:
        return False

# def collideFlappy(flappy_bird, raven_x_pos, raven_y_pos):
#     if math.sqrt(pow(flappy_bird.x - raven_x_pos, 2) + pow(flappy_bird.y - raven_y_pos, 2)) < (flappy_bird.radius*2):
#         return True
#     else:
#         return False

#keybinds
class Keys:
  def __init__(self):
    self.keys = {
      ord("w"):False,
      ord("d"):False,
      ord("s"):False,
      ord("a"):False,
      pg.K_SPACE:False
    }
  
  def update(self):
    for ev in pg.event.get():
      if ev.type == pg.KEYDOWN:
        if ev.key in self.keys:
          self.keys[ev.key] = True
      
      elif ev.type == pg.KEYUP:
        if ev.key in self.keys:
          self.keys[ev.key] = False

      elif ev.type == pg.K_RIGHT:
        if ev.key in self.keys:
          self.keys[ev.key] = True

      elif ev.type == pg.K_LEFT:
        if ev.key in self.keys:
          self.keys[ev.key] = True

      elif ev.type == pg.K_SPACE:
        if ev.key in self.keys:
          self.keys[ev.key] = True

keys = {

    ord("w"):False,
    ord("s"):False,
    ord("d"):False,
    ord("a"):False,
    pg.K_SPACE:False
        }

pg.init()

width, height = 800, 800
window = pg.display.set_mode((width, height))
clock = pg.time.Clock()
fps = 60

#FONT
text_font = pg.font.Font(None, 60)

#SCORE

def GameActive():
    
    title = pg.display.set_caption("Flappy bird")

    #bird
    flappy_x = 400
    flappy_y = 400
    flappy_bird = Bird(window, flappy_x, flappy_y, "#E24E1b", 20)
    flappy_gravity = 0 
    flappy_speed = 0

    # ravens
    ravens = [flappy_bird]
    # random_x = []
    # random_y = []

    # clock = pg.time.Clock()
    # fps = 60
    # score = 0

    

    raven_h = 0
    raven_w = 800
    raven_radius = 25 
    raven_gravity = 0

    game_active = True
    
    score = 0
    def dispaly_score():    
        ScoreSurface = text_font.render(f'score:{score}', False, "green")
        ScoreRect = ScoreSurface.get_rect(center = (400, 100))
        pg.draw.rect(window,"Pink",ScoreRect)      # rect's color
        window.blit(ScoreSurface, ScoreRect)

    # if game_active == True:
    for i in range(20):
        raven_x_pos = random.randint(raven_h + raven_radius, raven_w - raven_radius)
            # random_x.append(raven_x_pos)
        raven_y_pos = random.randint(raven_h + raven_radius, raven_w - raven_radius)   
        # random_y.append(raven_y_pos) 
        while True:
            for raven in ravens:   
                if collideCircle(raven, raven_x_pos, raven_y_pos, raven_radius*3): 
                    break  
            else:  
                break  
            raven_x_pos = random.randint(raven_h + raven_radius, raven_w - raven_radius)   
            # random_x.append(raven_x_pos) 
            raven_y_pos = random.randint(raven_h + raven_radius, raven_w - raven_radius)   
            # random_y.append(raven_y_pos) 
        ravens.append(Bird(window, raven_x_pos, raven_y_pos, color = "#0000FF", radius= raven_radius)) 
    ravens.pop(0)
    

    #keybinds
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()


            if event.type == pg.KEYDOWN:
                if event.key in keys:
                    keys[event.key] = True

            elif event.type == pg.KEYUP:
                if event.key in keys:
                    keys[event.key] = False

            #keybinds
            if keys[ord("w")]:
                if flappy_gravity >= 0:
                    # flappy_bird.x += 2
                    flappy_speed = -5


            # if keys[ord("s")]:
            #     if flappy_gravity >= 0:
            #         flappy_bird.y += 5


        window.fill("white")
        flappy_speed += 0.3
        flappy_bird.y += flappy_speed
        score += 1
        
        

        for raven in ravens:
            #raven animation
            if raven.x + raven.radius <= 0:
                raven_x_pos = width + raven.radius

                raven_y_pos = random.randint(raven_h + raven_radius , raven_w - raven_radius)
                while True:
                    for r in ravens:
                        if collideCircle(r, raven_x_pos, raven_y_pos, raven_radius*3):
                            break
                    else:
                        break
                    
                    raven_y_pos = random.randint(raven_h + raven_radius , raven_w - raven_radius)
                raven.x = raven_x_pos
                raven.y = raven_y_pos

            raven.x -= 2

            # flappy collison
            if collideCircle(flappy_bird, raven.x, raven.y, raven.radius):
                print("collision") 
                flappy_bird.color = "#FF0000"
                game_active = False 
                # pg.display.update()
            raven.render()


        # if game_active == False:
        #     break
        flappy_bird.render()

        if game_active == False:
            window.fill("blue") 
            TryAgain = text_font.render("Press space to try again", False, "green")
            TryAgainRect = TryAgain.get_rect(center = (400, 50))     
            window.blit(TryAgain, TryAgainRect)
            dispaly_score()
            return False
            
        pg.display.flip()
        clock.tick(fps) 

def GameOverScreen():
    while True:
        for event in pg.event.get():
            window.fill("blue") 
            StartGame = text_font.render("Press space to start the game", False, "green")
            StartGameRect = StartGame.get_rect(center = (400, 50))     
            window.blit(StartGame, StartGameRect)

            if event.type == pg.QUIT:
                pg.quit()

            if event.type == pg.KEYDOWN:
                if event.key in keys:
                    keys[event.key] = True

            elif event.type == pg.KEYUP:
                if event.key in keys:
                    keys[event.key] = False
            
        # dispaly_score()
        # print(game_active)

        if keys[pg.K_SPACE]:
        # game_active = True
            return
        clock.tick(fps) 
        pg.display.flip()
        
while True:
    GameOverScreen()
    #score / timer
    GameActive()

