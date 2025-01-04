import pygame
import random
from settings import *
from sprites import *
from sprites import Board

file = open("Leaderboard.txt","a")

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    def new(self):
        self.board = Board()
        self.colour = None

    def run(self):
        self.playing = True
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
        win_routine(self)

    def win_routine(self):
        file = open("Leaderboard.txt","a")
        print(f"Well done it took you {11-tries} attmepts to clear this code.")
        name = input("Can you type in your username for the leaderboard: ")
        file.write(f"{name}: {tries}\n")
        file.close()
    
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
    print(f"The available game modes are {DIFFICULTY_SETTINGS[0]}, {DIFFICULTY_SETTINGS[1]} or {DIFFICULTY_SETTINGS[2]}.")
    gamemode = input("Type in the chosen difficulty from the choices above: ")
    game.new()
    game.run()
