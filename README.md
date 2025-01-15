Johvani Nava 
CST-580 Artificial Intelligence
January 15, 2025

This script generates a random maze and uses a breadth-first search (BFS) algorithm to find the shortest path from a random starting point to a treasure. 
It also visualizes the search process through an animation. The maze is represented as a 2D array where obstacles are marked by 1s, open paths by 0s, 
and the treasure by 2s. The BFS algorithm explores the maze step by step, updating the animation frames to show the agent's movement. 
If a path to the treasure is found, the shortest path and the total number of steps are printed. If no path is found, 
the script outputs that no path is available.

Steps in the script:
1. Generate a random maze with obstacles and a randomly placed treasure.
2. Perform a BFS search to find the shortest path from a random starting point to the treasure.
3. Animate the BFS search process, displaying each step of the exploration.
4. Output the path to the treasure and the number of steps, or indicate if no path was found.

Dependencies:
- numpy: For matrix manipulation.
- matplotlib: For creating the animation and visualizing the maze.
- random: For generating random start and treasure locations.

Functions:
- generate_maze: Generates a maze with random obstacles and a treasure location.
- bfs_search_with_animation: Performs a BFS search to find the treasure and generates animation frames.
- update: Updates the animation frame to show the agent's current position.
