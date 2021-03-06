class TreeNode():
    def __init__(self, val):
        self._val = val
        self._left = None
        self._right = None

    def set_val(self, val):
        self._val = val

    def __str__(self):
        return str(self._val)

    def to_str(self):
        return str(self._val)

    def insert_left(self, left):
        self._left = left

    def insert_right(self, right):
        self._right = right


class Tree():
    def populate(self, node, val):
        if val == 1:
            return

        left_node = TreeNode("L_" + str(val - 1))
        right_node = TreeNode("R_" + str(val - 1))
        node.insert_left(left_node)
        self.populate(left_node, val - 1)
        node.insert_right(right_node)
        self.populate(right_node, val - 1)

    def build_tree(self, depth=1):
        self._root = TreeNode("Root_" + str(depth))
        self.populate(self._root, depth)
        return self._root

    def str_internal(self, node):
        return (node.to_str() + (
            " (" + (self.str_internal(node._left) if node._left else "")+ ", " +
            (self.str_internal(node._right) if node._right else "")+ ")" if node._left or node._right else ""))

    def __str__(self):
        return self.str_internal(self._root)

    def print_preorder(self):
        return self.__str__()

    def print_postorder_iterative(self):
        stack = []
        output = ""

        node = self._root
        while True:
            if node:
                if not (stack and node == stack[-1][0]):
                    stack.append([node, False, False])

                if not stack[-1][1]:
                    node = node._left
                    stack[-1][1] = True
                    continue

                elif not stack[-1][2]:
                    stack[-1][2] = True
                    node = node._right
                    continue

                output += node.to_str() + ", "
                stack.pop()

            if not stack:
                return output[0: -2]

            node = stack[-1][0]

    def print_preorder_iterative(self):
        stack = []
        output = ""

        node = self._root
        while True:
            if node:
                stack.append(node._right)
                stack.append(node._left)
                output += str(node) + ", "

            if not stack:
                return output[0:-2]

            node = stack.pop()

    def print_inorder_iterative(self):
        stack = []
        output = ""

        node = self._root
        while True:
            if node:
                if stack and node == stack[-1]:
                    output += str(node) + ", "
                    stack.pop()
                    node = node._right
                    continue

                stack.append(node)
                node = node._left
                continue

            if not stack:
                return output[0: -2]

            node = stack[-1]

if __name__ == "__main__":
    tree = Tree()
    tree.build_tree(4)
    print "Preorder: ", tree
    print "Postorder iterative: ", tree.print_postorder_iterative()
    print "Preorder iterative: ", tree.print_preorder_iterative()
    print "In order iterative: ", tree.print_inorder_iterative()
