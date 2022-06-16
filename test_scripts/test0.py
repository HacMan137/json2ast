import random
from datetime import date

def randomDate():
    day = random.randrange(1, 28)
    month = random.randrange(1, 12)
    year = random.randrange(1900, 2022)

    return date(month=month, day=day, year=year)

if __name__ == "__main__":
    x = input("Enter Q to quit.")
    while(len(x) < 1 or (x[0] != 'Q' and x[0] != 'q')):
        print(randomDate())
        x = input(">")