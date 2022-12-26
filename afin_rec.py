import math
from Ciphers import *
def main(phrase):
    counter = 0
    cipher = NumCipher(Alphabet('rus', 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'), AfinRecScrambler(Alphabet('rus', 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя')))
    a_list = [i for i in range(1, 34) if math.gcd(i, 33) == 1]
    for a1 in a_list:
        for b1 in range(1, 33):
            for a2 in a_list:
                for b2 in range(1, 34):
                    phrase_decode = cipher.decode(phrase, a1=a1, b1=b1, a2=a2, b2=b2)
                    IC_ = count(phrase_decode)
                    if 0.05 < IC_ and IC_ < 0.06:
                        print(a1, b1, a2, b2, phrase_decode, IC_)


def count(phrase):
    chars = {}
    phrase = ''.join(c for c in phrase if c.isalpha())
    phrase = phrase.lower()
    for i in phrase:
        if i not in chars:
            chars[i] = 0
        chars[i] += 1
    up = 0
    for seq in chars.keys():
        seqq = chars[seq]
        up += seqq * (seqq - 1)
    return up / (len(phrase) * (len(phrase)- 1))


if __name__ == '__main__':
    print(main(input('Введите фразу: ')))
