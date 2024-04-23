import time
import pyautogui

def jump_to_window_1():

	time.sleep(1.0)
	pyautogui.moveTo(9, 1067)
	pyautogui.mouseDown()
	pyautogui.moveTo(9, 1067)
	pyautogui.mouseUp()


if __name__ == "__main__":
	jump_to_window_1()
