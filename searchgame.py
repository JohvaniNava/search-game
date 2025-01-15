"""
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

"""
from collections import deque
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Function to generate a maze
def generate_maze(rows, cols, obstacle_probability=0.2):
    """
    Generate a maze with random obstacles and a random treasure location.
    
    Args:
        rows (int): Number of rows in the maze.
        cols (int): Number of columns in the maze.
        obstacle_probability (float): Probability of placing an obstacle in any given cell.
        
    Returns:
        np.ndarray: The generated maze.
        tuple: Coordinates of the treasure.
    """
    maze = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            if random.random() < obstacle_probability:
                maze[i, j] = 1  # 1 = obstacle
    while True:
        treasure_row = random.randint(0, rows - 1)
        treasure_col = random.randint(0, cols - 1)
        if maze[treasure_row, treasure_col] == 0:
            maze[treasure_row, treasure_col] = 2  # 2 = treasure
            break
    return maze, (treasure_row, treasure_col)

# BFS with animation support
def bfs_search_with_animation(maze, start, treasure):
    """
    Perform a breadth-first search (BFS) to find the shortest path from the start to the treasure in the maze.
    The search also generates animation frames that visualize the BFS exploration process.

    Args:
        maze (np.ndarray): A 2D array representing the maze, where 1 denotes walls, and 0 denotes open paths.
        start (tuple): The starting point in the maze as a tuple (x, y).
        treasure (tuple): The target point (treasure) in the maze as a tuple (x, y).

    Returns:
        tuple: A tuple containing:
            - path (list): A list of tuples representing the coordinates of the shortest path from the start to the treasure.
            - frames (list): A list of numpy arrays representing the state of the maze at each step of the BFS for animation. 
              If no path is found, `path` will be `None` and the frames will show the full exploration process.
    """
    rows, cols = maze.shape
    visited = np.zeros((rows, cols), dtype=bool)
    queue = deque([(start, [start])])
    frames = []  # To store the frames for animation

    while queue:
        (current, path) = queue.popleft()
        x, y = current

        if current == treasure:
            frames.append((np.copy(maze), current))
            return path, frames  # Return the path and animation frames

        if visited[x, y]:
            continue

        visited[x, y] = True
        maze[x, y] = 0.5  # Mark as part of the search (explored path)
        frames.append((np.copy(maze), current))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if not visited[nx, ny] and maze[nx, ny] != 1:
                    queue.append(((nx, ny), path + [(nx, ny)]))

    return None, frames  # No path to the treasure

def update(frame_data):
    """
    Update the animation frame with the agent's current position.

    Args:
        frame_data (tuple): A tuple containing the current frame of the maze and the agent's position.
    """
    frame, current = frame_data
    x, y = current

    # Create a copy of the maze to highlight the agent's position
    display_frame = np.copy(frame)
    display_frame[x, y] = 1.75   # Mark agent's current position as black (0 in the color map)
 
    im.set_array(display_frame)
    ax.set_title(f"Agent at {current}")
    return im,

# Maze dimensions
rows, cols = 30, 30  # Adjust for testing purposes

# Generate the maze
maze, treasure_pos = generate_maze(rows, cols, obstacle_probability=0.3)

# Starting position of the agent is random
start_pos = (random.randint(0, rows - 1), random.randint(0, cols - 1))

# Ensure the start position is not an obstacle
while maze[start_pos] == 1:
    start_pos = (random.randint(0, rows - 1), random.randint(0, cols - 1))

# Find the treasure with animation
path_to_treasure, animation_frames = bfs_search_with_animation(maze, start_pos, treasure_pos)

# Create animation
fig, ax = plt.subplots(figsize=(8, 8))
im = ax.imshow(maze, cmap="hot")

ani = animation.FuncAnimation(
    fig, update, frames=animation_frames, interval=100, blit=False, repeat=False
)

plt.show()

# Output path and steps
if path_to_treasure:
    print(f"Path to the treasure: {path_to_treasure}")
    print(f"Number of steps: {len(path_to_treasure)}")
else:
    print("No path to the treasure found!")
