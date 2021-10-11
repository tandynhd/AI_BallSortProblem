from heapq import heappush, heappop, heapify
from utils import create_node
depth = 0


def index(f, s):
    return next((i for i, x in enumerate(f) if x[1][0] == s), -1)


def uniform_cost_graph_search(problem):
    initial_node = create_node(problem.initialStack(), None, 0)
    frontier = [(0, initial_node)]
    explored = set()
    n_visits = 0
    while True:
        if not frontier:
            return (None, n_visits)
        else:
            n_visits += 1
            _, node = heappop(frontier)
            state, path_cost, depth = node
            explored.add(state)
            if problem.is_goal(state):
                return (node, n_visits)
            else:
                for succ, cost in problem.successors(state):
                    child_cost = path_cost + cost
                    child = create_node(succ, child_cost, depth + 1)
                    if succ not in explored:
                        idx = index(frontier, succ)
                        if idx < 0:
                            heappush(frontier, (child_cost, child))
                        else:
                            _, existing = frontier[idx]
                            if existing[3] > child_cost:
                                frontier[idx] = (child_cost, child)
                                heapify(frontier)
