from statistics import mean, stdev, median

GRADE_IDX = 2


def extract_student_grade(line):
    lst = line.strip().split(',')
    grade = float(lst[GRADE_IDX])

    return grade


def get_list_of_grades(filepath):
    grades = []

    try:
        gradescope_file = open(filepath, 'r')
    except FileNotFoundError:
        print("WARNING: File '{}' not found. Returning empty list.".format(filepath))
        return []

    gradescope_file.readline()  # header

    for line in gradescope_file:
        grade = extract_student_grade(line)
        grades.append(grade)

    gradescope_file.close()

    return grades


def create_stats_report(grades_filename, report_filename="report.csv"):
    grades = get_list_of_grades(grades_filename)

    average, standard_deviation, med, amount = mean(grades), stdev(grades), median(grades), len(grades)

    report_file = open(report_filename, 'w')

    print("Amount", "Average", "Standard Deviation", "Median", sep=',', file=report_file)
    print(amount, average, standard_deviation, med, sep=',', file=report_file)

    report_file.close()


def main():
    input_filepath = "grades.csv"
    create_stats_report(input_filepath)


main()
