import sys
import time
import json

from pynput import keyboard, mouse


class RecordingManager():
    _interval: float = 0.1

    def __init__(self):
        self._name = sys.argv[1]
        self._counter = 0
        self._recording = False
        self._record = []
        self._keyboard_listener = keyboard.Listener(
            on_press=self._on_press,
            on_release=self._on_release)
        self._mouse_listener = mouse.Listener(
            on_click=self._on_click,
            on_scroll=self._on_scroll,
            on_move=self._on_move)
        self._mouse_listener.start()
        self._keyboard_listener.start()
        self._active = True

    @property
    def active(self):
        return self._active

    def start_recording(self):
        self._counter += 1
        self._record = []
        self._recording = True

    def stop_recording(self):
        with open(f"{self._name}_{self._counter}.json", "w") as f:
            json.dump(self._record, f)
        self._recording = False

    def stop_threads(self):
        self._keyboard_listener.join()
        self._mouse_listener.join()

    def _on_press(self, key):
        if key == keyboard.Key.esc:
            self.stop_recording()
        if key == keyboard.Key.space:
            self.start_recording()

    def _on_release(self, key):
        print(f'on_release : {key}')

    def _on_click(self, x, y, button, pressed):
        json_object = {
            'action':'clicked' if pressed else 'unclicked', 
            'button':str(button), 
            'x':x, 
            'y':y, 
            '_time':time.time()
        }
        self._add_action(json_object, force=True)

    def _on_move(self, x, y):
        json_object = {
            'action':'moved', 
            'x':x, 
            'y':y, 
            '_time':time.time()
        }
        self._add_action(json_object)

    def _on_scroll(self, x, y, dx, dy):
        json_object = {
            'action': 'scroll', 
            'vertical_direction': int(dy), 
            'horizontal_direction': int(dx), 
            'x':x, 
            'y':y, 
            '_time': time.time()
        }
        self._add_action(json_object)

    def _add_action(self, action, force=False):
        if len(self._record) == 0 or force:
            self._record.append(action)
        elif time.time() - self._record[-1]['_time'] > self._interval:
            self._record.append(action)

    def run(self):
        while self.active:
            time.sleep(self._interval)
            print("Recording: {}".format(self._recording))
        self.stop_threads()

