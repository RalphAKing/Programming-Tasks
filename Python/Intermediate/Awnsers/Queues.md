# Queues

## Class

```python
from collections import deque
import random
import pygame

class SnakeGame:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.block_size = 20

        self.snake = deque()
        self.snake.append((width//2, height//2)) 
        self.direction = (self.block_size, 0)  
        self.food = self._generate_food()
        self.score = 0

        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        
    def _generate_food(self):
        x = random.randrange(0, self.width, self.block_size)
        y = random.randrange(0, self.height, self.block_size)
        return (x, y)
    
    def _move_snake(self):
        current_head = self.snake[0]
        new_head = (current_head[0] + self.direction[0], 
                   current_head[1] + self.direction[1])
        
        if self._check_collision(new_head):
            return False
            
        self.snake.appendleft(new_head)
        
        if new_head == self.food:
            self.score += 1
            self.food = self._generate_food()
        else:
            self.snake.pop() 
            
        return True
    
    def _check_collision(self, position):
        if (position[0] < 0 or position[0] >= self.width or 
            position[1] < 0 or position[1] >= self.height):
            return True
            
        if position in list(self.snake)[1:]:
            return True
            
        return False
    
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
                           (segment[0], segment[1], self.block_size, self.block_size))
        
        pygame.draw.rect(self.screen, (255, 0, 0),
                        (self.food[0], self.food[1], self.block_size, self.block_size))
        
        pygame.display.flip()
    
    def run(self):
        running = True
        while running:
            running = self._handle_input()
            if not self._move_snake():
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