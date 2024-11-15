import timeit
from collections import deque

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
        return self.map < other.map

    def __str__(self):
        return str(self.map)

GoalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
GoalNode = None
NodesExpanded = 0
MaxSearchDeep = 0
MaxFrontier = 0

def bfs(startState):
    global MaxFrontier, GoalNode, MaxSearchDeep
    boardVisited = set()
    Queue = deque([PuzzleState(startState, None, None, 0, 0, 0)])

    while Queue:
        node = Queue.popleft()
        boardVisited.add(node.map)
        if node.state == GoalState:
            GoalNode = node
            return Queue
        possiblePaths = subNodes(node)
        for path in possiblePaths:
            if path.map not in boardVisited:
                Queue.append(path)
                boardVisited.add(path.map)
                if path.depth > MaxSearchDeep:
                    MaxSearchDeep = MaxSearchDeep + 1
        if len(Queue) > MaxFrontier:
            MaxFrontier = len(Queue)

def subNodes(node):
    global NodesExpanded
    NodesExpanded += 1
    nextPaths = [
        PuzzleState(move(node.state, 1), node, 1, node.depth + 1, node.cost + 1, 0),
        PuzzleState(move(node.state, 2), node, 2, node.depth + 1, node.cost + 1, 0),
        PuzzleState(move(node.state, 3), node, 3, node.depth + 1, node.cost + 1, 0),
        PuzzleState(move(node.state, 4), node, 4, node.depth + 1, node.cost + 1, 0),
    ]
    return [path for path in nextPaths if path.state]

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
    bfs(startState)
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
