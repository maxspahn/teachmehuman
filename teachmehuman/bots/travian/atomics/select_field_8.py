import time
import pyautogui

def select_field_8():

	time.sleep(0.1)
	pyautogui.moveTo(430, 607)
	pyautogui.mouseDown()
	pyautogui.moveTo(430, 607)
	pyautogui.mouseUp()


if __name__ == "__main__":
	select_field_8()
