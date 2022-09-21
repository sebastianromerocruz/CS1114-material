class_size_a = 35
class_size_b = 15

num_of_students = int(input("How large is the student body? "))

num_size_a = num_of_students // class_size_a
num_of_students = num_of_students % class_size_a

num_size_b = num_of_students // class_size_b
num_of_students = num_of_students % class_size_b

print("We formed " + str(num_size_a) + " 35-student classroom(s), " + str(num_size_b) +
      " 15-student classrooms, and have " + str(num_of_students) + " leftover students.")
