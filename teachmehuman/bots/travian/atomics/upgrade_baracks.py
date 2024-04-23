import time
import pyautogui

def upgrade_baracks():

	time.sleep(1.0)
	pyautogui.moveTo(456, 176)
	pyautogui.mouseDown()
	pyautogui.moveTo(456, 176)
	pyautogui.mouseUp()
	time.sleep(1.0)
	pyautogui.moveTo(712, 619)
	pyautogui.mouseDown()
	pyautogui.moveTo(712, 619)
	pyautogui.mouseUp()
	time.sleep(1.0)
	pyautogui.moveTo(540, 703)
	pyautogui.mouseDown()
	pyautogui.moveTo(540, 703)
	pyautogui.mouseUp()


if __name__ == "__main__":
	upgrade_baracks()
