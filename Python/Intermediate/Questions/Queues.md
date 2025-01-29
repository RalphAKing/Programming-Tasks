# Queues

## Task Description
Create a snake game where the snake's movement and growth are managed using a queue data structure.

## Core Requirements
1. Snake Implementation
   - Use a queue to store the snake's body segments
   - Head of the snake should be at the front of the queue
   - Tail should be at the back of the queue

2. Movement Mechanics
   - When snake moves, enqueue new head position
   - Dequeue tail position (unless food is eaten)
   - Support 4 directional movement (UP, DOWN, LEFT, RIGHT)

3. Game Elements
   - Snake grows when eating food
   - Food appears randomly on the board
   - Game ends when snake hits walls or itself

## Technical Requirements
1. Data Structures
   - Queue implementation for snake body
   - Grid-based game board

2. Game Logic
   - Movement validation
   - Collision detection
   - Score tracking
   - Food placement logic

## Bonus Features
- High score system
- Increasing difficulty
- Multiple food types
- Visual display of the queue operations

## Learning Objectives
- Queue data structure implementation
- Game state management
- Collision detection algorithms
- Event handling

## Evaluation Criteria
- Correct queue implementation
- Smooth game mechanics
- Code organization
- Error handling
