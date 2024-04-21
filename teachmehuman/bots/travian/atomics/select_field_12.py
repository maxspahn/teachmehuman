import time
import pyautogui

def select_field_12():

	time.sleep(0.1)
	pyautogui.moveTo(428, 368)
	pyautogui.mouseDown()
	pyautogui.moveTo(428, 368)
	pyautogui.mouseUp()


if __name__ == "__main__":
	select_field_12()
