import random

def play_round():
    S=0
    #Holmes round
    while S <= 100:
        x = random.randint(1, 100)
        S += x

    #Moriarty round
    while S <= 200:
        y = random.randint(1, 100)
        S += y

    if y > x:
        return True
    else:
        return False

N = 100000
moriarty_wins = 0

for _ in range(N):
    if play_round():
        moriarty_wins += 1

moriarty_win_odds = moriarty_wins / N

print("Moriarty wins:", moriarty_wins, f"({moriarty_win_odds:.4f})")



