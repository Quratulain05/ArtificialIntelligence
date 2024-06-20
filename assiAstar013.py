import math

class Node:
    def __init__(self, state, parent, actions, totalCost, heuristic):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost
        self.heuristic = heuristic

def findMin(frontier):
    minV = math.inf
    node = ''
    for key, value in frontier.items():
        if value[1] < minV:
            minV = value[1]
            node = key
    return node

def Astar():
    initialState = 'Arad'
    goalState = 'Bucharest'

    graph = {
    'Arad': Node('Arad', None, [('Sibiu', 140)], 0, 366),
    'Sibiu': Node('Sibiu', None, [('Rimnicu', 80), ('Fagaras', 99)], 140, 253),
    'Rimnicu': Node('Rimnicu', None, [('Pitesti', 97), ('Craiova', 146)], 220, 193),
    'Pitesti': Node('Pitesti', None, [('Bucharest', 101)], 317, 98),
    'Fagaras': Node('Fagaras', None, [('Bucharest', 211)], 239, 178),
    'Craiova': Node('Craiova', None, [('Pitesti', 138), ('Drobeta', 120)], 366, 160),
    'Drobeta': Node('Drobeta', None, [('Craiova', 120), ('Mehadia', 75)], 486, 242),
    'Mehadia': Node('Mehadia', None, [('Lugoj', 70)], 561, 241),
    'Lugoj': Node('Lugoj', None, [('Timisoara', 111)], 631, 244),
    'Timisoara': Node('Timisoara', None, [], 742, 329),
    'Bucharest': Node('Bucharest', None, [], 418, 0),
}



    frontier = {}
    heuristicCost = graph[initialState].heuristic
    frontier[initialState] = (None, heuristicCost)
    explored = {}

    while frontier:
        currentNode = findMin(frontier)
        print(currentNode)
        del frontier[currentNode]

        if currentNode == goalState:
            return reconstructPath(graph, initialState, goalState)

        currentCost = graph[currentNode].totalCost
        explored[currentNode] = currentCost

        for childState, cost in graph[currentNode].actions:
            childCost = currentCost + cost

            if childState in explored and explored[childState] <= childCost:
                continue

            heuristicCost = graph[childState].heuristic
            totalCost = childCost + heuristicCost

            if childState not in frontier or totalCost < frontier[childState][1]:
                graph[childState].parent = currentNode
                frontier[childState] = (currentNode, totalCost)

    return None

def reconstructPath(graph, initialState, goalState):
    path = []
    currentNode = goalState
    while currentNode is not None:
        path.insert(0, currentNode)
        currentNode = graph[currentNode].parent
    return path

solution = Astar()
print(solution)
