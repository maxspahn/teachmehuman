import time
import pyautogui

def select_field_3():

	time.sleep(0.1)
	pyautogui.moveTo(686, 433)
	pyautogui.mouseDown()
	pyautogui.moveTo(686, 433)
	pyautogui.mouseUp()


if __name__ == "__main__":
	select_field_3()
