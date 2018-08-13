def toBinary(num):
    return bin(int(num))[2:]
def toTernary(num):
    num = int(num)
    ret = ""
    while num > 0:
        ret += str(num%3)
        num //= 3
    return ret[::-1]
