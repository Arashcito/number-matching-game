# COMP348 ASSIGNMENT 2
# AUTHOR : ARASH SHAFIEE

import random
from typing import List


class Cell:
    def __init__(self, value: int):
        self.value = value
        self.is_revealed = False

    def __str__(self) -> str:
        return str(self.value) if self.is_revealed else 'X'


class Grid:
    def __init__(self, size: int):
        if size not in [2, 4, 6]:
            raise ValueError("Grid size must be 2, 4, or 6")

        self.size = size
        self.cells: List[Cell] = []
        self.guesses = 0
        self.initialize_grid()

    # Create pairs of numbers
    def initialize_grid(self) -> None:


        pairs = self.size * self.size // 2
        numbers = list(range(pairs)) * 2
        random.shuffle(numbers)

        self.cells = [Cell(num) for num in numbers]
        self.guesses = 0

    def get_cell(self, coord: str) -> Cell:
        if not coord or len(coord) < 2:
            raise ValueError("Invalid coordinate format")

        col = coord[0].upper()
        try:
            row = int(coord[1:])
        except ValueError:
            raise ValueError("Invalid row number")

        if not ('A' <= col <= chr(ord('A') + self.size - 1)):
            raise ValueError("Invalid column letter")
        if not (0 <= row < self.size):
            raise ValueError("Invalid row number")

        index = (ord(col) - ord('A')) + (row * self.size)
        return self.cells[index]

    # reveling all cells
    def reveal_all(self) -> None:
        for cell in self.cells:
            cell.is_revealed = True

    def hide_all(self) -> None:
        for cell in self.cells:
            cell.is_revealed = False

    def is_game_won(self) -> bool:
        return all(cell.is_revealed for cell in self.cells)

    def calculate_score(self) -> float:
        if self.guesses == 0:
            return 0.0
        min_guesses = (self.size * self.size) // 2
        return (min_guesses / self.guesses) * 100

    #Return string representation of grid
    def __str__(self) -> str:

        # Column headers
        result = "   " + " ".join(chr(ord('A') + i) for i in range(self.size)) + "\n"

        # Grid content
        for row in range(self.size):
            result += f"{row}  "
            for col in range(self.size):
                cell = self.cells[col + row * self.size]
                result += str(cell) + " "
            result += "\n"

        return result