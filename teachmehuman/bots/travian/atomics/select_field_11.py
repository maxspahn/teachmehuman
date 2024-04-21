import time
import pyautogui

def select_field_11():

	time.sleep(0.1)
	pyautogui.moveTo(366, 414)
	pyautogui.mouseDown()
	pyautogui.moveTo(366, 414)
	pyautogui.mouseUp()


if __name__ == "__main__":
	select_field_11()
