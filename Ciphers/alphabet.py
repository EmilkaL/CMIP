class Alphabet:
    
    def __init__(self, lang, alphabet) -> None:
        self.lang = lang
        self.alphabet_str = {}
        self.alphabet_int = {}
        if len(set(alphabet)) != len(alphabet):
            raise ValueError('Повторяющиеся символы в алфавите')
        
        for i, symb in enumerate(alphabet):
            self.alphabet_str[symb] = i
            self.alphabet_int[i] = symb
    
    def get(self, symb):
        if isinstance(symb, str):
            if symb in self.alphabet_str:
                return self.alphabet_str[symb]
            else:
                return symb
        elif isinstance(symb, int):
            
            return self.alphabet_int[symb]
        
        
    def __len__(self):
        return len(self.alphabet_int)