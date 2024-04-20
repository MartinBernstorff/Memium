import hashlib


def hash_str_to_int(input_string: str, max_length: int = 10) -> int:
    # Convert the string to bytes
    bytes_string = input_string.encode()

    # Create a SHA256 hash object
    hash_object = hashlib.sha256(bytes_string)

    # Hex digest the hash and convert it to an integer
    unique_int = int(hash_object.hexdigest(), 16)
    shortened = unique_int % 10**max_length

    return shortened
