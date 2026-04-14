def abc1():
    a = [2, 2, 2, 2, 2]
    hand_suits = []
    for card in a:
        hand_suits.append(card)
    return hand_suits.count(hand_suits[0]) >= 5

def abc2():
    a = [2, 2, 2, 2, 2]
    hand_suits = []
    for card in a:
        hand_suits.append(card)
    return hand_suits.count(hand_suits[0]) >= 5

def abc3():
    return abc1() and abc2()

print(abc3())