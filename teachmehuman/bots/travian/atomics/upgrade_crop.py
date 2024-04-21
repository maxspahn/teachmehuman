import time
import pyautogui

def upgrade_crop():

	time.sleep(0.1)
	pyautogui.moveTo(505, 749)
	pyautogui.mouseDown()
	pyautogui.moveTo(505, 749)
	pyautogui.mouseUp()


if __name__ == "__main__":
	upgrade_crop()
