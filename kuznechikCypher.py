from sympy import symbols, Poly

counter = 0


def read_word_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()


word_file_path = 'req_88e2b8c5-47cc-4e82-996a-ea7ec4a20d04.xml'
word_binary_data = read_word_file(word_file_path)
file_string = ''.join(format(byte, '08b') for byte in word_binary_data)
file_path = 'engineFile.txt'
with open(file_path, 'a') as file1:
    file1.write(file_string)
if len(file_string) % 128 != 0:
    while len(file_string) % 128 != 0:
        file_string += '0'
        counter += 1
print(counter)

x = symbols('x')
nonlinearBinaryConversionArr = [252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35, 197, 4, 77, 233, 119, 240,
                                219, 147, 46,
                                153, 186, 23, 54, 241, 187, 20, 205, 95, 193, 249, 24, 101, 90, 226, 92, 239, 33, 129,
                                28,
                                60, 66,
                                139, 1, 142, 79, 5, 132, 2, 174, 227, 106, 143, 160, 6, 11, 237, 152, 127, 212, 211, 31,
                                235, 52, 44,
                                81, 234, 200, 72, 171, 242, 42, 104, 162, 253, 58, 206, 204, 181, 112, 14, 86, 8, 12,
                                118,
                                18, 191,
                                114, 19, 71, 156, 183, 93, 135, 21, 161, 150, 41, 16, 123, 154, 199, 243, 145, 120, 111,
                                157, 158,
                                178, 177, 50, 117, 25, 61, 255, 53, 138, 126, 109, 84, 198, 128, 195, 189, 13, 87, 223,
                                245, 36, 169,
                                62, 168, 67, 201, 215, 121, 214, 246, 124, 34, 185, 3, 224, 15, 236, 222, 122, 148, 176,
                                188, 220,
                                232, 40, 80, 78, 51, 10, 74, 167, 151, 96, 115, 30, 0, 98, 68, 26, 184, 56, 130, 100,
                                159,
                                38, 65,
                                173, 69, 70, 146, 39, 94, 85, 47, 140, 163, 165, 125, 105, 213, 149, 59, 7, 88, 179, 64,
                                134, 172, 29,
                                247, 48, 55, 107, 228, 136, 217, 231, 137, 225, 27, 131, 73, 76, 63, 248, 254, 141, 83,
                                170, 144, 202,
                                216, 133, 97, 32, 113, 103, 164, 45, 43, 9, 91, 203, 155, 37, 208, 190, 229, 108, 82,
                                89,
                                166, 116,
                                210, 230, 244, 180, 192, 209, 102, 175, 194, 57, 75, 99, 182]
reverseNonlinearCoef = [165, 45, 50, 143, 14, 48, 56, 192, 84, 230, 158, 57, 85, 126, 82, 145, 100, 3, 87, 90, 28, 96,
                        7, 24, 33, 114, 168, 209, 41, 198, 164, 63, 224, 39, 141, 12, 130, 234, 174, 180, 154, 99, 73,
                        229, 66, 228, 21, 183, 200, 6, 112, 157, 65, 117, 25, 201, 170, 252, 77, 191, 42, 115, 132,
                        213, 195, 175, 43, 134, 167, 177, 178, 91, 70, 211, 159, 253, 212, 15, 156, 47, 155, 67, 239,
                        217, 121, 182, 83, 127, 193, 240, 35, 231, 37, 94, 181, 30, 162, 223, 166, 254, 172, 34, 249,
                        226, 74, 188, 53, 202, 238, 120, 5, 107, 81, 225, 89, 163, 242, 113, 86, 17, 106, 137, 148,
                        101, 140, 187, 119, 60, 123, 40, 171, 210, 49, 222, 196, 95, 204, 207, 118, 44, 184, 216, 46,
                        54, 219, 105, 179, 20, 149, 190, 98, 161, 59, 22, 102, 233, 92, 108, 109, 173, 55, 97, 75,
                        185, 227, 186, 241, 160, 133, 131, 218, 71, 197, 176, 51, 250, 150, 111, 110, 194, 246, 80,
                        255, 93, 169, 142, 23, 27, 151, 125, 236, 88, 247, 31, 251, 124, 9, 13, 122, 103, 69, 135,
                        220, 232, 79, 29, 78, 4, 235, 248, 243, 62, 61, 189, 138, 136, 221, 205, 11, 19, 152, 2, 147,
                        128, 144, 208, 36, 52, 203, 237, 244, 206, 153, 16, 68, 64, 146, 58, 1, 38, 18, 26, 72, 104,
                        245, 129, 139, 199, 214, 32, 10, 8, 0, 76, 215, 116]
linealCoef = [148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148, 1]
prime_polynome = [1, 1, 1, 0, 0, 0, 0, 1, 1]


