import math
from queue import PriorityQueue

class Node:
    def _init_(self, name, actions=None, parent=None):
        self.name = name
        self.actions = actions if actions else []
        self.parent = parent
        self.g_cost = 0  # Cost from the start node to this node
        self.h_cost = 0  # Heuristic cost from this node to the goal node

def astar():
    initialState = 'C'
    goalState = 'B'

    def heuristic(node_name):
        # Define your heuristic function here.
        # For example, you can use straight-line distance between nodes as a heuristic.
        heuristic_values = {
            'A': 3,
            'B': 0,
            'C': 5,
            'D': 7,
            'E': 4,
            'F': 2,
            'G': 5
        }
        return heuristic_values[node_name]

    graph = {
        'A': Node('A', [('B', 6), ('C', 9), ('E', 1)]),
        'B': Node('B', [('A', 6), ('D', 3), ('E', 4)]),
        'C': Node('C', [('A', 9), ('F', 2), ('G', 3)]),
        'D': Node('D', [('B', 3), ('E', 5), ('F', 7)]),
        'E': Node('E', [('A', 1), ('B', 4), ('D', 5), ('F', 6)]),
        'F': Node('F', [('C', 2), ('E', 6), ('D', 7)]),
        'G': Node('G', [('C', 3)])
    }

    frontier = PriorityQueue()
    frontier.put((0, initialState))
    explored = set()

    while not frontier.empty():
        currentCost, currentNode = frontier.get()

        if currentNode == goalState:
            return reconstruct_path(graph, currentNode)

        if currentNode in explored:
            continue

        explored.add(currentNode)

        for child in graph[currentNode].actions:
            childNode, stepCost = child
            if childNode not in explored:
                new_g_cost = graph[currentNode].g_cost + stepCost
                new_h_cost = heuristic(childNode)
                priority = new_g_cost + new_h_cost
                frontier.put((priority, childNode))
                graph[childNode].parent = currentNode
                graph[childNode].g_cost = new_g_cost

    return None  # If the goal state is not reachable

def reconstruct_path(graph, goal_node):
    path = []
    current_node = goal_node
    while current_node is not None:
        path.insert(0, current_node)
        current_node = graph[current_node].parent
    return path

solution = astar()
if solution:
    print("Path found:", solution)
    print("Total cost:", len(solution) - 1)
else:
    print("Path not found")