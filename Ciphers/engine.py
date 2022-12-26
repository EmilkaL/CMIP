from .alphabet import Alphabet
from .base_scramblers import *


class NumCipher:

    def __init__(self, alphabet: Alphabet, scrambler:Scrambler) -> None:
        self.scrambler = scrambler
        self.alphabet = alphabet
        
    def encode(self, phrase, *args, **kwargs):
        self.scrambler.validator(phrase, *args, **kwargs)
        self.scrambler.preprocessor(phrase, *args, **kwargs)
        output = ''
        counter_cipher = 0
        counter = 0
        for symb in phrase:
            is_upper = symb.isupper()
            symb = symb.lower()
            
            if self.alphabet.get(symb) != symb:
                kwargs['counter_cipher'], kwargs['counter'], kwargs['symb'] = counter_cipher, counter, symb
                symb, kwargs = self.scrambler.encoder(*args, **kwargs)
                counter_cipher += 1
            counter += 1
            output += symb.upper() if is_upper else symb
        return output
    
    def decode(self, phrase, *args, **kwargs):
        self.scrambler.validator(phrase, *args, **kwargs)
        self.scrambler.preprocessor(phrase, *args, **kwargs)
        output = ''
        counter_cipher = 0
        counter = 0
        for symb in phrase:
            is_upper = symb.isupper()
            symb = symb.lower()
            
            if self.alphabet.get(symb) != symb:
                kwargs['counter_cipher'], kwargs['counter'], kwargs['symb'] = counter_cipher, counter, symb
                symb, kwargs = self.scrambler.decoder(*args, **kwargs)
                counter_cipher += 1
            counter += 1
            output += symb.upper() if is_upper else symb
        return output