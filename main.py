import pygame
import csv
from settings import *
from sprites import Board


class Game:
    def __init__(self):
        """Initialize the game."""
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = False
        self.board = None
        self.colour = None
        self.difficulty = None

    def new_game(self):
        """Start a new game."""
        self.difficulty = self.get_difficulty()
        self.board = Board(self.difficulty)
        self.colour = None
        self.playing = True

    def run_game(self):
        """Main game loop."""
        while self.playing:
            self.handle_events()
            self.update_screen()
            self.clock.tick(FPS)

    def update_screen(self):
        """Update the display."""
        self.screen.fill(BGCOLOUR)
        self.board.draw(self.screen)
        pygame.display.flip()

    def handle_events(self):
        """Handle user input."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.handle_mouse_click(event.pos)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.handle_enter_key()

    def handle_mouse_click(self, position):
        """Handle mouse click to select or place colours."""
        mx, my = position
        self.colour = self.board.select_colour(mx, my, self.colour)
        if self.colour:
            self.board.place_pin(mx, my, self.colour)

    def handle_enter_key(self):
        """Handle the Enter key for row checking."""
        if self.board.check_row():
            clues = self.board.check_clues()
            self.board.set_clues(clues)

            if self.check_win(clues):
                self.win_routine()
                self.show_end_screen("You win!")
            elif not self.board.next_round():
                self.show_end_screen("Game over, you lose.")
                self.board.reveal_code()

    def check_win(self, clues):
        """Check if the player has won."""
        return len(clues) == 4 and all(colour == RED for colour in clues)

    def win_routine(self):
        """Handle the win scenario."""
        username = self.get_username()
        attempts = self.board.get_attempts()
        with open('Leaderboard.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, attempts])

    def show_end_screen(self, message):
        """Display the end screen."""
        print(message)
        self.board.reveal_code()
        self.playing = False
        self.wait_for_keypress()

    def wait_for_keypress(self):
        """Wait for the player to press Enter to continue."""
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return

    def quit_game(self):
        """Exit the game."""
        self.running = False
        self.playing = False
        pygame.quit()
        quit()

    def get_difficulty(self):
        """Get the difficulty level from the player."""
        while True:
            difficulty = input("Choose difficulty (Easy or Hard): ").strip().lower()
            if difficulty in {"easy", "hard"}:
                return difficulty
            print("Invalid input. Please choose 'Easy' or 'Hard'.")

    @staticmethod
    def get_username():
        """Get the player's username."""
        return input("Enter your username: ").strip()

    def start(self):
        """Start the main program loop."""
        while self.running:
            self.new_game()
            self.run_game()


if __name__ == "__main__":
    game = Game()
    game.start()