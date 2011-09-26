from collections import defaultdict

from ngram import Ngram

class Sentence:
    def __init__(self, tokens):
        self._sen = list(tokens)
        self.create_tok_index()

    def __len__(self):
        return len(self._sen)

    def __iter__(self):
        return iter(self._sen)
    def __reversed__(self):
        return reversed(self._sen)

    def __getitem__(self, key):
        return self._sen[key]

    def __setitem__(self, key, value):
        self._sen[key] = value

    def __delitem__(self, key):
        del self._sen[key]

    def __contains__(self, item):
        return item in self._index

    def create_tok_index(self):
        self._index = defaultdict(set)
        for i, tok in enumerate(self._sen):
            self._index[tok].add(i)

    def ngram_positions(self, ngram):
        if not isinstance(ngram, Ngram):
            raise TypeError
        result = []

        for starter_index in self._index[ngram[0]]:
            good = True
            for tok_i, tok in enumerate(ngram[1:]):
                try:
                    # search for remaining tokens
                    if self[starter_index + 1 + tok_i] == tok:
                        pass
                    else:
                        good = False
                        break
                except IndexError:
                    good = False
                    break
            if good:
                result.append(starter_index)
        return result

    def remove_ngram(self, ngram):
        positions = self.ngram_positions(ngram)
        for pos in positions:
            del self._sen[pos:pos+len(ngram)]

            # maintaining index
            for i in xrange(len(ngram)):
                self._index[ngram[i]].remove(pos+i)



