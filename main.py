import pygame
import csv
from settings import *
from sprites import *
from sprites import Board

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.difficulty = ""
        self.username = ""
    def new(self):
        self.board = Board()
        self.colour = None

    def run(self):
        self.playing = True
        self.difficulty = input("Type in your chosen difficulty (Easy or Hard): ")                    
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
            

    def draw(self):
        self.screen.fill(BGCOLOUR)
        self.board.draw(self.screen)
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                self.colour = self.board.select_colour(mx,my,self.colour)
                if self.colour is not None:
                    self.board.place_pin(mx, my, self.colour)
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.board.check_row():
                        clues_colour_list = self.board.check_clues()
                        self.board.set_clues(clues_colour_list)

                        if self.check_win(clues_colour_list):
                            print("You win")
                            self.board.reveal_code()
                            self.win_routine()
                            self.end_screen()
                        elif not self.board.next_round():
                            print("Game over, you lose")
                            self.board.reveal_code()
                            self.end_screen()

    def check_win(self, colour_list):
        if len(colour_list) != 4:
            return False
        for colour in colour_list:
            if colour != RED:
                return False
        return True
    
    def win_routine(self):
        if self.board.tries == 10:
            self.attempts = 1
        elif self.board.tries == 9:
            self.attempts = 2
        elif self.board.tries == 8:
            self.attempts = 3
        elif self.board.tries == 7:
            self.attempts = 4
        elif self.board.tries == 6:
            self.attempts = 5
        elif self.board.tries == 5:
            self.attempts = 6
        elif self.board.tries == 4:
            self.attempts = 7
        elif self.board.tries == 3:
            self.attempts = 8
        elif self.board.tries == 2:
            self.attempts = 9
        elif self.board.tries == 1:
            self.attempts = 10   
        self.attempts = int(input("How many attempts did it take you: "))
        self.username = input("Can you type in your username for the leaderboard: ")

        with open('Leaderboard.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.username, self.attempts])
    
    def end_screen(self):
        while True:
            event = pygame.event.wait()
            if event.type == pygame.quit:
                quit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.playing = False
                    return
            self.draw()

game = Game()
while True:
    game.new()
    game.run()
