"""A simple configurable ceaser cipher"""

from abc import abstractmethod
from collections import OrderedDict
from string import ascii_lowercase
from typing import Dict

from base.cipher import Cipher


class Ceaser(Cipher):
    def __init__(self):
        self.cipher_map = self._get_cipher_map()
        self.decipher_map = self._get_decipher_map()
        pass

    @abstractmethod
    def _cipher_alphabet(self) -> str:
        """Return a lowercase string of the cipher chars to use in place of a..z

        Essentially this is the positional mapping of characters from 0..25
        e.g. abc....xyz might map to bcd...yza (when shifted by 1)"""
        pass

    def _get_cipher_map(self) -> Dict[str, str]:
        """Map the regular alphabet upper and lower to the cipher alphabet"""
        cipher_lowercase = self._cipher_alphabet()
        cipher_map = {
            k: v for k, v in zip(list(ascii_lowercase), list(cipher_lowercase))
        }
        for k, v in zip(list(ascii_lowercase.upper()), list(cipher_lowercase.upper())):
            cipher_map[k] = v
        return cipher_map

    def _get_decipher_map(self) -> Dict[str, str]:
        """Revese mapping of the cipher map"""
        return {v: k for k, v in self.cipher_map.items()}

    def _encrypt(self, line: str) -> str:
        return "".join(
            [
                self.cipher_map[char] if char in self.cipher_map else char
                for char in line
            ]
        )

    def _decrypt(self, line: str) -> str:
        return "".join(
            [
                self.decipher_map[char] if char in self.decipher_map else char
                for char in line
            ]
        )


class CeaserKey(Ceaser):
    """Create a simple cipher by assigning a keyword to map the cipher alphabet

    e.g. keyword=juluisceaser
    abcdefghijklmnopqrstuvwxyz
    juliscaertvwxyzbdfghkmnopq"""

    def __init__(self, keyword: str) -> None:
        # this remove spaces and duplicate letters in the keyword
        self.keyword = "".join(OrderedDict.fromkeys(keyword.lower())).replace(" ", "")
        super().__init__()

    def _cipher_alphabet(self) -> str:
        cipher_lowercase = self.keyword + "".join(
            [char for char in ascii_lowercase if char not in self.keyword]
        )
        return cipher_lowercase


class CeaserShift(Ceaser):
    """Create a simple cipher by moving shifting the alphabet by N char

    e.g. shift=3
    abcdefghijklmnopqrstuvwxyz
    defghijklmnopqrstuvwxyzabc"""

    def __init__(self, shift: int) -> None:
        assert shift > 0 and shift < 26
        self.N = shift
        super().__init__()

    def _cipher_alphabet(self) -> str:
        cipher_lowercase = ascii_lowercase[self.N :] + ascii_lowercase[: self.N]
        return cipher_lowercase


if __name__ == "__main__":

    line = "the lazy brown dog fox"

    # example of the ceaser cipher with a keyword
    ceaser_key = CeaserKey(keyword="foobar")
    foo = ceaser_key.encrypt(line=line)
    bar = ceaser_key.decrypt(line=foo)
    print(f"line: {line}, encrypted: {foo}, decrypted: {bar}")

    # example of the ceaser cipher with a positional shift 1:26
    ceaser_shift = CeaserShift(shift=10)
    foo = ceaser_shift.encrypt(line=line)
    bar = ceaser_shift.decrypt(line=foo)
    print(f"line: {line}, encrypted: {foo}, decrypted: {bar}")
