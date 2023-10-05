#!/usr/bin/python3
'''
     a method that determines if all the boxes can be opened
'''


def canUnlockAll(boxes):

    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True  # The first box is unlocked initially

    stack = [0]  # Start with the first box in the stack

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
