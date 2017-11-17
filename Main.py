from RoundController import RoundController


def main():
    print("Welcome to text-only Counterstrike.")
    rc = RoundController()
    rc.start()
    rc.loop(1)

if __name__ == '__main__':
    main()