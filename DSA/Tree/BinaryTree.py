
class BinaryTreeNode:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.count_node = 0
    
    # insert the node
    def insert(self, data):
        new_node = BinaryTreeNode(data)

        if self.root is None:
            self.root = new_node
            self.count_node += 1
            return True
        else:
            self._insert_recervsion(self.root, new_node)

    def _insert_recervsion(self, current, new_node):
        if current.left is None:
            current.left = new_node
            self.count_node += 1
            return True
        elif current.right is None:
            current.right = new_node
            self.count_node += 1
            return True
        else:
            inserted = self._insert_recervsion(current.left, new_node)
            if inserted:
                return True
            else:
                self._insert_recervsion(current.right, new_node)
    
    # display tree in inorder way
    def inorder(self, node = None):
        if node is None:
            node = self.root
        
        if node is None:
            return
        
        if node.left:
            self.inorder(node.left)
        print(f"('{node.data}')",end = "")
        if node.right:
            self.inorder(node.right)
    
    
def main():
    tree = BinaryTree()

    tree.insert(10)
    tree.insert(20)
    tree.insert(30)

    tree.inorder()


if __name__ == "__main__":
    main()


        
