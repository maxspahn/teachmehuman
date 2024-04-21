import time
import pyautogui

def select_wall():

	time.sleep(0.1)
	pyautogui.moveTo(657, 735)
	pyautogui.mouseDown()
	pyautogui.moveTo(657, 735)
	pyautogui.mouseUp()


if __name__ == "__main__":
	select_wall()
