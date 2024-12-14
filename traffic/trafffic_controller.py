import time


class TrafficController:
    def __init__(self, lights):
        self.lights = lights
        self.start = self._start()

    def _start(self):
        while True:
            self.decision()
            time.sleep(15)

    def decision(self):
        road1 = sum([light.length for light in self.lights if 1.1 <= light.id <= 1.2])
        road2 = sum([light.length for light in self.lights if 2.1 <= light.id <= 2.2])

        self.next_color_road1() if road1 > road2 else self.next_color_road2()

    def next_color_road1(self):
        for light in self.lights:
            if light.type == '🚗' and 1.1 <= light.id <= 1.2:
                light.change_color('⚫🌕⚫'), light.add_event({'color': '⚫⚫🤢', 'duration': 3, 'time': 15}) if light.color == '🔴⚫⚫' else ...
                light.update_length(0), light.change_color('⚫🌕⚫'), light.add_event({'color': '🔴⚫⚫', 'duration': 3, 'time': 30}) if light.color == '⚫⚫🤢' else ...
            elif light.type == '👫' and 2.3 <= light.id <= 2.4:
                light.add_event({'color': '⚫🤢  ', 'time': 15}), light.update_length(0) if light.color == '🔴⚫  ' else light.add_event({'color': '🔴⚫  ', 'time': 30})
            else:
                light.change_color('🔴⚫⚫' if light.type == '🚗' else '🔴⚫  ')

    def next_color_road2(self):
        for light in self.lights:
            if light.type == '🚗' and 2.1 <= light.id <= 2.2:
                light.change_color('⚫🌕⚫'), light.add_event({'color': '⚫⚫🤢', 'duration': 3, 'time': 15}) if light.color == '🔴⚫⚫' else ...
                light.update_length(0), light.change_color('⚫🌕⚫'), light.add_event({'color': '🔴⚫⚫', 'duration': 3, 'time': 30}) if light.color == '⚫⚫🤢' else ...
            elif light.type == '👫' and 1.3 <= light.id <= 1.4:
                light.add_event({'color': '⚫🤢  ', 'time': 15}), light.update_length(0) if light.color == '🔴⚫  ' else light.add_event({'color': '🔴⚫  ', 'time': 30})
            else:
                light.change_color('🔴⚫⚫' if light.type == '🚗' else '🔴⚫  ')
