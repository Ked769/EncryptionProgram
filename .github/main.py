##############################
import math
primes = [2, 3, 5, 7, 11, 13, 17, 19]
##############################


def encode(msg):
    print("\n", "*" * 200, sep="")
    zeros = 1
    fa = []
    for i in msg:
        binary = bin(ord(i))[2:].zfill(8)
        print("Original Binary\t:", binary)
        shift = binary[4:] + binary[:4]
        c = 0
        for j in shift:
            j = int(j)
            if not bool(j):
                zeros = zeros * primes[c]
            c += 1
        fa.append(zeros)
        zeros = 1
    return fa


def fact(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors


def ascii(lst):
    x = "0b"
    for i in lst:
        x += str(i)
    return chr(int(x, 2))


def decode(fa):
    fins = []
    for i in range(len(fa)):
        facts = fact(fa[i])
        temp = []
        for k in primes:
            if k in facts:
                temp.append(0)
            else:
                temp.append(1)
        temp = temp[4:] + temp[:4]
        fins.append(ascii(temp))
    return fins


def main():
    sp = "*" * 200
    if bool(int(input("1 to encode, 0 to decode\t: "))):
        x = encode(input("Enter Encode Statement\t: "))
        print(sp, "\nENCODED\t:", x, "\n", sp, sep="")
        print("\n", sp, "\nDECODED \t:", ''.join(decode(x)), "\n", sp, sep="")
    else:
        inp = input("Enter Decode Statement\t: ")
        inp = [int(i) for i in inp[1:len(inp)-1].split(",")]
        print("\n", sp, "\nDECODED \t:", ''.join(decode(inp)), "\n", sp, sep="")


if __name__ == "__main__":
    main()
