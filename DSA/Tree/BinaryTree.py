# Binary Search Tree (BST)

class BinaryTreeNode:
    def __init__(self, data):
        self.left = None 
        self.data = data
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.count_node = 0

    def insert(self, data, current_node = None):
        if self.root is None:
            self.root = BinaryTreeNode(data)
            self.count_node += 1
            return True
        
        if current_node is None:
            current_node = self.root
        
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = BinaryTreeNode(data)
                self.count_node += 1
                return True
            else:
                self.insert(data, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = BinaryTreeNode(data)
                self.count_node += 1
                return True
            else:
                self.insert(data, current_node.right)
        ################### END ##############################

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
    
    def search(self, target_value, current_node=None, parent_node=None):
        if current_node is None and parent_node is None:
            current_node = self.root

        # Tree empty or value not found
        if current_node is None:
            return -1

        if target_value == current_node.data:
            return current_node.data

        if target_value < current_node.data:
            return self.search(target_value, current_node.left, current_node)
        else:
            return self.search(target_value, current_node.right, current_node)

    def inorder(self, temp = None):
        if temp is None:
            temp = self.root
        if temp is None:
            return 
        if temp.left:
            self.inorder(temp.left)
        print(f"({temp.data})",end=" ")
        if temp.right:
            self.inorder(temp.right)
    
    def preorder(self, temp = None):
        if temp is None:
            temp = self.root
        if temp is None:
            return 

        print(f"({temp.data})",end=" ")
        if temp.left:
            self.preorder(temp.left)
        if temp.right:
            self.preorder(temp.right)
    
    def postorder(self, temp = None):
        if temp is None:
            temp = self.root
        if temp is None:
            return 
        if temp.left:
            self.postorder(temp.left)
        if temp.right:
            self.postorder(temp.right)
        print(f"({temp.data})",end=" ")

    def size(self):
        return self.count_node
    
    def leaf_node(self, current_node=None, is_root_call=True):
        # Assign root only ONCE
        if is_root_call:
            current_node = self.root

        # Stop recursion
        if current_node is None:
            return 0

        # Leaf node
        if current_node.left is None and current_node.right is None:
            return 1

        # Recursive calls (never reset root again)
        left_count = self.leaf_node(current_node.left, False)
        right_count = self.leaf_node(current_node.right, False)

        return left_count + right_count
    
    def height(self, current_node=None, is_root_call=True):
        # Assign root only for the first call
        if is_root_call:
            current_node = self.root

        # Empty tree or subtree
        if current_node is None:
            return -1

        # Compute height of left and right subtrees
        left_height = self.height(current_node.left, False)
        right_height = self.height(current_node.right, False)

        # Height of current node = 1 + max of left and right
        return 1 + max(left_height, right_height)
    
    def get_root(self):
        if self.root is None:
            return None
        return self.root.data
 

def main():
    tree = BinaryTree()
    border = '-'*69

    # -------------------- RUN SHELL --------------------
    while True:
        print(border)
        print("1. Insert node")
        print("2. Remove node")
        print("3. Search node")
        print("4. Inorder traversal")
        print("5. Preorder traversal")
        print("6. Postorder traversal")
        print("7. Count leaf nodes")
        print("8. Height of tree")
        print("9. Get root data")
        print("10. Tree size")
        print("0. Exit")
        print(border)

        # Safely convert input to int
        try:
            user_choice = int(input("Enter your choice: ").strip())
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        print(border)

        if user_choice == 1:
            data = input("Enter value to insert: ")
            tree.insert(data)
            print(f"Inserted '{data}' successfully.")

        elif user_choice == 2:
            data = input("Enter value to remove: ")
            removed = tree.remove(data)
            if removed != -1:
                print(f"Removed '{removed}' successfully.")
            else:
                print(f"Value '{data}' not found in the tree.")

        elif user_choice == 3:
            data = input("Enter value to search: ")
            found = tree.search(data)
            if found != -1:
                print(f"Value '{found}' found in the tree.")
            else:
                print(f"Value '{data}' not found in the tree.")

        elif user_choice == 4:
            print("Inorder traversal:")
            tree.inorder()
            print()

        elif user_choice == 5:
            print("Preorder traversal:")
            tree.preorder()
            print()

        elif user_choice == 6:
            print("Postorder traversal:")
            tree.postorder()
            print()

        elif user_choice == 7:
            print("Leaf nodes count:", tree.leaf_node())

        elif user_choice == 8:
            print("Height of tree:", tree.height())

        elif user_choice == 9:
            print("Root node data:", tree.get_root())

        elif user_choice == 10:
            print("Total nodes in tree:", tree.size())

        elif user_choice == 0:
            print("Exiting Binary Tree shell. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()