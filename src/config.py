from math import floor

GameRect = {
    'top': 212,
    'left': 393,
    'width': 273,
    'height': 487
}


class Size:
  __width: int
  __height: int
  __half_width: int
  __half_height: int

  def __init__(self, width: int, height: int):
    self.__width = width
    self.__height = height
    self.__half_width = floor(width / 2)
    self.__half_height = floor(height / 2)

  @property
  def width(self):
    return self.__width

  @property
  def height(self):
    return self.__height

  @property
  def half_width(self):
    return self.__half_width

  @property
  def half_height(self):
    return self.__half_height


TileSize = Size(70, 120)
TileCount = 4

CheckInterval = 0.1
