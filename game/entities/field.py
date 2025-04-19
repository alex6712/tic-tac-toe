from typing import List

from game.entities import Square


class Field:
    def __init__(self, rows: int, columns: int) -> None:
        self._rows: int = rows
        self._columns: int = columns

        self._field: List[List[Square]] = list()
        self._init_field()

    def _init_field(self) -> None:
        self._field.clear()

        for i in range(self._rows):
            row: List[Square] = list()

            for j in range(self._columns):
                row.append(Square())

            self._field.append(row)

    def get_square(self, x: int, y: int):
        return self._field[x][y]
