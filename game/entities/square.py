from game.entities import Mark


class Square:
    def __init__(self) -> None:
        self._content: Mark = Mark.EMPTY

    def is_empty(self) -> bool:
        return self._content is Mark.EMPTY

    def get_mark(self) -> Mark:
        return self._content

    def place_mark(self, mark: Mark) -> None:
        if mark not in Mark:
            raise Exception("not a valid mark")

        self._content = mark

    def clear(self) -> None:
        self._content = Mark.EMPTY
