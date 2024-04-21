import time
import pyautogui

def select_building_2():

	time.sleep(0.1)
	pyautogui.moveTo(643, 504)
	pyautogui.mouseDown()
	pyautogui.moveTo(643, 504)
	pyautogui.mouseUp()


if __name__ == "__main__":
	select_building_2()
