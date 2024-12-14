import time
import random


class TrafficLight:
    def __init__(self, id, type, direction, color):
        self.id = id
        self.type = type
        self.direction = direction
        self.color = color
        self.length = self._get_length()
        self.events = []

    def _get_length(self):
        return random.randint(0, 10)

    def _handle_event(self, event):
        if event:
            self.color = event['color']
            print(f"{self.color} {self.direction} {self.length*('🚗' if self.type == '🚗' else '👫')}")
            if 'duration' in event:
                time.sleep(event['duration'])
                self.change_color(event['color'])
            if 'time' in event:
                time.sleep(event['time'])

    def _process_events(self):
        while self.events:
            event = self.events.pop(0)
            self._handle_event(event)

    def add_event(self, event):
        self.events.append(event)
        self._process_events()

    def change_color(self, color):
        self.add_event({'type': 'смена цвета', 'color': color})

    def update_length(self, new_length):
        self.length = new_length
