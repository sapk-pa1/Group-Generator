# Library Imports
import random
import json


# Internal Imports
from utils.utility import get_student_names, get_group_info
from collections import defaultdict
from utils.utility import random_choice
from utils.logger import get_logger
from config import SEED

logger = get_logger(__name__)

random.seed(SEED)


class GroupGenerator:
    def __init__(self) -> None:

        self.students = get_student_names()
        self.groups = defaultdict(list)
        self.group_info = get_group_info()

    def create_group(self):
        logger.info("Creating groups")
        available_students = self.students.copy()

        num_groups = self.group_info["no_of_groups"]
        leftover = self.group_info["no_of_remaining_students"]
        student_per_group = self.group_info["student_per_group"]
        logger.info(
            f"Group Info - Num Groups: {num_groups}, Students per Group: {student_per_group}, Leftover Students: {leftover}"
        )

        # Create groups with base size
        for i in range(num_groups):
            for _ in range(student_per_group):
                student = random_choice(available_students)
                self.groups[f"Group_{i+1}"].append(student)
                available_students.remove(student)

        # Distribute leftover students randomly
        for i in range(leftover):
            if available_students:
                # Get the Random Groups
                group = random.choice(list(self.groups.keys()))
                student = random_choice(available_students)
                self.groups[group].append(student)
                available_students.remove(student)

        return dict(self.groups)

    def dump_student_groups(self, path: str):
        with open(path, "w") as f:
            json.dump(self.groups, f, indent=4)
        logger.info(f"Student groups dumped to {path}")

        return None


if __name__ == "__main__":
    generator = GroupGenerator()
    result = generator.create_group()
    for group, members in result.items():
        print(group, ":", members)
