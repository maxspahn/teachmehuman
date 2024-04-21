import time
import pyautogui

def upgrade_main_building():

	time.sleep(0.1)
	pyautogui.moveTo(571, 720)
	pyautogui.mouseDown()
	pyautogui.moveTo(571, 720)
	pyautogui.mouseUp()


if __name__ == "__main__":
	upgrade_main_building()
