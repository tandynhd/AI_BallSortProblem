from collections import deque


def create_node(state,path_cost, depth):
    return (state, path_cost, depth)


def print_solution(n):
    r = deque()
    while n is not None:
        r.appendleft(n[0])
        n = n[1]
    for s in r:
        print(s)


def isnotX(x):
    if x != 'X':
        return True
    else:
        return False

def is_empty(stack):
    for i in range(4):
        if stack[i] == 'X':
            return True
    return False

def hasNothing(stack):
    checker = 0
    for i in range(4):
        if stack[i]=='X':
            checker+=1
    
    if checker == 4:
        return True
    else:
        False
