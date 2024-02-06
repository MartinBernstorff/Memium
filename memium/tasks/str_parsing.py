def get_letter_from_alphabet_position(position: int) -> str:
    return chr(position + 96)  # 96 comes from the Unicode point position for 'a' minus 1


def get_letter_alphabet_position(letter: str) -> int:
    return ord(letter.lower()) - 96
