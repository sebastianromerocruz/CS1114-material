from ceasar_decryptor import decrypt_string

TELEGRAM_SEP = " STOP "


def get_decoded_lines(encoded_message, key):
    decoded_message = decrypt_string(encoded_message, key)
    decoded_message = decoded_message.split(TELEGRAM_SEP)

    return decoded_message


def create_decoded_telegram(encoded_filepath, decoded_filepath="decoded_telegram.txt"):
    try:
        input_file = open(encoded_filepath, 'r')
    except FileNotFoundError:
        print("NON-FATAL ERROR: Encoded telegram file {} could not be found.".format(encoded_filepath))
        return

    key = input_file.readline().strip()

    try:
        key = int(key)
    except ValueError:
        print("NON-FATAL ERROR: Invalid encryption key '{}'. Must be able to be casted as int.".format(key))
        return

    encoded_message = input_file.readline().strip()
    input_file.close()

    decoded_lines = get_decoded_lines(encoded_message, key)
    output_file = open(decoded_filepath, 'w')

    for line in decoded_lines:
        print(line, end='.\n', file=output_file)

    # # You can also achieve this using the join() method:
    # decoded_message = ".\n".join(decoded_lines)
    # print(decoded_message, file=output_file)
    output_file.close()


def main():
    create_decoded_telegram("encoded_telegram.txt", "output.txt")


main()
