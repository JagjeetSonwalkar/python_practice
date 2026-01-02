
class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    # insert the node
    def insert(self, data):
        data = str(data)
        
        if self.root is None:
            self.root = Node(data)
            return 
        
        current_node = self.root

        while True:
            if data == current_node.data:
                return
            
            elif data < current_node.data:
                if current_node.left is None:
                    current_node.left = Node(data)
                    return
                current_node = current_node.left
            
            else:
                if current_node.right is None:
                    current_node.right = Node(data)
                    return
                current_node = current_node.right
    
    # display BT - inorder
    def inorder(self, root = None):
        if root is None:
            root = self.root
        if root is None:
            return
        
        if root.left:
            self.inorder(root.left)
        print(f"({root.data})", end=" ")
        if root.right:
            self.inorder(root.right)

def main():
    tree = BinaryTree()

    tree.insert(10)
    tree.insert(20)
    tree.insert(10)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)
    tree.insert("jack")

    tree.inorder()



if __name__ == "__main__":
    main()