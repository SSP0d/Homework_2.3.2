from multiprocessing import cpu_count, Pool
from time import time


def factorize(*numbers) -> list[list[int]]:
    result = []

    for num in numbers:
        new_numbers = []

        operand = 1

        while operand <= num:
            if num % operand != 0:
                operand += 1
                continue
            new_numbers.append(operand)
            operand += 1

        result.append(new_numbers)

    return result


if __name__ == '__main__':

    begin = time()

    with Pool(8) as pool:
        pool.apply(factorize, (128, 255, 99999, 10651060))
        pool.close()
        pool.join()

    # a, b, c, d  = factorize(128, 255, 99999, 10651060)

    print(f'Working time: {time()-begin}')
    print(f'CPU - {cpu_count()}')

    # print(f'a = {a}')
    # print(f'b = {b}')
    # print(f'c = {c}')
    # print(f'd = {d}')

    # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    # assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    # a, b, c, d = factorize(2, 4, 8, 16)