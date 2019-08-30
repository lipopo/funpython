# -*- coding: utf8 -*-
import os
import math
import numpy as np
import random
from collections import deque
import curses


class Build(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    @property
    def build(self):
        return "---" * self.width + "\n" + ("|" + " " * self.width + "|\n") * self.height


class Map(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = curses.initscr()
        self.windows = curses.newwin(
            0, 0,
            height, width
        )

    @property
    def map(self):
        return self.screen


class Fly(object):
    def __init__(self, start_location):
        self.location = start_location

    def go_step(self, speed, direction):
        self.location[0] = self.location[0] + speed * math.cos(direction)
        self.location[1] = self.location[1] + speed * math.sin(direction)


class FlyBird(object):
    def __init__(self, start_location):
        self.fly_direction = 0.0
        self.fly_speed = 0.0
        self.fly = Fly(start_location)
        self.location = start_location

    def go_step(self, event):
        if event:
            if event == "x_pong":
                self.fly_direction = 2 * math.pi - self.fly_direction
            elif event == "y_pong":
                self.fly_direction = math.pi - self.fly_direction
        if self.fly_direction < 0:
            self.fly_direction += 2 * math.pi

        self.fly.go_step(self.fly_speed, self.fly_direction)
        self.location = self.fly.location

    def set_speed(self, speed):
        self.fly_speed = speed

    def set_direction(self, direction):
        self.fly_direction = direction

    def fly_up(self):
        self.fly_speed += 1.0
        self.fly_direction += 1.0

    @property
    def bird(self):
        return "| |\n| |"

    @property
    def bird_width(self):
        return max(map(lambda row: len(row), self.bird.split("\n")))

    @property
    def bird_height(self):
        return len(self.bird.split("\n"))


class BuildFlow(object):
    def __init__(self, max_height, build_intent, build_width=2, max_len=10):
        self.buildings = deque()
        self.max_len = max_len
        self.max_height = max_height
        self.build_intent = build_intent
        self.build_gen = self.build_generate(build_width)

    def build_generate(self, width):
        while True:
            yield Build(random.randint(0, self.max_len), width)

    def go_step(self):
        self.buildings.append(self.build_gen.next())

    @property
    def build_map_height(self):
        return len(self.build_map.split("\n"))

    @property
    def build_map_width(self):
        return max(map(lambda row: len(row), self.build_map.split("\n")))

    @property
    def intent(self):
        return np.array([" " * self.build_intent for _ in range(self.max_height)]).reshape(-1, 1)

    @property
    def build_map(self):
        buildings = []
        for build in self.buildings:
            building_list = build.build.split("\n")
            building = [" " * (build.width + 3.5) for _ in range(self.max_height - len(building_list))]
            building.extend(building_list)
            building_rot = np.array(building).reshape(-1, 1)
            buildings.append(building_rot)
            buildings.append(self.intent)
        all_build_int = []
        if len(buildings) > 0:
            all_build_int = np.concatenate(buildings, axis=1)
        build_str = []
        for build_row in all_build_int:
            build_str.append("".join(build_row))

        return "\n".join(build_str)


class FlyBirdGame(object):
    def __init__(self, bird, map, build_flow):
        self.bird = bird
        self.map = map
        self.build_flow = build_flow

    def print_map(self):
        self.build_flow.go_step()
        print_map = self.build_flow.build_map
        self.map.addstr(
            0, 0,
            print_map
        )

    def go_step(self):
        event = None
        self.bird.go_step(event)

    @staticmethod
    def clear_map():
        os.system("clear")


if __name__ == "__main__":
    import time
    game_map = Map(100, 30)
    bird = FlyBird([10, 10])
    bird.set_speed(1)
    bird.set_direction(1.0)

    build_flow = BuildFlow(30, 5)
    fly_bird_game = FlyBirdGame(bird, game_map.map, build_flow)
    while True:
        fly_bird_game.print_map()
        fly_bird_game.go_step()
        game_map.screen.refresh()
        time.sleep(1)
