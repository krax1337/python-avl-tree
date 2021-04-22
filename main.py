from tree import AVLTree

if __name__ == '__main__':
    tree1 = AVLTree()
    tree1.insert(10)
    tree1.insert(15)
    tree1.insert(14)
    tree1.insert(5)
    tree1.print_beauty()
    tree1.print_classic()


    tree2 = AVLTree()
    tree2.insert(10)
    tree2.insert(9)
    tree2.insert(8)
    tree2.insert(7)
    tree2.insert(6)
    tree2.print_beauty()
    tree2.print_classic()