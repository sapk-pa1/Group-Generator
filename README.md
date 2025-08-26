# Student Group Generator


This project provides a simple way to **create and manage student groups** programmatically.
It generates student group data and exports it into a JSON file for easy access and further use.


---


## 🚀 Features
- Automatically generates student groups using `GroupGenerator`.
- Saves the generated groups into a JSON file (`student_group.json`).
- Includes a logging utility for tracking workflow execution.
- Output is stored in a dedicated `output/` directory.


---




## ⚙️ How It Works
1. Creates an `output/` directory if it does not exist.
2. Configures a logger to track the execution process.
3. Initializes a `GroupGenerator` instance.

## 🏃 Running the Script

1. **Prepare the Student List**  
   - Add student names in the `data/students.txt` file.  
   - Each student name should be placed on a new line.  

2. **Configure Group Settings**  
   - Open the `config.py` file.  
   - Update the values for the number of groups and the desired group size per student.  

3. **Execute the Script**  
   Run the following command from the project root:  
   ```bash
   python main.py