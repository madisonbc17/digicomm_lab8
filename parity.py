#using the brute force section of
#http://p-nand-q.com/python/algorithms/math/bit-parity.html
def odd_parity(x):
    bit = 0
    num_bits = 0
    while x:
        bitmask = 1 << bit
        bit += 1
        if x & bitmask:
            num_bits += 1
        x &= ~bitmask
    return num_bits % 1

def even_parity(x):
    bit = 0
    num_bits = 0
    while x:
        bitmask = 1 << bit
        bit += 1
        if x & bitmask:
            num_bits += 1
        x &= ~bitmask
    return num_bits % 2

result_even = even_parity(0x0010)
result_odd = odd_parity(0x0010)

print(result_even)
print(result_odd)