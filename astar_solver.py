import timeit

class PuzzleState:
    def __init__(self, state, parent, move, depth, cost, key):
        self.state = state  
        self.parent = parent  
        self.move = move  
        self.depth = depth  
        self.cost = cost 
        self.key = key  
        if self.state:
            self.map = ''.join(str(e) for e in self.state)  

    def __eq__(self, other):
        return self.map == other.map

    def __lt__(self, other):
        return self.key < other.key



GoalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
GoalNode = None  
NodesExpanded = 0  
MaxSearchDeep = 0  


values = [
    [0, 1, 2, 1, 2, 3, 2, 3, 4],
    [1, 0, 1, 2, 1, 2, 3, 2, 3],
    [2, 1, 0, 3, 2, 1, 4, 3, 2],
    [1, 2, 3, 0, 1, 2, 1, 2, 3],
    [2, 1, 2, 1, 0, 1, 2, 1, 2],
    [3, 2, 1, 2, 1, 0, 3, 2, 1],
    [2, 3, 4, 1, 2, 3, 0, 1, 2],
    [3, 2, 3, 2, 1, 2, 1, 0, 1],
    [4, 3, 2, 3, 2, 1, 2, 1, 0],
]


def heuristic(state):
    return sum(values[i][state.index(i)] for i in range(len(state)))



def astar(startState):
    global GoalNode, MaxSearchDeep
    openSet = [PuzzleState(startState, None, None, 0, 0, heuristic(startState))]
    visited = set()
    MaxFrontier = 0  

    while openSet:
        openSet.sort()
        current = openSet.pop(0)
        visited.add(current.map)

        if current.state == GoalState:
            GoalNode = current
            return MaxFrontier

        for neighbor in subNodes(current):
            if neighbor.map not in visited:
                neighbor.key = neighbor.depth + heuristic(neighbor.state)
                openSet.append(neighbor)
                visited.add(neighbor.map)
                MaxSearchDeep = max(MaxSearchDeep, neighbor.depth)

        
        MaxFrontier = max(MaxFrontier, len(openSet))

    return MaxFrontier



def subNodes(node):
    global NodesExpanded
    NodesExpanded += 1

    neighbors = []
    for direction in range(1, 5):  
        new_state = move(node.state, direction)
        if new_state:
            neighbors.append(
                PuzzleState(new_state, node, direction, node.depth + 1, node.cost + 1, 0)
            )
    return neighbors



def move(state, direction):
    newState = state[:]
    index = newState.index(0)  

    
    swaps = {
        0: {2: 3, 4: 1},
        1: {2: 4, 3: 0, 4: 2},
        2: {2: 5, 3: 1},
        3: {1: 0, 2: 6, 4: 4},
        4: {1: 1, 2: 7, 3: 3, 4: 5},
        5: {1: 2, 2: 8, 3: 4},
        6: {1: 3, 4: 7},
        7: {1: 4, 3: 6, 4: 8},
        8: {1: 5, 3: 7},
    }

    
    if direction in swaps.get(index, {}):
        swap_with = swaps[index][direction]
        newState[index], newState[swap_with] = newState[swap_with], newState[index]
        return newState
    return None



def main():
    global GoalNode
    startState = [1, 8, 2, 0, 4, 3, 7, 6, 5]
    start = timeit.default_timer()
    MaxFrontier = astar(startState)
    stop = timeit.default_timer()

    moves = []
    while startState != GoalNode.state:
        moves.insert(0, {1: "Up", 2: "Down", 3: "Left", 4: "Right"}[GoalNode.move])
        GoalNode = GoalNode.parent

    result = (
        f"Start State: {startState}\n"
        f"Path: {moves}\n"
        f"Cost: {len(moves)}\n"
        f"Nodes Expanded: {NodesExpanded}\n"
        f"Max Search Depth: {MaxSearchDeep}\n"
        f"Max Frontier: {MaxFrontier}\n"
        f"Running Time: {format(stop - start, '.8f')} seconds\n\n\n"
    )

    
    with open("a_star_output.txt", "a") as file:
        file.write(result)


if __name__ == '__main__':
    main()
