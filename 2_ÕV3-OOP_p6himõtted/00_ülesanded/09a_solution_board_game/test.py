game_sessions = ["b", "a", "b", "a", "a", "b"]

class Test:
    def __init__(self):
        self.players: list[Player] = []


class Player:
    """Player class."""

    def __init__(self, name: str):
        """Initialze player."""
        self.name = name

    def get_name(self):
        """Return name of player."""
        return self.name

    def __repr__(self) -> str:
        """
        Person representation.

        :return: person's full name
        """
        return self.name

if __name__ == '__main__':
    test = Test("tiit")

    print(str(test))
