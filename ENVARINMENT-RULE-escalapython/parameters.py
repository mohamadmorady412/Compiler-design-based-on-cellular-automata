import pygame
import numpy as np

class PygameEnvironment:
  def __init__(self, dimensions, cell_size):
    self.dimensions = dimensions
    self.cell_size = cell_size
    self.screen_width = self.dimensions * self.cell_size
    self.screen_height = self.dimensions * self.cell_size
    pygame.init()
    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
    pygame.display.set_caption("محیط شبیه سازی")
    self.state = np.zeros(shape=(2**dimensions,))
    self.font = pygame.font.Font(None, 32)

  def reset(self):
    self.state = np.zeros(shape=(2**self.dimensions,))
    return self.state

  def step(self, action):
    # ... اعمال action بر روی state ...

    # بررسی حاشیه ها
    for i in range(self.dimensions):
      if self.state[i] == 0 or self.state[i] == 2**self.dimensions - 1:
        # پرتگاه
        new_position = np.random.randint(0, 2**self.dimensions)
        self.state[i] = new_position

    reward = 0  # ... محاسبه reward ...
    done = False  # ... بررسی اتمام شبیه سازی ...
    info = {}  # ... اطلاعات اضافی ...

    return self.state, reward, done, info

  def render(self):
    self.screen.fill((0, 0, 0))
    for i in range(2**self.dimensions):
      x = i % self.dimensions * self.cell_size
      y = (i // self.dimensions) * self.cell_size
      color = (255, 255, 255) if self.state[i] == 0 else (0, 255, 0)
      pygame.draw.rect(self.screen, color, (x, y, self.cell_size, self.cell_size))

    text = self.font.render(f"State: {self.state}", True, (255, 255, 255))
    self.screen.blit(text, (10, 10))

    pygame.display.flip()

# مثال استفاده از کلاس PygameEnvironment

env = PygameEnvironment(3, 50)
state = env.reset()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # ... انتخاب action ...
  action = ...

  # ... انجام step ...
  next_state, reward, done, info = env.step(action)
  env.render()

  # ... بررسی اتمام شبیه سازی ...
  if done:
    print("شبیه سازی به پایان رسید!")
    break

pygame.quit()

"""import pygame
import numpy as np
from collections import factorial

# With the correct dimensions
def Builder_infinite_degrees(number_free: int) -> list[tuple[int]]:
    controller_list = np.zeros(number_free, dtype=np.int8)
    

class Environment_cd:
    def __init__(self, n_dime: int, Border_areas: np.ndarray | None):
        '''
        n_dime:
          It determines the non-fractal
          dimensions of the environment

        Border_areas:
          Determines whether the edges of the
          environment are killing or spawning
          if None then all env-moves is deadly
          else For each input number except one,
          it recognizes the number of edges of the 
          environment as spawning cells. 
        
        '''
        self.n_dime = n_dime
        self._number_moves = 2 * n_dime + 1
        self._cervition = factorial(n_dime)
"""
