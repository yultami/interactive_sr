import random

from traffic.trafffic_controller import TrafficController
from traffic.traffic_light import TrafficLight

road1 = [
    TrafficLight(1.1, '🚗', '↓↓↓', '🔴⚫⚫'),
    TrafficLight(1.2, '🚗', '↑↑↑', '🔴⚫⚫'),
    TrafficLight(1.3, '👫', '⟶⟶⟶', '🔴⚫   '),
    TrafficLight(1.4, '👫', '⟵⟵⟵', '🔴⚫   '),
]
road2 = [
    TrafficLight(2.1, '🚗', '⟶⟶⟶', '🔴⚫⚫'),
    TrafficLight(2.2, '🚗', '⟵⟵⟵', '🔴⚫⚫'),
    TrafficLight(2.3, '👫', '↓↓↓', '🔴⚫   '),
    TrafficLight(2.4, '👫', '↑↑↑', '🔴⚫   '),
]
controller = TrafficController(road1 + road2)
controller.start()
