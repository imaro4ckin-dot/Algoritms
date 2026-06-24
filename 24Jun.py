import heapq
from collections import defaultdict
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValid(root: TreeNode):
    def validate(node, low=float('-inf'), high=float('inf')):

        if not node:
            return True

        if node.val <= low or node.val >= high:
            return False

        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))

    return validate(root)




if __name__ == "__main__":

    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    print(f"Test 1 (Simple Valid): {isValid(root1)} | Expected: True")


    root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(f"Test 2 (Simple Invalid): {isValid(root2)} | Expected: False")

    root3 = TreeNode(5, TreeNode(4, None, TreeNode(7)), TreeNode(6))
    print(f"Test 3 (Deep Violation Trap): {isValid(root3)} | Expected: False")


    root4 = None
    print(f"Test 4 (Empty Tree): {isValid(root4)} | Expected: True")


    root5 = TreeNode(10)
    print(f"Test 5 (Single Node): {isValid(root5)} | Expected: True")

    root6 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    print(f"Test 6 (Right-Skewed Valid): {isValid(root6)} | Expected: True")


    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


    def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root


    # --- Test Data & Driver Code ---
    if __name__ == "__main__":
        # We will build the following valid Binary Search Tree:
        #
        #          6
        #        /   \
        #       2     8
        #      / \   / \
        #     0   4 7   9
        #        / \
        #       3   5

        # 1. Instantiate the nodes from bottom to top so we can easily reference them
        node3 = TreeNode(3)
        node5 = TreeNode(5)
        node4 = TreeNode(4, node3, node5)
        node0 = TreeNode(0)
        node2 = TreeNode(2, node0, node4)

        node7 = TreeNode(7)
        node9 = TreeNode(9)
        node8 = TreeNode(8, node7, node9)

        root_node = TreeNode(6, node2, node8)


        # Test 1: Split at the root (One on left, one on right)

        result1 = lowestCommonAncestor(root_node, node2, node8)
        print(f"Test 1 (Split at Root): {result1.val} | Expected: 6")

        # Test 2: Deep split on the left side

        result2 = lowestCommonAncestor(root_node, node3, node5)
        print(f"Test 2 (Deep Left Split): {result2.val} | Expected: 4")

        # Test 3: Deep split on the right side

        result3 = lowestCommonAncestor(root_node, node7, node9)
        print(f"Test 3 (Deep Right Split): {result3.val} | Expected: 8")

        # Test 4: One node is the ancestor of the other

        result4 = lowestCommonAncestor(root_node, node2, node4)
        print(f"Test 4 (Node is Ancestor): {result4.val} | Expected: 2")

        # Test 5: Root is one of the target nodes

        result5 = lowestCommonAncestor(root_node, root_node, node5)
        print(f"Test 5 (Root is Target): {result5.val} | Expected: 6")


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:

            graph = defaultdict(list)
            for u, v, w in times:
                graph[u].append((v, w))


            pq = [(0, k)]


            dist = {}


            while pq:
                time, node = heapq.heappop(pq)


                if node in dist:
                    continue


                dist[node] = time


                for neighbor, weight in graph[node]:
                    if neighbor not in dist:
                        heapq.heappush(pq, (time + weight, neighbor))


            if len(dist) == n:
                return max(dist.values())


            return -1


if __name__ == "__main__":
    # Test 1: Standard Network

    times1 = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n1, k1 = 4, 2
    print(f"Test 1 (Standard): {networkDelayTime(times1, n1, k1)} | Expected: 2")

    # Test 2: Unreachable Node

    times2 = [[1, 2, 1]]
    n2, k2 = 3, 1
    print(f"Test 2 (Disconnected): {networkDelayTime(times2, n2, k2)} | Expected: -1")

    # Test 3: Multiple Paths (Testing the Min-Heap)

    times3 = [[1, 2, 5], [1, 3, 2], [3, 2, 1]]
    n3, k3 = 3, 1
    print(f"Test 3 (Shortest Path Bypass): {networkDelayTime(times3, n3, k3)} | Expected: 3")

    # Test 4: Linear Path (Essentially a linked list)

    times4 = [[1, 2, 10], [2, 3, 10], [3, 4, 10]]
    n4, k4 = 4, 1
    print(f"Test 4 (Linear Chain): {networkDelayTime(times4, n4, k4)} | Expected: 30")

    # Test 5: Single Node Edge Case

    times5 = []
    n5, k5 = 1, 1
    print(f"Test 5 (Single Node): {networkDelayTime(times5, n5, k5)} | Expected: 0")