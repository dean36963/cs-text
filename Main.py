from RoundController import RoundController
from random import randint


def main():
    print("Welcome to text-only Counterstrike.")
    player_is_terrorist = randint(0,1)
    rc = RoundController(player_is_terrorist)
    rc.loop(3)
    input("Press enter to quit.")

if __name__ == '__main__':
    main()
