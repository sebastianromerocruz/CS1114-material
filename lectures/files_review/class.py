from ceasar_decryptor import decrypt_string


# function signature 2pts; correct variables and order 2pts
def get_decoded_lines(encoded_message, encryption_key):
    # decoding message and saving it 2pts
    decoded_message = decrypt_string(encoded_message, encryption_key)
    # splitting 2pts
    decoded_lines = decoded_message.split("STOP")

    for index in range(len(decoded_lines)):
        decoded_lines[index] = decoded_lines[index].strip()

    # returning 3pts
    return decoded_lines


# function signature 2pts; correct number and order of params 2pts; Optional params 1pts
def create_decoded_telegram(input_path, output_path="decoded_telegram.csv"):
    try:
        # the line that can fail
        in_file = open(input_path, 'r')
    except FileNotFoundError:
        # What to do if it fails
        print("ERROR: Could not open file {}.".format(input_path))
        return

    # What to do if the it didn't fail
    key = in_file.readline().strip()  # "42"
    try:
        key = int(key)
    except ValueError:
        return

    message = in_file.readline().strip()

    decoded_lines = get_decoded_lines(message, key)

    output_file = open(output_path, 'w')
    # method 1
    for line in decoded_lines:
        # print the line in the file output_file, each line ending with a .\n
        print(line, file=output_file, end=".\n")

    # # method 2
    # whole_message = ".\n".join(decoded_lines)
    # print(whole_message, file=output_file)

    in_file.close()


def main():
    create_decoded_telegram("encoded_telegram.txt")


main()
