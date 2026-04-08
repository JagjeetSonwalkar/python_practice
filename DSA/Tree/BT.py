class BinaryTreeNode:
    def __init__(self, data = None):
        self.left = None
        self.data = data
        self.right = None
    
class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def insert(self, data, current_node = None):
        if self.root is None:
            self.root = BinaryTreeNode(data)
            self.size += 1
            return True
        
        if current_node is None:
            current_node = self.root
        
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = BinaryTreeNode(data)
                self.size += 1
                return True
            else:
                self.insert(data, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = BinaryTreeNode(data)
                self.size += 1
                return True
            else:
                self.insert(data, current_node.right)
    
    def preorder(self, current_node = None):
        if self.root == None:
            print("Tree is Empty")
            return
    
        if current_node == None:
            current_node = self.root
        
        print(f"({current_node.data})")
        if current_node.left:
            self.preorder(current_node.left)
        if current_node.right:
            self.preorder(current_node.right)
    
    def inorder(self, current_node = None):
        if self.root == None:
            print("Tree is Empty")
            return
    
        if current_node == None:
            current_node = self.root

        if current_node.left:
            self.inorder(current_node.left)
        print(f"({current_node.data})")
        if current_node.right:
            self.inorder(current_node.right)
    
    def postorder(self, current_node = None):
        if self.root == None:
            return False
        
        if current_node == None:
            current_node = self.root
        
        if current_node.left:
            self.postorder(current_node.left)
        if current_node.right:
            self.postorder(current_node.right)
        print(f"({current_node.data})")
    
    def search(self, data, current_node = None, parent_node = None):
        if self.root == None:
            print("Tree is Empty")
            return False
    
        if current_node == None and parent_node == None:
            current_node = self.root
        
        if current_node == None:
            return False
        
        if data == current_node.data:
            return current_node.data

        if data < current_node.data:
            return self.search(data, current_node.left, current_node)
        else:
            return self.search(data, current_node.right, current_node)


    
     

def main():
    tree = BinaryTree()

    tree.insert(10)
    tree.insert(20)
    tree.insert(5)
    tree.insert(0)
    tree.insert(2)
    tree.insert(55)

    tree.preorder()

    print()

    tree.inorder()

    print()

    tree.postorder()

    print()

    ret = tree.search(2)
    if ret:
        print(f"Data is found")
    else:
        print("Data is not found!")

if __name__ == "__main__":
    main()
