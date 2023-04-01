READ_MODE = 'r'
DECIMAL_PRECISION = 2
DEFAULT_SEPARATOR, FILE_SEPARATOR = ' ', ','
ID_IDX, GRADES_IDX = 0, 1


def get_line_sum(string, separator=DEFAULT_SEPARATOR):
    """
    Gets the sum of a string of numbers separated by a single space. Assumes valid input.

    :param separator: Separator to use in string when splitting
    :param string: A string containing numbers separated by a space
    :return: The sum of such numbers
    """
    string = string.split(separator)
    summation = 0

    for element in string:
        try:
            element = float(element)
        except ValueError:
            print("WARNING: Non-numerical grade found ({}) and ignored.".format(element))
        else:
            summation += element

    return summation


def get_file_sums(filepath):
    """
    Returns a list of tuples containing the sum of the grades of students, each identifies by an ID, contained in a text
    file.

    :param filepath: A string containing the path of a text file
    :return: A list of tuples
    """
    try:
        file_obj = open(filepath, READ_MODE)
    except FileNotFoundError:
        print("WARNING: File {} not found. Returning empty list.".format(filepath))
        return []

    sums = []

    for string in file_obj:
        grades = string.strip()

        summation = get_line_sum(grades, FILE_SEPARATOR)
        sums.append(round(summation, DECIMAL_PRECISION))

    file_obj.close()

    return sums


def main():
    filepath = "student_grades_incomplete.csv"
    file_sums = get_file_sums(filepath)
    print(file_sums)


main()
