
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BSTGenerator:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        
        for current in self._traverse_to_insert():
            if value == current.value:
                return  # No duplicates
            if value < current.value:
                if not current.left:
                    current.left = Node(value)
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = Node(value)
                    break
                current = current.right
    
    def _traverse_to_insert(self):
        current = self.root
        while current:
            yield current
            
    def search(self, value):
        return next((node for node in self._traverse_search(value) if node.value == value), None)
    
    def _traverse_search(self, value):
        current = self.root
        while current:
            yield current
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                break
                
    def delete(self, value):
        parent = None
        current = self.root
        
        # Find node to delete
        for node in self._traverse_search(value):
            if node.value == value:
                current = node
                break
            parent = node
            
        if not current:
            return
            
        # Handle deletion cases
        if not current.right:
            if parent:
                if parent.left == current:
                    parent.left = current.left
                else:
                    parent.right = current.left
            else:
                self.root = current.left
        else:
            successor_parent = current
            successor = current.right
            while successor.left:
                successor_parent = successor
                successor = successor.left
                
            current.value = successor.value
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
    
    def inorder_traversal(self):
        yield from self._inorder_generator(self.root)
    
    def _inorder_generator(self, node):
        if node:
            yield from self._inorder_generator(node.left)
            yield node.value
            yield from self._inorder_generator(node.right)
    
    def preorder_traversal(self):
        yield from self._preorder_generator(self.root)
    
    def _preorder_generator(self, node):
        if node:
            yield node.value
            yield from self._preorder_generator(node.left)
            yield from self._preorder_generator(node.right)
    
    def postorder_traversal(self):
        yield from self._postorder_generator(self.root)
    
    def _postorder_generator(self, node):
        if node:
            yield from self._postorder_generator(node.left)
            yield from self._postorder_generator(node.right)
            yield node.value

def main():
    bst = BSTGenerator()
    
    # Test insertions
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    for value in values:
        bst.insert(value)
    
    # Test traversals
    print("Inorder traversal:", list(bst.inorder_traversal()))
    print("Preorder traversal:", list(bst.preorder_traversal()))
    print("Postorder traversal:", list(bst.postorder_traversal()))
    
    # Test search
    print("Search for 6:", "Found" if bst.search(6) else "Not found")
    print("Search for 15:", "Found" if bst.search(15) else "Not found")
    
    # Test deletion
    bst.delete(3)
    print("After deleting 3, inorder traversal:", list(bst.inorder_traversal()))

if __name__ == "__main__":
    main()
