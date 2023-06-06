import time
from collections import deque
import sys

# Question 1.3


def bfs(maze, start, goal, queue=None, visited=None, parent=None):
    sys.setrecursionlimit(10000000)
    if queue is None:
        # Creates a queue with start node in
        queue = deque([start])
    if visited is None:
        # Creates a set for visited nodes
        visited = set()
    if parent is None:
        parent = {}
    if not queue:
        return None
    
    # Creates gives the current variable with the value of the current node
    current = queue.popleft()
    # Adds the current node location the the visited nodes set 
    visited.add(current)
    
    if current == goal:
        # Checks if the current node matches the goal
        path = [current]
        while current in parent:
            current = parent[current]
            # Adds current node to the path list
            path.append(current)
        path.reverse()
        # Reverses the list to get the path in the order of start to finish 
        return path
    
    row, col = current
    # All possible moves from the current location
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        r, c = row + dr, col + dc
        # Checking if moves are possible 
        if r < 0 or c < 0 or r >= len(maze) or c >= len(maze[0]) or maze[r][c] == 1 or (r, c) in visited:
            continue
        parent[(r, c)] = current
        queue.append((r, c))
        #print("Total nodes visited ", len(visited))
    
    return bfs(maze, start, goal, queue, visited, parent)


def main():
   # Takes an imputted filename and coverts it into a 1 and 0 maze form
   filename = input("Enter the name of your file ")
   with open(filename) as f:
                contents = f.read()
                maze = contents.replace('#','1').replace('-', '0')
                maze = [[int(i) for i in line.split()] for line in maze.split('\n')]


# Finds the start and end location of the inputted maze
   for i in range(len(maze[0])):
            if maze[0][i] == 0:
                start = (0,i)
            
   for i in range(len(maze[0])):
            if maze[len(maze)-1][i] == 0:
                goal = (len(maze)-1,i)
   start_time = time.time()
   path = bfs(maze, start, goal)
   print("--- %s seconds ---" % (time.time() - start_time))
   # Time import used either side of the function call to time just the algorithm speed
   print("The length of the chose path: ", len(path),"And the shorest path: ", path)


if __name__ == "__main__":
 main()