def get_letter(position: int) -> str:
    return chr(
        position + 96
    )  # 96 comes from the Unicode point position for 'a' minus 1


def get_position(letter: str) -> int:
    return ord(letter.lower()) - 96
