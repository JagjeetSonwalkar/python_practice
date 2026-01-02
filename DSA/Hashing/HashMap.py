# hash map/ Dict

# node of hash map
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class Dict:
    def __init__(self, size = 10):
        self.count_node = 0
        self.table = [None] * size
    
    # Hash function
    def _hash(self, key):
        return hash(key) % self.size
    
    # insert or update key - value
    def update(self, key, value):
        index = self._hash(key)

        if self.table is None:
            self.table[index] = Node(key, value)
            self.count_node += 1
            return True
        
        temp = self.table[index]

        while temp.next is None:
            if temp.key == key:
                temp.value = value # update value
                return True
            temp = temp.next
        temp.next = Node(key, value)
    
    # display hash map
    def show(self):
        for i in enumerate(self.table):
            print(f"Bucket {i}:", end=" ")
            current = node
            while current:
                print(f"({current.key}: {current.value})", end=" -> ")
                current = current.next
            print("None")
    
def main():
    dict_obj = Dict()

    dict_obj.update(1, "Rohit")
    dict_obj.update(2, "Virat")
    dict_obj.update(3, "Hardik")

    dict_obj.show()

if __name__ == "__main__":
    main()

