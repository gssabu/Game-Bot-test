"""
This file contains the game control logic.

Author: Arda Mavi
"""
import pyautogui
import pydirectinput
import time

from pynput.mouse import Controller as Mouse
from pynput.keyboard import Key


# For encoding keyboard keys:
def get_keys():
    """
    Returns a list of all the keys that can be pressed.
    :return: The list of keys.
    """
    return ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "Key.space",
            "a", "s", "d", "f", "g", "h", "j", "k", "l", "x", "Key.left", 
            "Key.up", "Key.right", "Key.down", "Key.shift"]


def get_key(key_id):
    """
    Returns the key that corresponds to the given key id.
    :param key_id: Set the key id.
    :return: the key that corresponds to the given key id.
    """
    return get_keys()[key_id]


def get_id(key):
    """
    Returns the id of the given key.
    :param key: The key.
    :return: The id of the given key.
    """
    try:
        print("Key Pressed:", key.char, sep=" ")
        return get_keys().index(key.char)
    except:
        if (str(key) + "") not in get_keys():
            print((str(key) + ""), " is not in list")
            return 1000
    print("Key Pressed:", (str(key) + ""), sep=" ")
    return get_keys().index((str(key) + ""))


mouse = Mouse()


# Mouse:
def move(x, y):
    """
    Moves the mouse to the given coordinates.
    :param x: x coordinate.
    :param y: y coordinate.
    :return: None
    """
    pydirectinput.moveTo(x, y)


def scroll(x, y):
    """
    Scrolls the mouse to the given coordinates.
    :param x: The horizontal scroll.
    :param y: The vertical scroll.
    """
    pydirectinput.scroll(x, y)


def click(x, y):
    """
    Clicks the mouse at the given coordinates.
    :param x: The x coordinate.
    :param y: The y coordinate.
    """
    move(x, y)
    pydirectinput.click()


# Keyboard:
def press(key):
    """
    Presses the given key.
    :param key: The key.
    """
    if key in ["Key.shift", "shift"]:
        pydirectinput.keyDown("shift")
    elif key in ["Key.space", "space"]:
        pydirectinput.keyDown("space")
    else:
        pydirectinput.keyDown(key)


def release(key):
    """
    Releases the given key.
    :param key: the key.
    """
    if key in ["Key.shift", "shift"]:
        pydirectinput.keyUp(Key.shift)
    elif key in ["Key.space", "space"]:
        pydirectinput.keyUp(Key.space)
    else:
        pydirectinput.keyUp(key)
