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