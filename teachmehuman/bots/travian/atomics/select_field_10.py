import time
import pyautogui

def select_field_10():

	time.sleep(0.1)
	pyautogui.moveTo(335, 490)
	pyautogui.mouseDown()
	pyautogui.moveTo(335, 490)
	pyautogui.mouseUp()


if __name__ == "__main__":
	select_field_10()
