#!/uer/bin/python3
"""
Module 0-lockboxes
"""


def canUnlockAll(boxes):
        """
        Determine if all the boxes can be opened
        :param boxes: List of lists, where each sublist represents keys contained in the box
        :return: True if all boxes can be opened, else False
        """
        n = len(boxes)
        if n == 0:
            return False


        visited = set()
        queue = [0]
        visited.add(0)

        while queue:
            current_box = queue.pop(0)
            for key in boxes[current_box]:
                if key < n and key not in visited:
                    visited.add(key)
                    queue.append(key)

        return len(visited) == n
