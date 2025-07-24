from collections import deque
from itertools import combinations

# Time dictionary
times = {
    'Amogh': 5,
    'Ameya': 10,
    'Grandmother': 20,
    'Grandfather': 25
}

# Initial and goal states
initial_state = (frozenset(times.keys()), frozenset(), True, 0)
goal_state_set = frozenset(times.keys())

# Get successors
def get_successors(state):
    left, right, umbrella_left, elapsed = state
    successors = []

    if umbrella_left:
        # Two people go from left to right
        for pair in combinations(left, 2):
            new_left = left.difference(pair)
            new_right = right.union(pair)
            time = max(times[pair[0]], times[pair[1]])
            new_elapsed = elapsed + time
            if new_elapsed <= 60:
                successors.append((frozenset(new_left), frozenset(new_right), False, new_elapsed))
    else:
        # One person returns with umbrella
        for person in right:
            new_left = left.union({person})
            new_right = right.difference({person})
            time = times[person]
            new_elapsed = elapsed + time
            if new_elapsed <= 60:
                successors.append((frozenset(new_left), frozenset(new_right), True, new_elapsed))

    return successors

# BFS
def bfs():
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        left, right, umbrella_left, elapsed = state

        if right == goal_state_set and elapsed <= 60:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        for next_state in get_successors(state):
            queue.append((next_state, path + [state]))
    return None

# DFS
def dfs():
    stack = [(initial_state, [])]
    visited = set()

    while stack:
        state, path = stack.pop()
        left, right, umbrella_left, elapsed = state

        if right == goal_state_set and elapsed <= 60:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        for next_state in get_successors(state):
            stack.append((next_state, path + [state]))
    return None

# Output results
def print_path(path, title):
    print(f"\n{title}")
    if not path:
        print("No valid solution found.")
        return
    for step in path:
        left, right, umbrella, time = step
        print(f"Left: {sorted(left)}, Right: {sorted(right)}, Umbrella on {'Left' if umbrella else 'Right'}, Time: {time} min")
    print(f"Total Time: {path[-1][3]} minutes")

# Run and print both
print_path(bfs(), "BFS Solution")
print_path(dfs(), "DFS Solution")

