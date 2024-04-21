import time
import pyautogui

def select_field_5():

	time.sleep(0.1)
	pyautogui.moveTo(671, 531)
	pyautogui.mouseDown()
	pyautogui.moveTo(671, 531)
	pyautogui.mouseUp()


if __name__ == "__main__":
	select_field_5()
