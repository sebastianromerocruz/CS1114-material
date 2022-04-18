"""
Sebastián Romero Cruz
CS-UY 1114

"""
ASCII_A_UPPER = ord('A')
ASCII_A_LOWER = ord('a')
ALPHABET_LEN = 26


def decrypt_character(character: str, key: int) -> str:
    """
    Decrypts a single ASCII character from Caesar cipher encryption using a user-given key.

    Caesar cipher: E(x) = (x - 26) mod 26.

    Returns decoded character.
    :param character: An encoded character
    :param key: A decryption key integer
    :return: A decoded character
    """
    if type(character) != str:
        raise TypeError("Messages must be an str type, not {}.".format(type(character)))
    if type(key) != int:
        raise TypeError("Decryption key must be an int type, not {}.".format(type(character)))

    if not character.isalpha():
        return character

    # Base to ord 0
    ascii_eq = ord(character)
    ascii_eq -= ASCII_A_UPPER if character.isupper() else ASCII_A_LOWER

    # Decrypt and rebase to original ord
    ascii_eq = (ascii_eq - key) % ALPHABET_LEN
    ascii_eq += ASCII_A_UPPER if character.isupper() else ASCII_A_LOWER

    return chr(ascii_eq)


def decrypt_string(string: str, key: int) -> str:
    """
    Returns a decoded Caesar cipher-encrypted message.

    :param string: An encoded string
    :param key: The encryption key
    :return: A decoded string
    """
    return "".join(decrypt_character(char, key) for char in string)


if __name__ == '__main__':
    print(decrypt_string("Yj mqid'j weydw je ru jxqj uqio beb we rqsa je oekh emd vybu", 42))
