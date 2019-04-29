"""Interface for cipher classes"""

from abc import abstractmethod
from pathlib import Path
from typing import Union


class Cipher:
    def file_encrypt(self, filename: Union[str, Path]):
        """Encrypt an entire text file line by line, writes output with file suffix .enc"""
        input_ = Path(filename)
        output_ = input_.with_suffix(".enc")
        with input_.open("r") as in_, output_.open("w") as out_:
            for line in in_:
                print(self.encrypt(line), file=out_)

    def file_decrypt(self, filename: Union[str, Path]):
        """Decrypt an entire text file line by line, writes output with file suffix .dec"""
        input_ = Path(filename)
        output_ = input_.with_suffix(".dec")
        with input_.open("r") as in_, output_.open("w") as out_:
            for line in in_:
                print(self.decrypt(line), file=out_)

    def encrypt(self, line: str) -> str:
        """Perform encryption on a single line"""
        return self._encrypt(line)

    def decrypt(self, line: str) -> str:
        """Perform decryption on a single line"""
        return self._decrypt(line)

    @abstractmethod
    def _encrypt(self, line: str) -> str:
        pass

    @abstractmethod
    def _decrypt(self, line: str) -> str:
        pass
