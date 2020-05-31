#!/usr/bin/env python
from random import randint, sample
from PIL import Image, ImageDraw


class Picture():
  def __init__(self, width, height, rec_type='labrynth'):
    self.width = width
    self.height = height
    self.array = [[False for x in range(width)] for y in range(height)]
    self.history = []
    if rec_type == 'labrynth':
      self.type = 0
    elif rec_type == 'maze':
      self.type = 1
    elif rec_type == 'weird':
      self.type = 2
    else:
      raise ValueError('Unknown rec_type')

  def print(self):
    for row in self.array:
      print("".join(['#' if r else ' ' for r in row]))

  def start(self, point=None):
    if point is None:
      point = (int(self.width/2), int(self.height-1))
    self.array[point[1]][point[0]] = True
    self.history.append(point)

  def start_random(self):
    self.start((randint(0, self.width - 1), randint(0, self.height - 1)))

  def start_center(self):
    self.start((int(self.width/2), int(self.height/2)))

  def run(self):
    while len(self.history) > 0:
      self.next()

  def next_point(self):
    if self.type == 0:
      return self.history[-1], -1
    elif self.type == 1:
      r = randint(0, len(self.history) - 1)
      return self.history[r], r
    elif self.type == 2:
      r = randint(0, 1)
      return self.history[-r], -r

  def next(self):
    current, index = self.next_point()

    options = []
    up = (current[0], current[1] + 2)
    down = (current[0], current[1] - 2)
    left = (current[0] - 2, current[1])
    right = (current[0] + 2, current[1])
    if self.available(up):
      options.append(up)
    if self.available(right):
      options.append(right)
    if self.type != 2 or len(options) == 0:
      if self.available(down):
        options.append(down)
      if self.available(left):
        options.append(left)

    if len(options) == 0:
      self.history.pop(index)
      return

    d = sample(options, 1)[0]
    self.history.append(d)
    for i in range(min(current[0], d[0]), max(current[0], d[0]) + 1):
      for j in range(min(current[1], d[1]), max(current[1], d[1]) + 1):
        self.array[j][i] = True

  def inside(self, x, y):
    return x >= 0 and y >= 0 and x < self.width and y < self.height

  def available(self, point):
    x,y = point
    if not self.inside(x, y):
      return False

    if self.array[y][x]:
      return False

    if self.inside(x-1, y) and self.array[y][x-1]:
      return False

    if self.inside(x+1, y) and self.array[y][x+1]:
      return False

    if self.inside(x, y-1) and self.array[y-1][x]:
      return False

    if self.inside(x, y+1) and self.array[y+1][x]:
      return False

    return True

  def to_image(self, file_name="image.png"):
    im = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))

    img = ImageDraw.Draw(im)

    for y in range(self.height):
      for x in range(self.width):
        if self.array[y][x]:
          img.point((x,y), (255, 255, 255, 255))

    im.save(file_name)


if __name__ == '__main__':
  # maze, labrynth, weird
  pic = Picture(80, 60, 'labrynth')
  pic.start_random()
  pic.run()
  pic.to_image()

