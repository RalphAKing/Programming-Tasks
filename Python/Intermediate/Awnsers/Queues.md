# Queues

## Class

```python
import pygame
import random

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop() if not self.is_empty() else None
    
    def peek(self):
        return self.items[0] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __iter__(self):
        return iter(self.items)

class SnakeGame:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.block_size = 20
        
        self.snake = Queue()
        self.snake.enqueue((width//2, height//2))
        self.direction = (self.block_size, 0)
        self.food = self._generate_food()
        self.score = 0
        
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
    
    def _generate_food(self):
        x = random.randrange(0, self.width - self.block_size, self.block_size)
        y = random.randrange(0, self.height - self.block_size, self.block_size)
        return (x, y)

    def _check_collision(self, position):
        if (position[0] < 0 or position[0] >= self.width or 
            position[1] < 0 or position[1] >= self.height):
            return True
            
        snake_list = list(self.snake)
        return position in snake_list[1:] 
    
    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != (0, self.block_size):
                    self.direction = (0, -self.block_size)
                elif event.key == pygame.K_DOWN and self.direction != (0, -self.block_size):
                    self.direction = (0, self.block_size)
                elif event.key == pygame.K_LEFT and self.direction != (self.block_size, 0):
                    self.direction = (-self.block_size, 0)
                elif event.key == pygame.K_RIGHT and self.direction != (-self.block_size, 0):
                    self.direction = (self.block_size, 0)
        return True

    def _draw(self):
        self.screen.fill((0, 0, 0))

        for segment in self.snake:
            pygame.draw.rect(self.screen, (0, 255, 0), 
                           (segment[0], segment[1], self.block_size-2, self.block_size-2))

        pygame.draw.rect(self.screen, (255, 0, 0),
                        (self.food[0], self.food[1], self.block_size-2, self.block_size-2))
        
        pygame.display.flip()
    
    def _move_snake(self):
        head = self.snake.peek()
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        
        if self._check_collision(new_head):
            return False
            
        self.snake.enqueue(new_head)
        
        if new_head == self.food:
            self.score += 1
            self.food = self._generate_food()
        else:
            self.snake.dequeue()
            
        return True

    def run(self):
        running = True
        while running:
            running = self._handle_input()
            if not running or not self._move_snake():
                break
                
            self._draw()
            self.clock.tick(10)
            
        pygame.quit()
        return self.score

if __name__ == "__main__":
    game = SnakeGame()
    final_score = game.run()
    print(f"Game Over! Final Score: {final_score}")
```