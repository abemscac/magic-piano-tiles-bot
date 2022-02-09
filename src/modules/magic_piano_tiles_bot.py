from math import floor
import time

from config import GameRect, TileSize, TileCount, CheckInterval
from mss import mss
from mss.base import MSSBase
from pynput.keyboard import Listener
from pynput.mouse import Controller


class MagicPianoTilesBot:
  __tile_positions_in_screen: list
  __tile_positions_in_img: list
  __detecting: bool
  __mss: MSSBase
  __mouse: Controller
  __keyboard_listener: Listener

  def __init__(self):
    self.__tile_positions_in_screen = list(
        map(self.__get_tile_position_in_screen_by_index, range(TileCount)))
    self.__tile_positions_in_img = list(
        map(self.__get_tile_position_in_img_by_index, range(TileCount)))
    self.__detecting = False
    self.__mss = mss()
    self.__mouse = Controller()
    self.__keyboard_listener = Listener(on_press=self.__handle_key_press)

  def start(self):
    self.__keyboard_listener.start()
    print('MagicPianoTiles bot is running.')
    print("Press 'Q' to eanble/disable bot.")
    while 1:
      if self.__detecting:
        self.__check_tiles()
      time.sleep(CheckInterval)

  def __get_tile_position_in_screen_by_index(self, index: int):
    x = GameRect.get('left') + TileSize.half_width + (TileSize.width * index)
    y = GameRect.get('top') + GameRect.get('height') - \
        TileSize.height - TileSize.half_height
    return (x, y)

  def __get_tile_position_in_img_by_index(self, index: int):
    x = floor((TileSize.half_width + (TileSize.width * index)) * 2)
    y = floor((GameRect.get('height') -
              TileSize.height - TileSize.half_height) * 2)
    return (x, y)

  def __check_tiles(self):
    img = self.__mss.grab(GameRect)
    for i in range(TileCount):
      pos_in_img = self.__tile_positions_in_img[i]
      pixelR = img.pixel(pos_in_img[0], pos_in_img[1])[0]
      if pixelR <= 5:
        pos_in_screen = self.__tile_positions_in_screen[i]
        print(f"Click tile {i}.")
        self.__click(pos_in_screen[0], pos_in_screen[1])

  def __click(self, x: int, y: int):
    self.__mouse.position = (x, y)
    # self.__mouse.click(Button.left, 1)

  def __handle_key_press(self, key):
    if self.__key_is_q(key):
      if not self.__detecting:
        self.__detecting = True
        print('Detection start.')
      else:
        self.__detecting = False
        print('Detection end.')

  def __key_is_q(self, key):
    return hasattr(key, 'char') and key.char == 'q'
