"""English conversion from number to string"""
import sys

__version__ = '1.0.1'


def shortscale(num: int) -> str:
    words = []

    if num < 0:
        words.append('minus')
        num = -num

    if num <= 20:
        words.append(numwords[num])  # 0 - 20
    elif num >= 1000 ** 11:
        words.append('(big number)')
    else:
        for (n, exponent) in powers_of_1000(num):
            scale_words(n, exponent, words)

    return ' '.join(words)


def powers_of_1000(n: int):
    """
    Return list of (n, exponent) for each power of 1000.
    List is ordered highest exponent first.
    n = 0 - 999.
    exponent = 0,1,2,3...
    """
    p_list = []
    exponent = 0
    while n > 0:
        p_list.insert(0, (n % 1000, exponent))
        n = n // 1000
        exponent += 1

    return p_list


def scale_words(n: int, exponent: int, words):
    """
    Append numwords for (n, exponent).
    Highest exponent first, n = 0 - 999.
    """
    if n == 0:
        return

    if hundreds := n // 100:
        words.append(numwords[hundreds])
        words.append(numwords[100])

    if tens_and_units := n % 100:

        if hundreds or (exponent == 0 and len(words)):
            words.append('and')

        if tens_and_units < 20:
            words.append(numwords[tens_and_units])

        else:
            if tens := tens_and_units // 10:
                words.append(numwords[tens * 10])

            if units := tens_and_units % 10:
                words.append(numwords[units])

    if exponent:
        words.append(numwords[1000 ** exponent])


numwords = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand',
    1000_000: 'million',  # 1000 ** 2
    1000_000_000: 'billion',  # 1000 ** 3
    1000_000_000_000: 'trillion',  # 1000 ** 4
    1000_000_000_000_000: 'quadrillion',  # 1000 ** 5
    1000_000_000_000_000_000: 'quintillion',  # 1000 ** 6
    1000_000_000_000_000_000_000: 'sextillion',  # 1000 ** 7
    1000_000_000_000_000_000_000_000: 'septillion',  # 1000 ** 8
    1000_000_000_000_000_000_000_000_000: 'octillion',  # 1000 ** 9
    1000_000_000_000_000_000_000_000_000_000: 'nonillion'  # 1000 ** 10
}


def main():
    if len(sys.argv) < 2:
        print('usage: shortscale num')
        sys.exit(1)
    try:
        num = int(sys.argv[1], 0)
        print(f'{num:,} => {shortscale(num)}')
        sys.exit(0)
    except Exception as err:
        print(f'Oops! {err}')
        sys.exit(2)


if __name__ == '__main__':
    main()
