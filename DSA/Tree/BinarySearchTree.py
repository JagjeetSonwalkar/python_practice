# Binary Search Tree

# BST Node
class BSTNode:
    def __init__(self, data):
        self.left = None
        self.data = data 
        self.right = None

# BST class
class BST:
    def __init__(self):
        self.root = None
        self.count_node = 0
    
    def insert(self, data, current_node = None):
        if self.root is None:
            self.root = BSTNode(data)
            self.count_node += 1
            return True
        
        if current_node is None:
            current_node = self.root
        
        if current_node.data == data:
            return -1
        
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = BSTNode(data)
                self.count_node += 1
                return True
            else:
                return self.insert(data, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = BSTNode(data)
                self.count_node += 1
                return True
            else:
                return self.insert(data, current_node.right)
    
    def remove(self, target_value, current_node=None, parent_node=None):
        # Initial call only
        if current_node is None and parent_node is None:
            current_node = self.root

        # Data not found
        if current_node is None:
            return -1

        if target_value < current_node.data:
            return self.remove(target_value, current_node.left, current_node)

        elif target_value > current_node.data:
            return self.remove(target_value, current_node.right, current_node)

        else:
            removed_value = current_node.data

            # Case 1: Node has two children
            if current_node.left and current_node.right:
                successor_parent = current_node
                successor_node = current_node.right

                while successor_node.left:
                    successor_parent = successor_node
                    successor_node = successor_node.left

                current_node.data = successor_node.data

                # Remove successor (actual physical deletion)
                self.remove(successor_node.data, successor_node, successor_parent)

            # Case 2: Node has one or no child
            else:
                replacement_node = (
                    current_node.left
                    if current_node.left
                    else current_node.right
                )

                if parent_node is None:
                    self.root = replacement_node
                elif parent_node.left == current_node:
                    parent_node.left = replacement_node
                else:
                    parent_node.right = replacement_node

                self.count_node -= 1

            return removed_value
    
    def clear(self, current_node = None):
        if current_node is None:
            current_node = self.root
            if current_node is None:
                return
        
        if current_node.left:
            self.clear(current_node.left)
        if current_node.right:
            self.clear(current_node.right)
        
        current_node.left = None
        current_node.right = None

        if current_node == self.root:
            self.root = None

    def search(self, target_value, current_node = None, is_root_call = True):
        if is_root_call:
            current_node = self.root
        
        if current_node is None:
            return -1
        
        if target_value == current_node.data:
            return current_node.data
        if target_value < current_node.data:
            return self.search(target_value, current_node.left, False)
        else:
            return self.search(target_value, current_node.right, False)
    
    def update(self, current_value,  update_value, current_node = None, is_root_call = True):
        if is_root_call:
            current_node = self.root
        
        if current_node is None:
            return -1
        
        if current_value == current_node.data:
            current_node.data = update_value
            return True
        if current_value < current_node.data:
            return self.update(current_value,  update_value, current_node.left, False)
        else:
            return self.update(current_value,  update_value, current_node.right, False)
    
    def preorder(self, current_node = None, is_root_call = True):
        if is_root_call:
            current_node = self.root
        
        if current_node is None:
            return 

        print(f"({current_node.data})",end=" ")
        self.preorder(current_node.left, False)
        self.preorder(current_node.right, False)

    def inorder(self, current_node = None, is_root_call = True):
        if is_root_call:
            current_node = self.root
        
        if current_node is None:
            return 
       
        self.inorder(current_node.left, False)
        print(f"({current_node.data})",end=" ")
        self.inorder(current_node.right, False)

    def postorder(self, current_node = None, is_root_call = True):
        if is_root_call:
            current_node = self.root
        
        if current_node is None:
            return 

        self.postorder(current_node.left, False)
        self.postorder(current_node.right, False)
        print(f"({current_node.data})",end=" ")

    @staticmethod
    def clone(old_tree):
        def copy(node):
            if node is None:
                return None

            new_node = BSTNode(node.data)
            new_node.left = copy(node.left)
            new_node.right = copy(node.right)
            return new_node
            
        new_tree = BST()
        new_tree.root = copy(old_tree.root)
        return new_tree

    def size(self):
        return self.count_node
    
    def height(self, current_node = None, is_root_call = True):
        if is_root_call:
            current_node = self.root
        if current_node is None:
            return -1

        left_count = self.height(current_node.left, False)
        right_count = self.height(current_node.right, False)

        return 1 + max(left_count, right_count)

    def leaf(self, current_node = None, is_root_call = True):
        if is_root_call:
            current_node = self.root
        
        if current_node is None:
            return 0
        
        if current_node.left is None and current_node.right is None:
            return 1
        
        return(
        self.leaf(current_node.left, False) +
        self.leaf(current_node.right, False)
        )

    def is_empty(self):
        if self.root is None:
            return True
        return False
    
    def is_leaf(self, target_value, current_node = None, is_root_call = True):
        if is_root_call:
            current_node = self.root
        
        if current_node is None:
            return 

        if current_node.data == target_value:
            return current_node.left is None and current_node.right is None
                
        self.is_leaf(target_value, current_node.left, False)
        self.is_leaf(target_value, current_node.right, False)
    

def main():
    tree = BST()
    ret = 0

    tree.insert(50)
    tree.insert(30)
    tree.insert(70)
    tree.insert(20)
    tree.insert(40)
    tree.insert(60)
    tree.insert(80)

    tree.preorder()
    print()
    tree.inorder()
    print()
    tree.postorder()
    print()

    value = 10
    ret = tree.search(value)
    if ret != -1:
        print(f"The '{value}' Value is present")
    else:
        print(f"The Value {value} is 'NOT' present")

    value = 20
    new_value = 111
    ret = tree.update(value, new_value)
    if ret == True:
        print(f"Value updated {value} -> {new_value} ")
    else:
        print("Unbale to update the value")
    
    tree.inorder()
    print()

    # tree.clear()

    tree.inorder()
    print()


    newT = BST.clone(tree)
    newT.preorder()
    print()

    print("The total node are: ", tree.size())

    print("The height of tree is:",tree.height())

    print("The total leaf node is:",tree.leaf())

    print("The tree is empty or not:",tree.is_empty())

    data = 80
    print("The current node is leaf or not:",tree.is_leaf(data))

if __name__ == "__main__":
    main()
