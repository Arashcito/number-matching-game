# COMP348 ASSIGNMENT 2
# AUTHOR : ARASH SHAFIEE

import os
import sys
import time
from grid import Grid

# clearing screen whenever its called
def clear_screen():
    os.system('clear')


# displaying menu whenever its called
def display_menu():

    print("\nMenu Options:")
    print("1. Guess a pair")
    print("2. Reveal a cell")
    print("3. I give up - reveal the grid")
    print("4. Start new game")
    print("5. Exit")
    print()


def get_valid_coordinate(prompt: str, grid: Grid) -> str:

    while True:
        coord = input(prompt).strip()
        try:
            grid.get_cell(coord)
            return coord
        except ValueError as e:
            print(f"Error: {e}")


def main():
    # Validating command line argument
    if len(sys.argv) != 2 or sys.argv[1] not in ['2', '4', '6']:
        print("Usage: python3 game.py [2|4|6]")
        sys.exit(1)

    grid_size = int(sys.argv[1])
    grid = Grid(grid_size)

    while True:
        clear_screen()
        print("\nMemory Game")
        print(grid)
        display_menu()

        # getting prompt from user
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice not in range(1, 6):
                raise ValueError
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 5.")
            time.sleep(2)
            continue

        # Guess a pair
        if choice == 1:
            coord1 = get_valid_coordinate("Enter first cell (e.g., A0): ", grid)
            coord2 = get_valid_coordinate("Enter second cell (e.g., B0): ", grid)

            cell1 = grid.get_cell(coord1)
            cell2 = grid.get_cell(coord2)

            if cell1 is cell2:
                print("Error: Cannot select the same cell twice!")
                time.sleep(2)
                continue

            if cell1.is_revealed or cell2.is_revealed:
                print("Error: One or both cells are already revealed!")
                time.sleep(2)
                continue

            # Reveal both cells temporarily
            cell1.is_revealed = True
            cell2.is_revealed = True
            grid.guesses += 1

            clear_screen()
            print("\nMemory Game")
            print(grid)

            if cell1.value == cell2.value:
                print("Match found!")
                if grid.is_game_won():
                    score = grid.calculate_score()
                    print(f"\nCongratulations! You've won!")
                    print(f"Final Score: {score:.1f}")
                    input("\nPress Enter to start a new game...")
                    grid.initialize_grid()
            else:
                print("No match!")
                time.sleep(2)
                cell1.is_revealed = False
                cell2.is_revealed = False

        # Reveal a cell
        elif choice == 2:
            coord = get_valid_coordinate("Enter cell to reveal (e.g., A0): ", grid)
            cell = grid.get_cell(coord)
            if not cell.is_revealed:
                cell.is_revealed = True
                grid.guesses += 2

        # Give up
        elif choice == 3:
            clear_screen()
            print("\nMemory Game")
            grid.reveal_all()
            print(grid)
            print("\nGrid revealed! Game Over!")
            input("\nPress Enter to start a new game...")
            grid.initialize_grid()

        # New game
        elif choice == 4:
            grid.initialize_grid()

        # Exit
        elif choice == 5:
            print("\nThanks for playing!")
            sys.exit(0)


if __name__ == "__main__":
    main()