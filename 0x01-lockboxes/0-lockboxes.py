#!/usr/bin/python3
'''
     a method that determines if all the boxes can be opened.
'''
def canUnlockAll(boxes):

    ''''
        box visit method
    '''
    def dfs(box_index, visited):

        visited[box_index] = True
        for key in boxes[box_index]:
            if not visited[key]:
                dfs(key, visited)

    n = len(boxes)
    visited = [False] * n
    visited[0] = True

    dfs(0, visited)

    return all(visited)
