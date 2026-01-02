# Tree

class TreeNode(self, data):
    self.left = None
    self.data = data
    self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        new_node = Node(data)

        if root is None:
            self.root = new_node
        else:
            self.insert_recursive(self.root, new_node)
    
    def insert_recursive(self,current, new_node):
        if current.left is None:
            current.left = new_node
        elif current.right is None:
            current.right = new_node
        else:
            if self.count_nodes(current.left) <= self.count_nodes(current.right):
                self.insert_recursive(current.left, new_node)
            else:
                self.insert_recursive(current.right, new_node)
    
    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

def main():

if __name__ == "__main__":
    main()