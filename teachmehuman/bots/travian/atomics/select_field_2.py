import time
import pyautogui

def select_field_2():

	time.sleep(0.1)
	pyautogui.moveTo(614, 387)
	pyautogui.mouseDown()
	pyautogui.moveTo(614, 387)
	pyautogui.mouseUp()


if __name__ == "__main__":
	select_field_2()
