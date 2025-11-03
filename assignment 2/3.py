import random
def PrintBinary(n):
    if n == 0:
        return 0
    binary = 0
    place = 1  
    while n > 0:
        bit = n % 2
        binary += bit * place
        place *= 10
        n = n // 2
    return binary

def random_bit(n):
    binary = PrintBinary(n)
    binary_str = str(binary)
    
    r_pos = random.randint(0, len(binary_str) - 1)
    bit = int(binary_str[-(r_pos + 1)])

    print(f"Integer: {n}")
    print(f"Binary: {binary}")
    print(f"Random Position (from right): {r_pos}")
    print(f"Bit at Position: {bit}")
    print(f"Result: {bit == 1}")
    return bit

print(random_bit(13))