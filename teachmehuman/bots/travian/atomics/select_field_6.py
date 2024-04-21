import time
import pyautogui

def select_field_6():

	time.sleep(0.1)
	pyautogui.moveTo(652, 600)
	pyautogui.mouseDown()
	pyautogui.moveTo(652, 600)
	pyautogui.mouseUp()


if __name__ == "__main__":
	select_field_6()
