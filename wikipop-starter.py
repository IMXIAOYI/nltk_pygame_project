"""
 Sample code for SI 507 Waiver Assignment
 University of Michigan School of Information

 Based on "Pygame base template for opening a window" 
     Sample Python/Pygame Programs
     Simpson College Computer Science
     http://programarcadegames.com/
     http://simpson.edu/computer-science/
 
See README for the assignment for instructions to complete and submit this.
"""
 
import pygame
import random
import test

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# You must construct a dictionary of this form from your wikipedia search
# See test.py for more details on the format requirements for the dictionary
sample_pos_dict = {"JJ": [("happy", 5), ("sad", 4)], "NN": [("ball", 3), ("bat", 2)]}

# You must leave this line in your submission, and you must pass the test!
if test.test(sample_pos_diction):
    print ("You passed this sample_pos_diction part of the test!")
else:
    print ("You didn't pass. Please try again")

# This is the temp word list for testing.
# You will need to **replace this** with words extracted from your wikipedia search.
# See README for more details.
word_list = ["apple", "banana", "pear", "grape", "pineapple", "kiwi"]

# The class that manages the balls shown on the screen in the game.
class BallManager:

    INIT_SPEED = 1
    current_index = 0

    def __init__(self):
        self.max_balls = 3
        self.active_balls = []
        for w in word_list: 
            self.active_balls.append(WordBall(w, self.INIT_SPEED))


    def create_ball(self, word):
        self.active_balls += WordBall(word, self.INIT_SPEED)
    
    def num_balls(self):
        return len(self.active_balls)

    def __str__(self):
        s = ''
        for b in self.active_balls:
            s += b.word + ", "
        return s

# The class for each ball showing on the screen.
# You can play around with size, color, font, etc. 
class WordBall:

    def __init__(self, word, speed):
        self.word = word
        self.x_pos = random.randint(0, pygame.display.Info().current_w)
        self.y_pos = 0
        self.height = 100
        self.width = 100
        self.speed = speed

    def move_ball(self):
        self.y_pos += self.speed
        if (self.y_pos > pygame.display.Info().current_h - self.height):
            self.y_pos = 0

# Initialize game
pygame.init()

size = (1000, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Type to Win")
clock = pygame.time.Clock()
 
# Loop until the user clicks the close button...

ball_manager = BallManager()
ball_font = pygame.font.Font(None, 36)
keys_font = pygame.font.Font(None, 60)
done = False
game_over = False
keys_typed = ''

# Main display loop
while not done:
    
    # Handle input events.
    key = ''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            key = event.unicode
            keys_typed += key


    # Manipulate game objects.
    for b in ball_manager.active_balls:
        b.move_ball()


    # Blank the screen
    screen.fill(WHITE)

    # Render game objects
    for ball in ball_manager.active_balls:
        pygame.draw.ellipse(screen, RED, [ball.x_pos, ball.y_pos, ball.width, ball.height]) 
        text = ball_font.render(ball.word, 1, BLACK)
        textpos = text.get_rect()
        textpos.centerx = ball.x_pos + ball.width / 2
        textpos.centery = ball.y_pos + ball.height / 2
        screen.blit(text, textpos)

 
    text = keys_font.render('keys typed: ' + keys_typed, 1, GREEN)
    textpos = text.get_rect()
    textpos.centerx = pygame.display.Info().current_w / 2
    textpos.centery = pygame.display.Info().current_h - 30
    screen.blit(text, textpos)


    # Update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()   
