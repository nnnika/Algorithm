class Node(object):
    def __init__(self, item):
        self.elem = item
        self.left = None
        self.right = None


class Tree(object):
    """binary tree"""
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)

            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=" ")  # 打印根
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)

    def preorder(self, node):
        """前序遍历"""
        if node is None:
            return
        print(node.elem, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        """中序遍历"""
        if node is None:
            return
        self.inorder(node.left)
        print(node.elem, end=" ")
        self.inorder(node.right)

    def postorder(self, node):
        """后序遍历"""
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.elem, end=" ")


if __name__ == "__main__":
    tree = Tree()
    for i in range(1, 10):
        tree.add(i)
    tree.breadth_travel()
    print(" ")
    tree.preorder(tree.root)
    print(" ")
    tree.inorder(tree.root)
    print(" ")
    tree.postorder(tree.root)
    print(" ")

