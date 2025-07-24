from collections import deque

# Initial and goal states
initial_state = ('E', 'E', 'E', '_', 'W', 'W', 'W')
goal_state = ('W', 'W', 'W', '_', 'E', 'E', 'E')

def get_next_states(state):
    moves = []
    idx = state.index('_')
    state = list(state)

    # E can move right into '_'
    if idx > 0 and state[idx - 1] == 'E':
        new_state = state[:]
        new_state[idx], new_state[idx - 1] = new_state[idx - 1], new_state[idx]
        moves.append(tuple(new_state))

    # E can jump right over 1 into '_'
    if idx > 1 and state[idx - 2] == 'E' and state[idx - 1] != '_':
        new_state = state[:]
        new_state[idx], new_state[idx - 2] = new_state[idx - 2], new_state[idx]
        moves.append(tuple(new_state))

    # W can move left into '_'
    if idx < len(state) - 1 and state[idx + 1] == 'W':
        new_state = state[:]
        new_state[idx], new_state[idx + 1] = new_state[idx + 1], new_state[idx]
        moves.append(tuple(new_state))

    # W can jump left over 1 into '_'
    if idx < len(state) - 2 and state[idx + 2] == 'W' and state[idx + 1] != '_':
        new_state = state[:]
        new_state[idx], new_state[idx + 2] = new_state[idx + 2], new_state[idx]
        moves.append(tuple(new_state))

    return moves

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path
        visited.add(current)
        for next_state in get_next_states(current):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))
    return None

def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        current, path = stack.pop()
        if current == goal:
            return path
        visited.add(current)
        for next_state in get_next_states(current):
            if next_state not in visited:
                stack.append((next_state, path + [next_state]))
    return None

# Run BFS
print("BFS Solution Path:")
bfs_path = bfs(initial_state, goal_state)
if bfs_path:
    for step in bfs_path:
        print(step)
else:
    print("No solution found using BFS.")

# Run DFS
print("\nDFS Solution Path:")
dfs_path = dfs(initial_state, goal_state)
if dfs_path:
    for step in dfs_path:
        print(step)
else:
    print("No solution found using DFS.")

