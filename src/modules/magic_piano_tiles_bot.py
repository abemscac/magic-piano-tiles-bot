import pyautogui
from pynput.keyboard import Listener
from mss import mss
from mss.base import MSSBase
from mss.models import Monitor
from config import TrackLocations


class MagicPianoTilesBot:
  __detecting: bool = False
  __mss: MSSBase
  __monitor: Monitor

  def __init__(self):
    self.__mss = mss()
    self.__monitor = self.__mss.monitors[0]
    print('MagicPianoTiles bot is running.')
    print("Hold 'Q' to eanble bot, and press any other key to exit.")

  def start(self):
    with Listener(
        on_press=self.__handle_key_press,
        on_release=self.__handle_key_release
    ) as listener:
      listener.join()

  def __handle_key_press(self, key):
    if self.__key_is_q(key):
      if not self.__detecting:
        self.__detecting = True
        print('Detection started.')
      self.__check_and_click()

  def __check_and_click(self):
    screenshot = self.__grab_screenshot()
    for location in TrackLocations:
      x, y = location[0], location[1]
      pixel = screenshot.pixel(x, y)  # (r, g, b)
      if pixel[0] == 0:
        pyautogui.moveTo(x, y)
        pyautogui.leftClick()

  def __grab_screenshot(self):
    return self.__mss.grab(self.__monitor)

  def __handle_key_release(self, key):
    if self.__key_is_q(key):
      self.__detecting = False
      print('Detection ended.')
    else:
      return False

  def __key_is_q(self, key):
    return hasattr(key, 'char') and key.char == 'q'
