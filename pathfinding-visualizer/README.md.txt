 Pathfinding Visualizer

An interactive **Pathfinding Visualizer** built with **Python** and **Pygame**, showcasing how algorithms like **A\*** and **Dijkstra's Algorithm** find the shortest path between two points.

This project demonstrates skills in:
- Algorithm design
- Data structures
- Software architecture
- Real-time visualization using Pygame

---

Features

-  Interactive grid with real-time animation  
-  Draw barriers, start and end nodes  
-  Visualize both **A\*** and **Dijkstra's Algorithm**  
-  Reset grid anytime with a single key  
-  On-screen instructions for easy use  

---

Controls

| Action | Key / Mouse |
|--------|--------------|
| Set Start, End, or Walls | **Left Click** |
| Erase Node | **Right Click** |
| Run A\* Algorithm | **SPACE** |
| Run Dijkstra's Algorithm | **D** |
| Clear Grid | **C** |
| Exit Program | **Close the Window (X)** |

---

Project Structure

pathfinding-visualizer/
│
├── main.py # Main game loop, event handling, UI
├── node.py # Node class (grid cells)
├── algorithms.py # A* and Dijkstra's algorithm logic
├── utils.py # Helper functions (heuristics, path reconstruction)
└── README.md # Documentation

Make sure you have Python 3.10+ and pygame installed.

How It Works

The program uses a grid-based environment where each node (cell) can be:

Empty (walkable)

Wall (blocked)

Start or End points

Algorithms like A* and Dijkstra traverse the grid step-by-step.

Each step is visualized in real-time:

Green → Open nodes (being explored)

Red → Closed nodes (already checked)

Purple → Final shortest path


Algorithms Used

A* Algorithm

Combines Dijkstra’s Algorithm and a heuristic (Manhattan distance) to efficiently find the shortest path.

Formula:

f(n) = g(n) + h(n)


g(n) = cost from start to node

h(n) = estimated cost from node to end (Manhattan distance)

Dijkstra's Algorithm

Explores all possible paths equally, without using a heuristic.
It guarantees the shortest path but is generally slower than A*.

License

This project is open-source and available under the MIT License

