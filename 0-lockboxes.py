#!/usr/bin/python3
"""
Module 0-lockboxes
"""

def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.
    :param boxes: List of lists, where each sublist represents keys contained in the box.
    :return: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    if n == 0:
        return False

    # Initialize
    visited = set()
    queue = [0]  # Start with box 0 (first box)
    visited.add(0)

    # BFS traversal
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and key not in visited:
                visited.add(key)
                queue.append(key)

    # Check if all boxes are visited
    return len(visited) == n
