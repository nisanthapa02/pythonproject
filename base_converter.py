# import time, sys
binary = '1101001110'
binary32 = '11000111011001100111001000110011'

def ipv4ToDotted(binary32):
    for i in range(0, len(binary32), 8): # i = 0, 8, 16, 32
        print(reverseConv(binary32[i:i+8]), end='.')

def reverseConv(binary):
    index = 0
    ans = 0
    # from end char to start char
    for dig in binary[::-1]:
        # if int(dig):
        # 1*2^0 + 0*2^1 + ....
        ans += int(dig) * (2 ** index)
        index += 1

    return ans

def normalConv(binary):
    index = len(binary) - 1
    ans = 0
    for dig in binary:
        ans += int(dig) * (2 ** index)
        index -= 1

    return ans

def positiveDecToBinary(dec):
    dec = int(dec)
    ansBin = ''
    # int(dec) cuz we dont take decimals
    while dec != 0:
        # does dec % 2 also do dec / 2? is this redundant?
        # remainder is taken at first cuz at any particular step it depends on the dividend not the quotient
        if dec % 2 == 0:    # if even, then remainder=0
            ansBin += '0'
        else:               # if odd, then remainder=1
            ansBin += '1'
        dec = int(dec / 2)
    # to change all to 8 bits
    while len(ansBin) < 8:
        ansBin += '0'

    # from down to up or from end to start
    return ansBin[::-1]

def negativeDecToBinary(negDec):
    # can we not have to convert the same number, two different times?
    # flipping digits is easy but performing binary addition is hard
    # since 1's and 2's complement only differ by 1
    # for eg: to convert -4 to 2's complement, we compute -3
    #    i.e. -4's 2complement == -3's 1complement
    # so we just substract 1
    negDec = abs(negDec) - 1
    ansDec = ''
    # first convert dec to binary normally (+ve numbers)
    minusDec = positiveDecToBinary(negDec)
    for digit in minusDec:
        # if 0 then add '1' which is same as flipping
        if digit == '0':
            ansDec += '1'
        # if 1 then add '0' which is same as flipping
        else:
            ansDec += '0'
    return ansDec

"""
def onesComplement():
    print('Ones ')

    for i in range(-100, 30):
        if i < 0:
            print(f'{negativeDecToBinary(i + 1)}  {i}')
        else:
            print(f'{positiveDecToBinary(i)}  {i}')

    # OR we could just use for loop for +ve and -ve decimal numbers. optimization? IDTS..

    # for i in range(-8, 1):
    #     print(f'{negativeDecToBinary(i)}  {i}')
    # for i in range(0, 8):
    #     print(f'{positiveDecToBinary(i)}  {i}')

    return '=========='
"""

def twosComplement():
    print('Twos ')
    for i in range(-130, 130):
        if i < 0:
            notPos = negativeDecToBinary(i)
            print(f'{notPos[0:4]} {notPos[4:9]}  {i}')
        else:
            notNeg = positiveDecToBinary(i)
            print(f'{notNeg[0:4]} {notNeg[4:9]}  {i}')

    return '========'

print(negativeDecToBinary(-9910))
# print(f'{-9910:b}')
print(positiveDecToBinary(12110))
# print(f'{2200:b}')

print(twosComplement())

# print(reverseConv('100100010010111'))
# print(normalConv('100010010111'))

# ipv4ToDotted(binary32)
