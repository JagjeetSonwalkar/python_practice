
# Node of General Tree
class GeneralTreeNode:
    def __init__(self, data):
        self.data = data
        self.first_child = None     # point to first chid
        self.next_siblings = None   # points to next siblings

class GeneralTree:
    def __init__(self):
        self.root = None
        self.count_nodes = 0

    # insert the new node
    def insert(self, data):
        new_node = GeneralTreeNode(data)
        
        # create root
        if self.root is None:
            self.root = new_node
            self.count_nodes += 1
            return True
        
        if self.root.first_child is None:
            self.root.first_child = new_node
            self.count_nodes += 1
            return True
        else:
            temp = self.root.first_child

            while temp.next_siblings is not None:
                temp = temp.next_siblings
            temp.next_siblings = new_node

            self.count_nodes += 1
            return True
    
    # get root node value:
    def get_root(self):
        return self.root.data

    # display tree
    def pre_order(self, node = None):
        if node is None:
            node = self.root
        
        if node is None:
            return
        
        print(f"('{node.data}')",end=" ")

        child = node.first_child
        while child is not None:
            self.pre_order(child)
            child = child.next_siblings

    # count total nodes in tree
    def size(self):
        return self.count_nodes

def main():
    tree = GeneralTree()

    tree.insert(10)
    tree.insert(20)
    tree.insert(10)
    tree.insert(20)

    tree.pre_order()
    print()

    print("The root node is:",tree.get_root())

    print("Total nodes in tree is:",tree.size())

if __name__ == "__main__":
    main()
        



