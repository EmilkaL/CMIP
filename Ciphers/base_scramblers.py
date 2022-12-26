import math
from .alphabet import Alphabet

class Scrambler:
    def __init__(self) -> None:
        pass
    
    def validator(self, *args, **kwargs) -> bool: ...
    def preprocessor(self, *args, **kwargs): ...
    def encoder(self, *args, **kwargs) -> tuple[str, dict]: ...
    def decoder(self, *args, **kwargs) -> tuple[str, dict]: ...

class SimpleScrambler(Scrambler):
    
    def __init__(self, alphabet: Alphabet) -> None:
        self.alphabet = alphabet
        
    def validator(self, *args, **kwargs):
        for symb in kwargs['sub_alphabet']:
            if self.alphabet.get(symb.lower()) == symb.lower():
                raise ValueError('Ключ может состоять только из символов алфавита.')
        return True
    
    def preprocessor(self, *args, **kwargs):
        self.sub_alphabet = self.__create_encoding_alphabet(kwargs['sub_alphabet'])
        
    def __create_encoding_alphabet(self, alphabet):
        key_compensator = list(self.alphabet.alphabet_str.keys())
        for symb in alphabet:
            if symb in key_compensator:
                del key_compensator[key_compensator.index(symb)]
            else:
                raise TypeError('Ошибка ключа, введите его согласно алфавиту')
        output = {'encode': {}, 'decode': {}}
        for i, symb in enumerate(list(alphabet) + key_compensator):
            output['encode'][i] = self.alphabet.get(symb)
            output['decode'][self.alphabet.get(symb)] = i
        return output


    def encoder(self, *args, **kwargs):
        symb = kwargs['symb']
        symb = self.sub_alphabet['encode'][self.alphabet.get(symb)]
        symb = self.alphabet.get(symb)
        return symb, kwargs
        
        
    def decoder(self, *args, **kwargs):
        symb = kwargs['symb']
        symb = self.sub_alphabet['decode'][self.alphabet.get(symb)]
        symb = self.alphabet.get(symb)
        return symb, kwargs


class AfinScrambler(Scrambler):
    
    def __init__(self, alphabet: Alphabet) -> None:
        self.alphabet = alphabet
        
    def validator(self, *args, **kwargs):
        if not self.__check_key_afin(kwargs['a']):
            raise ValueError('Длина алфавита и ключ a должны быть взаимнопростыми')
    
    def __check_key_afin(self, a, *args, **kwargs):
        return math.gcd(a, len(self.alphabet)) == 1
    
    def preprocessor(self, *args, **kwargs):
        pass

    def encoder(self, *args, **kwargs):
        symb = kwargs['symb']
        a, b = kwargs['a'], kwargs['b']
        symb = self.alphabet.get(
            (self.alphabet.get(symb) * a + b) % len(self.alphabet)
        )
        return symb, kwargs
    
    def __find_reverse_number(self, a, p):
        reverse = 0
        while (reverse * a % p != 1):
            reverse += 1
        return reverse 
    
    def decoder(self, *args, **kwargs):
        symb = kwargs['symb']
        a, b = kwargs['a'], kwargs['b']
        rev_num = self.__find_reverse_number(a, len(self.alphabet))
        symb = self.alphabet.get(
            ((self.alphabet.get(symb) - b) * (rev_num)) % len(self.alphabet)
        )
        return symb, kwargs


class AfinRecScrambler(Scrambler):
    
    def __init__(self, alphabet: Alphabet) -> None:
        self.alphabet = alphabet
        
    def validator(self, *args, **kwargs):
        if not (self.__check_key_afin(kwargs['a1']) and self.__check_key_afin(kwargs['a2'])):
            raise ValueError('Длина алфавита и ключи a1, а2 должны быть взаимнопростыми')
    
    def __check_key_afin(self, a, *args, **kwargs):
        return math.gcd(a, len(self.alphabet)) == 1
    
    def preprocessor(self, *args, **kwargs):
        pass

    def encoder(self, *args, **kwargs):
        symb = kwargs['symb']
        counter = kwargs['counter_cipher']
        if counter == 0:
            a, b = kwargs['a1'], kwargs['b1']
        elif counter == 1:
            a, b = kwargs['a2'], kwargs['b2']
        else:
            a = (kwargs['a1'] * kwargs['a2']) % len(self.alphabet)
            b = (kwargs['b1'] + kwargs['b2']) % len(self.alphabet)
            kwargs['a1'], kwargs['a2'] =  kwargs['a2'], a
            kwargs['b1'], kwargs['b2'] = kwargs['b2'], b
        symb = self.alphabet.get(
            (self.alphabet.get(symb) * a + b) % len(self.alphabet)
        )
        return symb, kwargs
    
    def __find_reverse_number(self, a, p):
        reverse = 0
        while reverse * a % p != 1:
            reverse += 1
        return reverse 
    
    def decoder(self, *args, **kwargs):
        symb = kwargs['symb']
        counter = kwargs['counter_cipher']
        if counter == 0:
            a, b = kwargs['a1'], kwargs['b1']
        elif counter == 1:
            a, b = kwargs['a2'], kwargs['b2']
        else:
            a = (kwargs['a1'] * kwargs['a2']) % len(self.alphabet)
            b = (kwargs['b1'] + kwargs['b2']) % len(self.alphabet)
            kwargs['a1'], kwargs['a2'] =  kwargs['a2'], a
            kwargs['b1'], kwargs['b2'] = kwargs['b2'], b
        symb = self.alphabet.get(
            ((self.alphabet.get(symb) - b) * (self.__find_reverse_number(a, len(self.alphabet)))) % len(self.alphabet)
        )
        return symb, kwargs