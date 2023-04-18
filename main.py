from poker import Rank, Card


if __name__ == "__main__":
    print('Möchtest du eine Randomkarte?')
    x = input()
    print(Card.make_random())
