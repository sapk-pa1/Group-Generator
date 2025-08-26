# Library Imports
import os

# Internal Imports
from generator.group_creator import GroupGenerator
from utils.logger import get_logger

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Config Logger
logger = get_logger(__name__)

logger.info("Starting group creation")
generator = GroupGenerator()
groups = generator.create_group()

generator.dump_student_groups(path=os.path.join(OUTPUT_DIR, "student_group.json"))
