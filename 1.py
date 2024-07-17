import random
from sympy import symbols, Poly

linealCoef = [148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148, 1]
prime_polynome = [1, 1, 1, 0, 0, 0, 0, 1, 1]
x = symbols('x')
random_string = ''.join(random.choice(['0', '1']) for _ in range(512))
print(random_string)


def linearConversion(sixteenBytes):  # скорее всего работает)
    summa = []
    result = ''
    temp = [sixteenBytes[i:i + 8] for i in range(0, len(sixteenBytes), 8)]
    for i in range(len(temp)):
        tempArr = [int(char) for char in temp[i]]
        linealCoefBin = bin(linealCoef[i])[2:].zfill(8)
        linealCoefArr = [int(char) for char in linealCoefBin]
        summa.append((Poly(tempArr, x) * Poly(linealCoefArr, x)) % Poly(prime_polynome, x))

    resultPolynomial = sum(summa).all_coeffs()
    for i in range(len(resultPolynomial)):
        resultPolynomial[i] %= 2
    while len(resultPolynomial) != 8:
        resultPolynomial = [0] + resultPolynomial
    for i in range(len(resultPolynomial)):
        result += str(resultPolynomial[i])
    return result


def dataBlockShuffle1(message):
    result = ''
    for blockStart in range(0, len(message), 64):
        block = message[blockStart:blockStart + 64]
        resultSi = linearConversion(block)
        temp = [block[i:i + 8] for i in range(0, len(block), 8)]
        for i in range(len(temp) - 1):
            resultSi += temp[i]
        result += resultSi
    return result


def dataBlockShuffle(opnBlck, count=0):
    if count == 16:
        return opnBlck

    resultSi = linearConversion(opnBlck)
    temp = [opnBlck[i:i + 8] for i in range(0, len(opnBlck), 8)]
    for i in range(len(temp) - 1):
        resultSi += temp[i]

    count += 1
    return dataBlockShuffle(resultSi, count)


print(dataBlockShuffle(random_string))
print(dataBlockShuffle1(random_string))
