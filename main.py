import string
import math
from Ciphers import *




def main():
    is_encode = True if input('Что сделать с текстом, encode/decode?') == 'encode' else False
    langs = {'rus': 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 'eng': string.ascii_lowercase}
    cipher_type = input('Введите шифр(simple, afin, afinrec): ')
    lang = input('Введите название алфавита(rus/eng для стандартного набора, любой другой для кастомизированного)')
    if lang not in langs:
        langs[lang] = input('Введите алфавит, состоящий из уникальных символов: ')
    alphabet = Alphabet(lang, langs[lang])
    file_name = input('Введите название файла: ')
    with open(f'{file_name}.txt', 'r', encoding='utf-8') as file:
        phrase = file.read()
    if is_encode:
        
        if cipher_type == 'simple':
            cipher = NumCipher(alphabet=alphabet, scrambler=SimpleScrambler(alphabet=alphabet))
            kwargs = {'phrase': phrase, 'sub_alphabet': input('Введите алфавит для подстановки: ')}
        elif cipher_type == 'afin':
            cipher = NumCipher(alphabet=alphabet, scrambler=AfinScrambler(alphabet=alphabet))
            key_inp = list(map(int, input('Введите a и b: ').split()))
            kwargs = {'phrase': phrase, 'a': key_inp[0], 'b': key_inp[1]}
        elif cipher_type == 'afinrec':
            cipher = NumCipher(alphabet=alphabet, scrambler=AfinRecScrambler(alphabet=alphabet))
            key_inp = list(map(int, input('Введите a1, b1, a2, b2: ').split()))
            kwargs = {'phrase': phrase, 'a1': key_inp[0], 'b1': key_inp[1], 'a2': key_inp[2], 'b2': key_inp[3]}
        with open(f'{file_name}_encoded.txt', 'w', encoding='utf-8') as file:
            print(cipher.encode(**kwargs), file=file)

    else:
        if cipher_type == 'simple':
            cipher = NumCipher(alphabet=alphabet, scrambler=SimpleScrambler(alphabet=alphabet))
            kwargs = {'phrase': phrase, 'sub_alphabet': input('Введите алфавит для подстановки: ')}
        elif cipher_type == 'afin':
            cipher = NumCipher(alphabet=alphabet, scrambler=AfinScrambler(alphabet=alphabet))
            key_inp = list(map(int, input('Введите a и b: ').split()))
            kwargs = {'phrase': phrase, 'a': key_inp[0], 'b': key_inp[1]}
        elif cipher_type == 'afinrec':
            cipher = NumCipher(alphabet=alphabet, scrambler=AfinRecScrambler(alphabet=alphabet))
            key_inp = list(map(int, input('Введите a1, b1, a2, b2: ').split()))
            kwargs = {'phrase': phrase, 'a1': key_inp[0], 'b1': key_inp[1], 'a2': key_inp[2], 'b2': key_inp[3]}
        with open(f'{file_name}_decoded.txt', 'w', encoding='utf-8') as file:
            print(cipher.decode(**kwargs), file=file)

if __name__ == '__main__':
    main()
