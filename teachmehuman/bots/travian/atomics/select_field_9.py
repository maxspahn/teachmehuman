import time
import pyautogui

def select_field_9():

	time.sleep(0.1)
	pyautogui.moveTo(336, 552)
	pyautogui.mouseDown()
	pyautogui.moveTo(336, 552)
	pyautogui.mouseUp()


if __name__ == "__main__":
	select_field_9()
