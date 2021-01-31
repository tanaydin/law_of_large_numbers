import random


def main():
    for number_of_zeroes in range(1, 9):
        total = 0
        num_of_rolls = 10 ** number_of_zeroes
        for _ in range(1, num_of_rolls):
            total += random.randint(1, 6)

        average = total / num_of_rolls
        print(f'{number_of_zeroes}\t{average}')


if __name__ == '__main__':
    main()
