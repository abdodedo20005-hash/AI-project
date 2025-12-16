# Vacuum Cleaner Intelligent Agent

## Project Overview
This project simulates an intelligent vacuum cleaner agent that operates in a grid-based environment.  
The agent’s goal is to clean all dirty cells in the room while minimizing the number of movements, using different search algorithms studied in Artificial Intelligence.

---

## Problem Statement
An intelligent vacuum cleaner needs to clean a room represented as a grid that contains clean and dirty cells.  
The objective is to reach and clean all dirty cells using the minimum number of steps, while making intelligent decisions about movement.

---

## Why is this Problem Important?
- It is a practical application of Search Algorithms in Artificial Intelligence.
- It represents an intelligent agent that perceives its environment and makes decisions.
- It helps compare the behavior and efficiency of different search strategies.

---

## Algorithms Used
The project implements and compares multiple search algorithms, each developed by a different team member:

- **Breadth-First Search (BFS)**  
  Implemented by: *Abdelrahman Osama*

- **Depth-First Search (DFS)**  
  Implemented by: *Abdelrahman Ismail*

- **Uniform Cost Search (UCS)**  
  Implemented by: *Abdelrahman El-Hebian*

- **Iterative Deepening Search (IDS)**  
  Implemented by: *Amr Khaled*

- **A\* Search Algorithm**  
  Implemented by: *Omar Hashem*

Each algorithm is used to find a path from the vacuum’s current position to a dirty cell.

---

## Project Workflow (How It Works)
1. Generate the environment as a 2D grid.
2. Identify all dirty cells in the room.
3. Select a target dirty cell.
4. Apply the selected search algorithm to find a path.
5. Move the vacuum cleaner along the path.
6. Clean the dirty cell.
7. Repeat the process until all cells are clean.

---

## Output
- The **movement path** of the vacuum cleaner.
- The final state of the room, where all cells are clean.

---

## Technologies Used
- Programming Language: Python
- Concepts: Artificial Intelligence, Search Algorithms, Intelligent Agents

---

## How to Run the Project
1. Make sure Python is installed on your system.
2. Clone the repository:
   ```bash
   git clone https://github.com/abdodedo20005-hash/AI-project.git
