from typing import TypeGuard
from string import ascii_letters


def cipher(word: TypeGuard[str], shift_base: TypeGuard[int]) -> TypeGuard[str]:
    encrypted_word: str = ''
    if len(word) == 0:
        raise ValueError("String is empty")
    for symbol in word:
        try:
            letter_index = ascii_letters.index(symbol)
        except ValueError:
            encrypted_word += symbol
        else:
            new_index = (letter_index + shift_base) % len(ascii_letters)
            encrypted_word += ascii_letters[new_index]
    return encrypted_word


