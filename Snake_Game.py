import pygame
from  pygame.locals import *
import time
import random

SIZE = 40

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.apple = pygame.image.load(("Resourese/apple.jpeg")).convert()
        self.apple = pygame.transform.scale(self.apple, (40, 40))
        self.x = SIZE*3
        self.y = SIZE*3

    def draw(self):

        self.parent_screen.blit(self.apple, (self.x,self.y))
        pygame.display.flip()


    def move(self):
        self.x =  random.randint(0, 19) * SIZE
        self.y = random.randint(0,19)* SIZE



class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load(("Resourese/block_img.png")).convert()
        self.block = pygame.transform.scale(self.block,(40, 40))
        self.x = [SIZE] * length
        self.y = [SIZE] * length

        self.direction = "right"

    def draw(self):
        self.parent_screen.fill((255, 25, 40))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()


    def increase_size(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)



    def move_up(self):
        self.direction = 'up'
    def move_down(self):
        self.direction = "down"

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def walk(self):

        for i in range(self.length -1, 0 ,-1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == "left":
            self.x[0] -= SIZE

        if self.direction == "right":
            self.x[0] += SIZE

        if self.direction == "up":
            self.y[0] -= SIZE

        if self.direction == "down":
            self.y[0] += SIZE

        self.draw()
class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((800, 800))
        self.surface.fill((255, 25, 40))
        self.Snake = Snake(self.surface,1)
        self.Snake.draw()
        self.Apple = Apple(self.surface)
        self.Apple.draw()

    def collision(self,x1, y1, x2, y2):

        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2  and y1 < y2 + SIZE:
                return True

        return  False

    def play(self):
        self.Snake.walk()
        self.Apple.draw()
        self.display_score()
        pygame.display.flip()

        if game.collision(self.Snake.x[0], self.Snake.y[0], self.Apple.x, self.Apple.y):

            self.Apple.move()
            self.Snake.increase_size()


    def display_score(self):
        font = pygame.font.SysFont("arial", 40)
        score = font.render(f"Score {self.Snake.length}", True , (255, 255, 255) )
        self.surface.blit(score, (600, 10))




    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.Snake.move_up()

                    if event.key == K_DOWN:
                        self.Snake.move_down()

                    if event.key == K_LEFT:
                        self.Snake.move_left()

                    if event.key == K_RIGHT:
                        self.Snake.move_right()

                elif event.type == QUIT:
                    running = False


            self.play()
            time.sleep(0.3)



if __name__ == "__main__":
    game = Game()
    game.run()


