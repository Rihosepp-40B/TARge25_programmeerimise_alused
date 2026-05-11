"""Functions for all modules.
Selle osa eesmärk on jagada teistele moodulitele ühiseid toiminguid.
Siin demonstreerin lugemist ja lisamist faili."""
import time


def print_sword_of_trollcraft():
    """Print game title."""
    with open("sword_of_troll_craft.txt", "r", encoding="utf-8") as f:
        print(f.read())
    time.sleep(1)


def exit_program(player):
    """Raise systemExit."""
    save_score(player)
    print_sword_of_trollcraft()
    raise SystemExit


def selection_exception():
    """Print selection exception message."""
    print("Action not in selection!!")
    print("Try again!!")
    time.sleep(0.5)


def save_score(player):
    """Add player score to file."""
    if player is not None:
        with open("game_scores.txt", "a") as f:
            f.write(f"{player.get_name()},{player.get_score()}\n")


def read_score():
    """Read games_score file and return, as öist."""
    score = []
    try:
        with open("game_scores.txt", "r") as f:
            for line in f.readlines():
                line = line.strip()
                if not line:
                    continue
                score.append(line.split(","))
        return sorted(score, key=lambda s: s[1], reverse=True)
    except FileNotFoundError:
        print("No score file found!!")


def print_top_10():
    """Print top 10 score"""
    n = 1
    for i in read_score()[:9]:
        print(f"{f"{n}.":<4}|{i[0]:^15} total damage done {i[1]:^10}")
        n += 1


if __name__ == '__main__':
    print_top_10()