def nonLinearBinaryConversion(byte, coefficients):  # работает правильно
    number = int(byte, 2)
    numberTemp = coefficients[number]
    binaryString = bin(numberTemp)[2:].zfill(8)
    return binaryString


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


def roundKeyOverlay(roundKey, blockOpenText):
    resultText = ''
    for i in range(len(blockOpenText)):
        if (int(blockOpenText[i]) + int(roundKey[i])) % 2 == 0:
            tempNumber = '0'
        else:
            tempNumber = '1'
        resultText += tempNumber
    return resultText


def changeByteInBlock(openBlock, binaryConversionArr):
    temp = [openBlock[i:i + 8] for i in range(0, len(openBlock), 8)]
    resultSi = ''
    for i in range(len(temp)):
        resultSi += nonLinearBinaryConversion(temp[i], binaryConversionArr)
    return resultSi


def dataBlockShuffle(opnBlck, count=0):
    if count == 16:
        return opnBlck

    resultSi = linearConversion(opnBlck)
    temp = [opnBlck[i:i + 8] for i in range(0, len(opnBlck), 8)]
    for i in range(len(temp) - 1):
        resultSi += temp[i]

    count += 1
    return dataBlockShuffle(resultSi, count)


def dataBlockShuffleForDecrypt(opnBlck, cnt=0):
    if cnt == 16:
        return opnBlck
    resultSiDecrypt = ''
    temp = [opnBlck[i:i + 8] for i in range(0, len(opnBlck), 8)]
    for i in range(1, len(temp)):
        resultSiDecrypt += temp[i]
    resultSiDecrypt += linearConversion(resultSiDecrypt + temp[0])
    cnt += 1
    return dataBlockShuffleForDecrypt(resultSiDecrypt, cnt)


filename = 'cypherText.txt'


def splitIntoBlocks(string):
    return [string[i:i + 128] for i in range(0, len(string), 128)]


roundKey = input('Введите раундовый ключ (двоичный ключ длиной 256 бит): ')


def formRoundKey(roundKey):
    rndKey1, rndKey2 = '', ''
    roundKeyArr = []
    for i in range(len(roundKey) // 2):
        rndKey1 += roundKey[128 + i]
        rndKey2 += roundKey[i]
    roundKeyArr.insert(0, rndKey1)
    roundKeyArr.insert(0, rndKey2)
    for _ in range(8):
        temp = rndKey2
        stage1 = roundKeyOverlay(rndKey1, rndKey2)
        stage2 = changeByteInBlock(stage1, nonlinearBinaryConversionArr)
        stage3 = dataBlockShuffle(stage2, count=0)
        roundKeyArr.append(stage3)
        rndKey1 = temp
        rndKey2 = stage3

    return roundKeyArr


def encpryptCypherKuznechik(text, roundKeyArr):
    print('Открытый текст: ', hex(int(text, 2))[2:])
    summaryString = ''
    blockTextArr = splitIntoBlocks(text)
    print(len(blockTextArr))
    for index in range(len(blockTextArr)):
        for i in range(len(roundKeyArr) - 1):
            workingBlockKey = roundKeyArr[len(roundKeyArr) - i - 1]
            blockTextArr[index] = roundKeyOverlay(workingBlockKey, blockTextArr[index])
            blockTextArr[index] = changeByteInBlock(blockTextArr[index], nonlinearBinaryConversionArr)
            blockTextArr[index] = dataBlockShuffle(blockTextArr[index], count=0)
        blockTextArr[index] = roundKeyOverlay(roundKeyArr[0], blockTextArr[index])
        summaryString += blockTextArr[index]
    with open(filename, 'a') as file1:
        file1.write(summaryString)
    return summaryString


b = encpryptCypherKuznechik(file_string, formRoundKey(roundKey))

filename1 = 'newEngineText.txt'


def decpryptCypherKuznechik(text, roundKeyArr):
    print('Зашифрованный текст: ', hex(int(text, 2))[2:])
    addResItog = ''
    blockTextArr = splitIntoBlocks(text)
    for index in range(len(blockTextArr)):
        blockTextArr[index] = roundKeyOverlay(roundKeyArr[0], blockTextArr[index])
        for i in range(1, len(roundKeyArr)):
            blockTextArr[index] = dataBlockShuffleForDecrypt(blockTextArr[index], cnt=0)
            blockTextArr[index] = changeByteInBlock(blockTextArr[index], reverseNonlinearCoef)
            blockTextArr[index] = roundKeyOverlay(roundKeyArr[i], blockTextArr[index])
        addResItog += blockTextArr[index]
    print('Расшифрованный текст: ', hex(int(addResItog, 2))[2:])
    with open(filename1, 'a') as file2:
        file2.write(addResItog[:-counter])
    return addResItog


z = decpryptCypherKuznechik(b, formRoundKey(roundKey))
if file_string == z:
    print('congratulations!')
