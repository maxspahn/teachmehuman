"""
Converts the recording.json file to a Python script 
'play.py' to use with PyAutoGUI.

The 'play.py' script may require editing and adapting 
before use.

Always review 'play.py' before running with PyAutoGUI!
"""
import json
import sys

key_mappings = {
    "cmd": "win",
    "alt_l": "alt",
    "alt_r": "alt",
    "ctrl_l": "ctrl",
    "ctrl_r": "ctrl"
}


def read_json_file(file_name: str):
    """

    Excludes released and scrolling events to 
    keep things simple.
    """
    with open(file_name) as f:
        recording = json.load(f)

    def excluded_actions(object):
        return "released" not in object["action"] and \
               "scroll" not in object["action"]

    recording = list(filter(excluded_actions, recording))

    return recording


def convert_to_pyautogui_script(file_name: str):
    """
    Converts to a Python template script 'play.py' to 
    use with PyAutoGUI.

    Converts the:

    - Mouse clicks
    - Keyboard input
    - Time between actions calculated
    """

    recording = read_json_file(file_name)

    action = file_name.split('.')[0]
    
    outfile_name = action + '.py'
    output = open(outfile_name, "w")
    output.write("import time\n")
    output.write("import pyautogui\n\n")
    output.write(f"def {action}():\n\n")
    
    for i, step in enumerate(recording):

        """
        not_first_element = (i - 1) > 0
        if not_first_element:
            ## compare time to previous time for the 'sleep' with a 10% buffer
            pause_in_seconds = (step["_time"] - recording[i - 1]["_time"]) * 1.1 

            output.write(f"time.sleep({pause_in_seconds})\n\n")
        else:
            output.write("time.sleep(1)\n\n")
        """

        if step["action"] == "pressed_key":
            key = step["key"].replace("Key.", "") if "Key." in step["key"] else step["key"]

            if key in key_mappings.keys():
                key = key_mappings[key]

            output.write(f"\tpyautogui.press('{key}')\n")

        
        if step["action"] == "clicked":
            output.write("\ttime.sleep(0.1)\n")
            output.write(f"\tpyautogui.moveTo({step['x']}, {step['y']})\n")

            if step["button"] == "Button.right":
                output.write("\tpyautogui.mouseDown(button='right')\n")
            else:
                output.write("\tpyautogui.mouseDown()\n")

        if step["action"] == "unclicked":
            output.write(f"\tpyautogui.moveTo({step['x']}, {step['y']})\n")

            if step["button"] == "Button.right":
                output.write("\tpyautogui.mouseUp(button='right')\n")
            else:
                output.write("\tpyautogui.mouseUp()\n")

    output.write("\n\n")
    output.write('if __name__ == "__main__":\n')
    output.write(f"\t{action}()\n")

    print("Recording converted. Saved to 'play.py'")


def rec2script():
    file_names = sys.argv[1:]
    for file_name in file_names:
        convert_to_pyautogui_script(file_name)

