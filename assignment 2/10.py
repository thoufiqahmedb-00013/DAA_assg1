def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    a_len = 0
    temp_x = x
    while temp_x != 0:
        temp_x //= 10
        a_len += 1

    b_len = 0
    temp_y = y
    while temp_y != 0:
        temp_y //= 10
        b_len += 1

    split_len = max(a_len, b_len)
    half = split_len // 2

    high1 = x // 10**half
    low1 = x % 10**half
    high2 = y // 10**half
    low2 = y % 10**half

    part1 = karatsuba(high1, high2)
    part2 = karatsuba(low1, low2)
    part3 = karatsuba(high1 + low1, high2 + low2) - part1 - part2

    return part1 * 10**(2 * half) + part3 * 10**half + part2

if __name__ == "__main__":
    print(karatsuba(13254, 87563))