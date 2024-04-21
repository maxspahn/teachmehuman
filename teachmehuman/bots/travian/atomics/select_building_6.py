import time
import pyautogui

def select_building_6():

	time.sleep(0.1)
	pyautogui.moveTo(515, 577)
	pyautogui.mouseDown()
	pyautogui.moveTo(515, 577)
	pyautogui.mouseUp()


if __name__ == "__main__":
	select_building_6()
