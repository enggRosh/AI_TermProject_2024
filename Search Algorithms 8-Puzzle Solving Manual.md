
# Search Algorithms for 8-Puzzle Solving: User Documentation

## Project Overview

### Introduction
The 8-puzzle is a classic problem in computer science and artificial intelligence that involves rearranging tiles on a 3x3 grid to reach a specified goal configuration. This project explores two search algorithms:
- **Breadth-First Search (BFS):** An uninformed level-by-level exploration guaranteeing the shortest path.
- **A* Search (A*):** A heuristic-guided algorithm that uses the Manhattan distance to optimize efficiency.

The project aims to compare the performance of these algorithms in solving the 8-puzzle problem, focusing on solution path length, nodes expanded, maximum frontier size, and execution time.

### Team Members
- Ratul Mazumder
- Sai Venkata Ramana Sampath Kothuri
- Roshani Jha

## Algorithms and Methodology

### Breadth-First Search (BFS)
- **Characteristics:** Uninformed, exhaustive search guaranteeing optimal solutions.
- **Strengths:** Guarantees shortest path.
- **Weaknesses:** Memory-intensive as all nodes at a level are stored.
- **Implementation Details:** [bfs_solver.py](bfs_solver.py)

### A* Search
- **Heuristic Used:** Manhattan distance, calculating the sum of tile moves required to reach the goal.
- **Strengths:** Focuses on promising paths, reducing node expansion and memory usage.
- **Weaknesses:** Efficiency is dependent on the heuristic's accuracy.
- **Implementation Details:** [astar_solver.py](astar_solver.py)

## Installation and Setup

1. Ensure Python 3.x is installed on your system.
2. Clone the repository:
   ```bash
   git clone https://github.com/enggRosh/AI_TermProject_2024
   ```
3. Navigate to the project directory:
   ```bash
   cd AI_TermProject_2024
   ```
4. Install any dependencies (if required).

## Usage Instructions

1. **Running BFS Solver:**
   - Execute the `bfs_solver.py` script to solve a predefined puzzle configuration using BFS:
     ```bash
     python bfs_solver.py
     ```
   - Results will be appended to `bfs_output.txt`.

2. **Running A* Solver:**
   - Execute the `astar_solver.py` script to solve the puzzle using A*:
     ```bash
     python astar_solver.py
     ```
   - Results will be logged in `a_star_output.txt`.

3. **Custom Configurations:**
   - Modify the `startState` variable in the respective scripts to define a custom initial configuration.

## Example Outputs

### BFS
```
Start State: [1, 8, 2, 0, 4, 3, 7, 6, 5]
Path: ['Right', 'Up', 'Left', 'Down', ...]
Cost: 21
Nodes Expanded: 70957
Max Search Depth: 22
Max Frontier: 21811
Running Time: 0.904 seconds
```

### A*
```
Start State: [1, 8, 2, 0, 4, 3, 7, 6, 5]
Path: ['Right', 'Up', 'Left', 'Down', ...]
Cost: 21
Nodes Expanded: 1743
Max Search Depth: 21
Max Frontier: 1023
Running Time: 0.084 seconds
```

## Evaluation Metrics

The algorithms are evaluated based on:
1. **Solution Path Length:** Optimal moves to reach the goal.
2. **Nodes Expanded:** Number of states processed.
3. **Max Frontier Size:** Peak memory usage.
4. **Execution Time:** Time taken to find the solution.

## Key Findings
- **BFS:** Guarantees shortest paths but has significant memory usage and execution time for complex configurations.
- **A* (Manhattan Heuristic):** Outperforms BFS in efficiency while maintaining optimal solutions.

## Challenges and Solutions
- **BFS Memory Constraints:** Optimized data structures were used to manage memory.
- **Heuristic Optimization for A*:** Refined the Manhattan heuristic for better focus on promising paths.

## References
- [Jananji et al., 2024](https://journals.sjp.ac.lk/index.php/vjs/article/view/7494)
- [Mishra et al., 2017](https://ieeexplore.ieee.org/document/8245012)
- [Mathew et al., 2014](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C7&q=Mathew%2C+Kuruvilla%2C+and+Mujahid+Tabassum.+%22Experimental+comparison+of+uninformed+and+heuristic+AI+algorithms+for+N+Puzzle+and+8+Queen+puzzle+solution.%22%C2%A0Int.+J.+Dig.+Inf.+Wireless+Commun.%28IJDIWC%29%C2%A04.1+%282014%29%3A+143-154.&btnG=)

## Contact
For any queries or contributions, contact the team via the [GitHub repository](https://github.com/enggRosh/AI_TermProject_2024).
