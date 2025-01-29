# Binary Trees

## Task Description
Implement a complete Binary Search Tree (BST) data structure with core operations.

## Requirements

### Core Functionality
1. Implement a BST class with the following operations:
   - Insertion of nodes
   - Deletion of nodes
   - Search operation
   - Traversal methods (in-order, pre-order, post-order)

### Technical Requirements
1. Create a Node class with:
   - Value storage
   - Left child pointer
   - Right child pointer

2. BST class must maintain these properties:
   - Left subtree contains only nodes with values less than parent
   - Right subtree contains only nodes with values greater than parent
   - No duplicate values allowed
   - Both subtrees must also be binary search trees

### Expected Methods
- `insert(value)`: Add new node
- `delete(value)`: Remove existing node
- `search(value)`: Find node
- `inorder_traversal()`: Left-Root-Right
- `preorder_traversal()`: Root-Left-Right
- `postorder_traversal()`: Left-Right-Root

## Evaluation Criteria
- Correct implementation of BST properties
- Proper handling of edge cases
- Code organization and clarity
- Time complexity optimization
- Memory usage efficiency

## Bonus Challenges
1. Implement tree balancing
2. Add tree visualization
3. Create method to find tree height
4. Add functionality to check if tree is balanced
