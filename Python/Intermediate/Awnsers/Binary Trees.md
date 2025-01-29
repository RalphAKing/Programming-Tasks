# Binary Trees Solution 

## Class

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value == node.value:
            return  
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)
    
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        if node is None:
            return None
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            min_node = self._find_min(node.right)
            node.value = min_node.value
            node.right = self._delete_recursive(node.right, min_node.value)
        
        return node
    
    def _find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

def main():
    bst = BinarySearchTree()
    
    # Test insertion
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    for value in values:
        bst.insert(value)
    
    # Test traversals
    print("Inorder traversal:", bst.inorder_traversal())
    print("Preorder traversal:", bst.preorder_traversal())
    print("Postorder traversal:", bst.postorder_traversal())
    
    # Test search
    print("Search for 6:", "Found" if bst.search(6) else "Not found")
    print("Search for 15:", "Found" if bst.search(15) else "Not found")
    
    # Test deletion
    bst.delete(3)
    print("After deleting 3, inorder traversal:", bst.inorder_traversal())

if __name__ == "__main__":
    main()
```

## Function

```python
def create_node(value):
    return {
        'value': value,
        'left': None,
        'right': None
    }

def insert(tree, value):
    if not tree:
        return create_node(value)
    
    if value < tree['value']:
        tree['left'] = insert(tree['left'], value)
    elif value > tree['value']:
        tree['right'] = insert(tree['right'], value)
    return tree

def search(tree, value):
    if not tree or tree['value'] == value:
        return tree
    if value < tree['value']:
        return search(tree['left'], value)
    return search(tree['right'], value)

def find_min(tree):
    current = tree
    while current and current['left']:
        current = current['left']
    return current

def delete(tree, value):
    if not tree:
        return None
        
    if value < tree['value']:
        tree['left'] = delete(tree['left'], value)
    elif value > tree['value']:
        tree['right'] = delete(tree['right'], value)
    else:
        if not tree['left']:
            return tree['right']
        elif not tree['right']:
            return tree['left']
            
        temp = find_min(tree['right'])
        tree['value'] = temp['value']
        tree['right'] = delete(tree['right'], temp['value'])
    return tree

def inorder_traversal(tree):
    result = []
    if tree:
        result.extend(inorder_traversal(tree['left']))
        result.append(tree['value'])
        result.extend(inorder_traversal(tree['right']))
    return result

def preorder_traversal(tree):
    result = []
    if tree:
        result.append(tree['value'])
        result.extend(preorder_traversal(tree['left']))
        result.extend(preorder_traversal(tree['right']))
    return result

def postorder_traversal(tree):
    result = []
    if tree:
        result.extend(postorder_traversal(tree['left']))
        result.extend(postorder_traversal(tree['right']))
        result.append(tree['value'])
    return result

def main():
    # Initialize empty tree
    bst = None
    
    # Test insertions
    test_values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    for value in test_values:
        bst = insert(bst, value)
    
    # Test traversals
    print("Inorder traversal:", inorder_traversal(bst))
    print("Preorder traversal:", preorder_traversal(bst))
    print("Postorder traversal:", postorder_traversal(bst))
    
    # Test search
    print("Search for 6:", "Found" if search(bst, 6) else "Not found")
    print("Search for 15:", "Found" if search(bst, 15) else "Not found")
    
    # Test deletion
    bst = delete(bst, 3)
    print("After deleting 3, inorder traversal:", inorder_traversal(bst))

if __name__ == "__main__":
    main()
```