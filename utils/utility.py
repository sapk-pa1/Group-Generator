from typing import List, Dict, Any
import random
from config import SEED
from config import NUM_OF_STUDENTS, NUM_OF_STUDENTS_PER_GROUP


def get_student_names() -> List[str]:
    """Generates the list of the students from the given file

    Returns:
        List[str]: List of Student
    """
    with open("data/students.txt") as f:
        students: list = f.readlines()
    # Clean the Students List for white spaces of new line character
    students = [student.strip() for student in students]
    return students


def get_group_info(
    number_of_students: int = NUM_OF_STUDENTS,
    number_of_student_per_group: int = NUM_OF_STUDENTS_PER_GROUP,
) -> Dict[str, Any]:
    """Returns the total Groups that can be formed with Remaining students

    Args:
        number_of_students (int): total number of students
        number_of_student_per_group (int): number of student in 1 group

    Returns:
        int: _description_
    """
    number_of_groups = number_of_students // number_of_student_per_group
    number_of_students_left = number_of_students % number_of_student_per_group
    return {
        "no_of_groups": number_of_groups,
        "no_of_remaining_students": number_of_students_left,
        "student_per_group": NUM_OF_STUDENTS_PER_GROUP,
    }


def random_choice(choices: List) -> str:
    return random.choice(choices)


if __name__ == "__main__":
    print(get_group_info(13, 4))
    students = get_student_names()
    print(random_choice(students))
