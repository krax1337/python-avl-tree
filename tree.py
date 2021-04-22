from printer import printBTree


class AVLTree:

    def __init__(self):
        self.__root = None

    def insert(self, value):
        if self.__root is None:
            self.__root = _Node(value)
        else:
            self.__insert(value, self.__root)

    def print_beauty(self):
        if self.__root is None:
            raise ValueError('Firstly you have to initialize a tree')

        printBTree(self.__root, lambda n: (str(n.key), n.left_child, n.right_child))

    def print_classic(self):
        if self.__root is None:
            raise ValueError('Firstly you have to initialize a tree')

        return self.__print_classic(self.__root)

    def __print_classic(self, node):
        if node.left_child:
            self.__print_classic(node.left_child)
        print(f"(key: {node.key} ; height: {node.height})")
        if node.right_child:
            self.__print_classic(node.right_child)

    def __insert(self, value, node):

        if not node.key:
            node.key = value
        else:
            if value < node.key:
                if node.left_child is None:
                    node.left_child = _Node(value)
                    node.left_child.parent = node
                    self.__check_insertion(node.left_child)
                else:
                    self.__insert(value, node.left_child)
            elif value > node.key:
                if node.right_child is None:
                    node.right_child = _Node(value)
                    node.right_child.parent = node
                    self.__check_insertion(node.right_child)
                else:
                    self.__insert(value, node.right_child)

    def find(self, value):
        if self.__root is not None:
            return self.__find(value, self.__root)
        else:
            return False

    def __find(self, value, cur_node):
        if value < cur_node.key:
            if cur_node.left_child is None:
                return False
            return self.__find(value, cur_node.left_child)
        if value > cur_node.key:
            if cur_node.right_child is None:
                return False
            return self.__find(value, cur_node.right_child)
        elif value == cur_node.key:
            return True

    def __check_insertion(self, node, nodes=None):
        if node.parent is None:
            return

        if nodes is None:
            nodes = list()
        nodes = [node] + nodes

        left_height = self.__get_height(node.parent.left_child)
        right_height = self.__get_height(node.parent.right_child)

        if abs(left_height - right_height) > 1:
            nodes = [node.parent] + nodes
            self.__balance_node(nodes[0], nodes[1], nodes[2])
            return

        new_height = node.height + 1
        if new_height > node.parent.height:
            node.parent.height = new_height

        self.__check_insertion(node.parent, nodes)

    def __balance_node(self, parent, child_1, child_2):

        # Small right rotation
        if child_1 == parent.left_child and child_2 == child_1.left_child:
            self.__right_rotate(parent)
        # Big right rotation
        elif child_1 == parent.left_child and child_2 == child_1.right_child:
            self.__left_rotate(child_1)
            self.__right_rotate(parent)
        # Small left rotation
        elif child_1 == parent.right_child and child_2 == child_1.right_child:
            self.__left_rotate(parent)
        # Big left rotation
        elif child_1 == parent.right_child and child_2 == child_1.left_child:
            self.__right_rotate(child_1)
            self.__left_rotate(parent)

    def __right_rotate(self, z):
        sub_root = z.parent
        y = z.left_child
        t3 = y.right_child
        y.right_child = z
        z.parent = y
        z.left_child = t3
        if t3 != None: t3.parent = z
        y.parent = sub_root
        if y.parent == None:
            self.__root = y
        else:
            if y.parent.left_child == z:
                y.parent.left_child = y
            else:
                y.parent.right_child = y
        z.height = 1 + max(self.__get_height(z.left_child),
                           self.__get_height(z.right_child))
        y.height = 1 + max(self.__get_height(y.left_child),
                           self.__get_height(y.right_child))

    def __left_rotate(self, z):
        sub_root = z.parent
        y = z.right_child
        t2 = y.left_child
        y.left_child = z
        z.parent = y
        z.right_child = t2
        if t2 != None: t2.parent = z
        y.parent = sub_root
        if y.parent == None:
            self.__root = y
        else:
            if y.parent.left_child == z:
                y.parent.left_child = y
            else:
                y.parent.right_child = y
        z.height = 1 + max(self.__get_height(z.left_child),
                           self.__get_height(z.right_child))
        y.height = 1 + max(self.__get_height(y.left_child),
                           self.__get_height(y.right_child))

    # noinspection PyMethodMayBeStatic
    def __get_height(self, node):
        if node is None:
            return 0
        return node.height


class _Node:

    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.height = 1
        self.key = value
