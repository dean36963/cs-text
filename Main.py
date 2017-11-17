from RoundController import RoundController


def main():
    print("Welcome to text-only Counterstrike.")
    rc = RoundController()
    rc.loop(3)

if __name__ == '__main__':
    main()