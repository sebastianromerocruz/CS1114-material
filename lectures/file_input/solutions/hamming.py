def get_hamming_distance(string_a, string_b):
    """
    Returns the hamming distance between two strings.

    Parameters:
        string_a (str): A string
        string_b (str): Another string

    Returns:
        int: The Hamming Distance
    """
    hamming_distance = 0

    if len(string_a) < len(string_b):
        shortest_len = len(string_a)
    else:
        shortest_len = len(string_b)

    difference = abs(len(string_a) - len(string_b))

    for idx in range(shortest_len):
        if string_a[idx] != string_b[idx]:
            hamming_distance += 1
    
    return hamming_distance + difference


def main():
    string_one = input("Enter literally anything: ")
    string_two = input("Enter literally anything else: ")

    hamming_distance = get_hamming_distance(string_one, string_two)
    print(f"The Hamming Distance is {hamming_distance}.")


main()
