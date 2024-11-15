import timeit

# PuzzleState class to define the state of the puzzle
class PuzzleState:
    def __init__(self, state, parent, move, depth, cost, key):
        self.state = state  # Current state of the puzzle
        self.parent = parent  # Parent node
        self.move = move  # Move that led to this state
        self.depth = depth  # Depth in the search tree
        self.cost = cost  # Cost to reach this state
        self.key = key  # Heuristic value
        if self.state:
            self.map = ''.join(str(e) for e in self.state)  # Unique identifier for the state

    def __eq__(self, other):
        return self.map == other.map

    def __lt__(self, other):
        return self.key < other.key


# Goal state for the 8-puzzle problem
GoalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
GoalNode = None  # Will store the node corresponding to the solution
NodesExpanded = 0  # Counter for expanded nodes
MaxSearchDeep = 0  # Maximum depth reached during the search

# Predefined heuristic values for the Manhattan distance calculation
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

# Heuristic function (Manhattan distance)
def heuristic(state):
    return sum(values[i][state.index(i)] for i in range(len(state)))


# A* Search algorithm
def astar(startState):
    global GoalNode, MaxSearchDeep
    openSet = [PuzzleState(startState, None, None, 0, 0, heuristic(startState))]
    visited = set()

    while openSet:
        openSet.sort()
        current = openSet.pop(0)
        visited.add(current.map)

        if current.state == GoalState:
            GoalNode = current
            return

        for neighbor in subNodes(current):
            if neighbor.map not in visited:
                neighbor.key = neighbor.depth + heuristic(neighbor.state)
                openSet.append(neighbor)
                visited.add(neighbor.map)
                MaxSearchDeep = max(MaxSearchDeep, neighbor.depth)


# Generate all possible next states from the current state
def subNodes(node):
    global NodesExpanded
    NodesExpanded += 1

    neighbors = []
    for direction in range(1, 5):  # 1: Up, 2: Down, 3: Left, 4: Right
        new_state = move(node.state, direction)
        if new_state:
            neighbors.append(
                PuzzleState(new_state, node, direction, node.depth + 1, node.cost + 1, 0)
            )
    return neighbors


# Move the blank tile (0) in the specified direction
def move(state, direction):
    newState = state[:]
    index = newState.index(0)  # Find the position of the blank tile (0)

    # Define the valid swaps based on the current position of the blank tile
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

    # Check if the direction is valid for the current position
    if direction in swaps.get(index, {}):
        swap_with = swaps[index][direction]
        newState[index], newState[swap_with] = newState[swap_with], newState[index]
        return newState
    return None


# Main function to run the A* algorithm
def main():
    global GoalNode
    startState = [1, 8, 2, 0, 4, 3, 7, 6, 5]
    start = timeit.default_timer()
    astar(startState)
    stop = timeit.default_timer()

    moves = []
    while startState != GoalNode.state:
        moves.insert(0, {1: "Up", 2: "Down", 3: "Left", 4: "Right"}[GoalNode.move])
        GoalNode = GoalNode.parent

    print("path:", moves)
    print("cost:", len(moves))
    print("nodes expanded:", NodesExpanded)
    print("search depth:", GoalNode.depth)
    print("max search depth:", MaxSearchDeep)
    print("running time:", format(stop - start, '.8f'))


if __name__ == '__main__':
    main()
