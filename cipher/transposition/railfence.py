"""Transposition algorithms for simple encoding"""

import math
import numpy as np
from typing import List
from itertools import zip_longest

from base.cipher import Cipher


# pg. 8 The Code Book
class RailFence(Cipher):
    """Breaks up text into N lines by every Nth word, arranges lines in sequence"""

    def __init__(self, number_of_rails: int) -> None:
        assert number_of_rails > 0
        self.n_rails = number_of_rails

    def _get_rail_assignment(self, line) -> np.array:
        """Assign each letter a rail number

        >>> get_rail_assignment(line='the lazy brown dog fox')
        [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
        """
        N = len(line)
        return np.tile(range(self.n_rails), reps=math.ceil(self.n_rails * N))[:N]

    def _encrypt(self, line: str) -> str:
        rail_assignment = self._get_rail_assignment(line)
        line_array = np.array(list(line))
        # assign all char in a rail to a list
        # e.g. line=decrypt; n_rail=3; rails=["drt", "eye", "cpt"]
        rails: List[str] = [
            "".join(line_array[rail_assignment == n]) for n in range(self.n_rails)
        ]
        return "".join(rails)

    def _decrypt(self, line: str) -> str:
        encrypt_assignment = self._get_rail_assignment(line)
        encrypt_assignment.sort()
        line_array = np.array(list(line))
        # line=decrypt; n_rail=3; encrypted_rails=["drt", "eye", "cpt"]
        encrypt_rails: List[str] = [
            list(line_array[encrypt_assignment == n]) for n in range(self.n_rails)
        ]
        # e.g. ["dec", "ryp", "ted"]
        reconstructed_pairs: List[str] = [
            "".join(rail) for rail in zip_longest(*encrypt_rails, fillvalue="")
        ]
        # return reconstructed_pairs
        return "".join(reconstructed_pairs)


if __name__ == "__main__":

    rf = RailFence(number_of_rails=3)
    line = "the lazy brown dog fox"
    print(f"line: {line}")
    foo = rf.encrypt(line=line)
    print(f"encrypt: {foo}")
    bar = rf.decrypt(line=foo)
    print(f"decrypt: {bar}")
