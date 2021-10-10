from __future__ import annotations
import queue
import random
import sys


class BinaryTree:
    def __init__(self, value: int):

        self.left = None
        self.right = None
        self.content = value

    """Insert element in tree"""
    def insert(self, value: int):

        if self.content is None:
            self.content = value
            return

        if value < self.content:
            self.left = self.__insert(self.left, value)
        elif value > self.content:
            self.right = self.__insert(self.right, value)

    def print(self):
        BinaryTree.print_subtree(self, 0)

#   func by yozn
    @staticmethod
    def print_subtree(node, level=0):
        if node is not None:
            BinaryTree.print_subtree(node.left, level + 1)
            #print(' ' * 4 * level + '>', node.content)
            if node.left is not None:
                print(' ' * (4 * level + 2) + "/")
            print(' ' * 4 * level, node.content)
            if node.right is not None:
                print(' ' * (4 * level + 2) + "\\")
            BinaryTree.print_subtree(node.right, level + 1)

    @staticmethod
    def __insert(node: BinaryTree, value: int):
        if node is None:
            return BinaryTree(value)
        else:
            node.insert(value)
            return node

    """InOrder: Left,Root,Right"""
    def inorder_traversal(self):
        return self._inorder_traversal(self, list())

    def _inorder_traversal(self, root: BinaryTree, elms: list[int]):
        if root:
            self._inorder_traversal(root.left, elms)
            elms.append(root.content)
            self._inorder_traversal(root.right, elms)
        return elms

    """PreOrder: Root,Left,Right"""
    def preorder_traversal(self):
        return self._preorder_traversal(self, list())

    def _preorder_traversal(self, root: BinaryTree, elms: list[int]):
        if root:
            elms.append(root.content)
            self._preorder_traversal(root.left, elms)
            self._preorder_traversal(root.right, elms)
        return elms

    """Postorder: Left,Right,Root"""
    def postorder_traversal(self):
        return self._postorder_traversal(self, list())

    def _postorder_traversal(self, root: BinaryTree, elms: list[int]):
        if root:
            self._postorder_traversal(root.left, elms)
            self._postorder_traversal(root.right, elms)
            elms.append(root.content)
        return elms

    def bfs_traversal(self):
        elms = list()
#       we will use this list as a queue
        q = list()
        q.append(self)

        while len(q) > 0:
            curr_elm = q.pop(0)
            elms.append(curr_elm.content)

            if curr_elm.left:
                q.append(curr_elm.left)
            if curr_elm.right:
                q.append(curr_elm.right)
        return elms


if __name__ == "__main__":
    SIZE = 16
    RANGE = SIZE*5

    if len(sys.argv) > 1:
        try:
            SIZE = int(sys.argv[1])
            RANGE = int(sys.argv[2])
        except:
            print("Invalid values %s:\nUsage: tree_traversals [tree_size] [tree_max_value]" % str(sys.argv[1:]))
            sys.exit(1)

    print("Creating tree of %d random values from 0 to %d (collisions will be voided)\n" % (SIZE, RANGE))
    tree = BinaryTree(random.randint(0, RANGE))
    for _ in range(SIZE):
        tree.insert(random.randint(0, RANGE))

    tree.print()

    print("DFS InOrder Traversal")
    print(tree.inorder_traversal())
    print("DFS PreOrder Traversal")
    print(tree.preorder_traversal())
    print("DFS PostOrder Traversal")
    print(tree.postorder_traversal())

    print("BFS Traversal")
    print(tree.bfs_traversal())
