READ_MODE = 'r'
DECIMAL_PRECISION = 2
DEFAULT_SEPARATOR, FILE_SEPARATOR = ' ', ','
ID_IDX, GRADES_IDX = 0, 1
FILEPATH = "student_grades.txt"


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
        element = float(element)
        summation += element

    return summation


def get_sums(lst):
    """
    Creates and returns a list of sums, given a list of strings each containing numbers separated by a single space.

    :param lst: A list of strings containing numbers
    :return: A list of float sums rounded to the 2nd decimal place
    """
    sums = []

    for string in lst:
        summation = get_line_sum(string, DEFAULT_SEPARATOR)
        sums.append(round(summation, 2))

    return sums


def get_file_sums(filepath):
    """
    Returns a list of tuples containing the sum of the grades of students, each identifies by an ID, contained in a text
    file.

    :param filepath: A string containing the path of a text file
    :return: A list of tuples
    """
    file_obj = open(filepath, READ_MODE)

    sums = []

    for string in file_obj:
        string = string.split()
        student_id = string[ID_IDX]
        grades = string[GRADES_IDX]

        summation = get_line_sum(grades, FILE_SEPARATOR)
        student_info = (student_id, round(summation, DECIMAL_PRECISION))
        sums.append(student_info)

    file_obj.close()

    return sums


def main():
    # Without files
    sample_list = [
        '50.98 82.72 89.18 51.57 23.95 69.82',
        '57.7 13.08 1.26 6.15 52.09 42.63 39.46',
        '96.21 43.32 79.45 7.87 10.5 10.92 67.87 21.22',
        '27.27 40.23 79.09 17.56 75.87 80.38 40.98 6.21 44.72 36.45',
        '0.07 29.63 97.73 58.01 97.47 24.07 83.46 99.4',
        '14.03 55.63 31.57 0.01 73.4 91.35 82.06 59.62 2.83 93.04'
    ]

    sums = get_sums(sample_list)
    print(sums)

    # With files
    file_sums = get_file_sums(FILEPATH)
    print(file_sums)


if __name__ == '__main__':
    main()
