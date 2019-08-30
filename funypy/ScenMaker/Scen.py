# -*- coding: utf8 -*-
import numpy as np


class Scen(object):
    """
    舞台
    要素:
    舞台大小
    切换舞台背景的工具
    """

    def __init__(self, height, width, depth):
        self.scen_height = height
        self.scen_width = width
        self.scen_depth = depth

        # 初始化舞台
        self.scen_instance = np.zeros(
            (height, width, depth),
            np.float32
        )

        self.scen_borders = None
        self.current_scen = 0
        self.scen_show = None

    def set_scen_border(self, border):
        """设置舞台背景板"""
        self.scen_borders = border

    def load_scen_show(self, scen_show):
        """装载舞台剧"""
        self.scen_show = scen_show
        self.current_scen = 0

    def play_scen_show(self):
        """播放舞台剧下一回目"""
        if self.isplayed:
            return u"播放已经结束"
        play_statue = self.scen_show.play()
        if play_statue:
            # 舞台效果计算
            self.show(play_statue)
            self.current_scen += 1
        else:
            self.current_scen = -1

    def show(self, show_state):
        """计算舞台效果"""
        for item in show_state.items:
            location_lt = item.thing_doing.location
            crop = item.crop
            # 放置
            self.scen_instance[location_lt[0]:, location_lt[1]:] = crop

    @property
    def readyforplay(self):
        """准备好开始播放"""
        if self.scen_show and self.current_scen == 0:
            return True
        return False

    @property
    def isplaying(self):
        """舞台剧正在播放的标志"""
        if self.scen_show and not self.readyforplay:
            return True
        return False

    @property
    def isplayed(self):
        """舞台剧播放结束的标记"""
        if self.scen_show and self.current_scen == -1:
            return True
        return False

